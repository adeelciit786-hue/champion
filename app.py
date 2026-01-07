"""
Main Flask Application for Champion Cleaners
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import re
from config import *
from database import save_order, get_order, log_notification

app = Flask(__name__)
app.secret_key = 'champion_cleaners_2025'

# Helper Functions
def validate_phone(phone):
    """Validate UAE phone number."""
    phone = phone.replace(" ", "").replace("-", "")
    pattern = r'^(\+971|0)?[5]{1}[0-9]{8}$'
    return bool(re.match(pattern, phone)), "Invalid phone number format"

def validate_email(email):
    """Validate email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email)), "Invalid email format"

def get_future_dates(days=30):
    """Get list of future dates."""
    dates = []
    for i in range(1, days + 1):
        date = datetime.now() + timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))
    return dates

def get_time_slots():
    """Get available time slots."""
    slots = [
        "8 to 10 AM",
        "10 AM to 12 noon",
        "2 to 4 PM",
        "4 to 6 PM",
        "6 to 8 PM",
        "8 to 10 PM"
    ]
    return slots

# Stop words that should be filtered out during search
STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'or', 'that', 'the', 'to', 'was', 'will',
    'with', 'you', 'your', 'do', 'does', 'how', 'what', 'when', 'where', 'why',
    'can', 'have', 'i', 'we', 'they', 'if', 'this', 'this', 'but', 'which'
}

def normalize_word(word):
    """Convert plural to singular by removing common plural endings."""
    word = word.lower().strip()
    # Handle common plural variations
    if word.endswith('ies'):
        return word[:-3] + 'y'  # babies -> baby
    elif word.endswith('sses'):
        return word[:-2]  # dresses -> dress
    elif word.endswith('ches'):
        return word[:-2]  # dishes -> dish
    elif word.endswith('xes'):
        return word[:-2]  # boxes -> box
    elif word.endswith('zes'):
        return word[:-2]  # buzzes -> buzz
    elif word.endswith('oes'):
        return word[:-2]  # shoes -> shoe (but need to handle special case)
    elif word.endswith('s') and not word.endswith('ss'):
        return word[:-1]  # books -> book
    return word

def get_keywords(text):
    """Extract meaningful keywords from text, removing stop words and short words."""
    words = text.lower().split()
    keywords = []
    
    for word in words:
        # Remove punctuation
        word = ''.join(c for c in word if c.isalnum())
        
        # Filter out stop words and short words
        if len(word) > 2 and word not in STOP_WORDS:
            keywords.append(word)
    
    return keywords

def search_faq(question):
    """Advanced FAQ search with intelligent matching."""
    if not question or len(question.strip()) < 3:
        return None
    
    question_lower = question.lower()
    query_keywords = get_keywords(question)
    
    # Normalize query keywords to handle plural/singular
    normalized_query = set()
    for keyword in query_keywords:
        normalized_query.add(normalize_word(keyword))
        normalized_query.add(keyword)
    
    best_match = None
    best_score = 0
    
    for faq in FAQ_DATA:
        faq_question = faq['question'].lower()
        faq_answer = faq['answer'].lower()
        faq_full_text = faq_question + ' ' + faq_answer
        
        # Extract keywords from FAQ question and answer
        faq_q_keywords = get_keywords(faq_question)
        faq_a_keywords = get_keywords(faq_answer)
        
        # Normalize FAQ keywords
        normalized_faq = set()
        for keyword in faq_q_keywords + faq_a_keywords:
            normalized_faq.add(normalize_word(keyword))
            normalized_faq.add(keyword)
        
        score = 0
        
        # 1. Question keyword matching (highest weight)
        question_matches = 0
        for keyword in query_keywords:
            norm_keyword = normalize_word(keyword)
            if keyword in faq_q_keywords or norm_keyword in [normalize_word(w) for w in faq_q_keywords]:
                question_matches += 1
        
        if question_matches > 0:
            score += question_matches * 100  # High weight for question matches
        
        # 2. Answer keyword matching (medium weight) - BUT reduce if it's just in general text
        answer_matches = 0
        for keyword in query_keywords:
            norm_keyword = normalize_word(keyword)
            if keyword in faq_a_keywords or norm_keyword in [normalize_word(w) for w in faq_a_keywords]:
                answer_matches += 1
        
        if answer_matches > 0:
            score += answer_matches * 50  # Medium weight for answer matches
        
        # 3. Substring phrase matching in question (good weight) - prioritize matches in question
        for i in range(len(query_keywords)):
            for j in range(i+1, min(i+3, len(query_keywords)+1)):
                phrase = ' '.join(query_keywords[i:j])
                if phrase in faq_question:
                    score += 60  # Bonus for phrase matching in question
        
        # 4. Substring phrase matching in answer
        for i in range(len(query_keywords)):
            for j in range(i+1, min(i+3, len(query_keywords)+1)):
                phrase = ' '.join(query_keywords[i:j])
                if phrase in faq_answer and phrase not in ['require', 'processing']:
                    score += 25
        
        # 5. Normalized keyword matching (handles plural/singular)
        normalized_matches = len(normalized_query.intersection(normalized_faq))
        if normalized_matches > 0:
            score += normalized_matches * 30
        
        # 6. Bonus: If FAQ question starts with a service name, give extra weight
        if 'what' in faq_question and ('service' in faq_question or 'cleaning' in faq_question or 'clean' in faq_question):
            if answer_matches > 0 or question_matches > 0:
                score += 40
        
        if score > best_score:
            best_score = score
            best_match = faq
    
    return best_match if best_score > 0 else None

# Routes
@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', colors=BRAND_COLORS, title=APP_TITLE, subtitle=APP_SUBTITLE)

@app.route('/schedule')
def schedule():
    """Schedule pickup page."""
    return render_template('schedule.html', 
                          colors=BRAND_COLORS,
                          services=SERVICES,
                          dates=get_future_dates(),
                          times=get_time_slots(),
                          offers=OFFERS_DATA)

@app.route('/track')
def track():
    """Track order page."""
    return render_template('track.html', colors=BRAND_COLORS)

@app.route('/faq')
def faq():
    """FAQ page."""
    return render_template('faq.html', colors=BRAND_COLORS, faqs=FAQ_DATA)

@app.route('/offers')
def offers():
    """Offers page."""
    return render_template('offers.html', colors=BRAND_COLORS, offers=OFFERS_DATA)

@app.route('/services')
def services():
    """Services page."""
    return render_template('services.html', colors=BRAND_COLORS, services=SERVICES)

# API Endpoints
@app.route('/api/schedule-pickup', methods=['POST'])
def api_schedule_pickup():
    """API endpoint to schedule pickup."""
    try:
        data = request.json
        
        # Validation
        if not data.get('full_name') or len(data['full_name'].strip()) < 2:
            return jsonify({"success": False, "error": "Invalid name"}), 400
        
        phone = data.get('phone_number', '').strip()
        valid, msg = validate_phone(phone)
        if not valid:
            return jsonify({"success": False, "error": msg}), 400
        
        if data.get('email'):
            valid, msg = validate_email(data['email'])
            if not valid:
                return jsonify({"success": False, "error": msg}), 400
        
        if not data.get('address') or len(data['address'].strip()) < 5:
            return jsonify({"success": False, "error": "Please provide a complete address"}), 400
        
        if not data.get('pickup_date'):
            return jsonify({"success": False, "error": "Please select a date"}), 400
        
        if not data.get('pickup_time'):
            return jsonify({"success": False, "error": "Please select a time"}), 400
        
        if not data.get('service_type'):
            return jsonify({"success": False, "error": "Please select a service"}), 400
        
        # Save order
        result = save_order(
            full_name=data['full_name'],
            phone_number=phone,
            email=data.get('email'),
            address=data['address'],
            pickup_date=data['pickup_date'],
            pickup_time=data['pickup_time'],
            service_type=data['service_type'],
            notes=data.get('notes')
        )
        
        if result['success']:
            # Log notification
            log_notification(
                phone_number=phone,
                message=f"New pickup scheduled: {data['service_type']} on {data['pickup_date']}",
                query_type="new_order"
            )
            
            return jsonify({
                "success": True,
                "order_id": result['order_id'],
                "message": "Your pickup has been scheduled successfully!"
            })
        else:
            return jsonify({"success": False, "error": result.get('error', 'Failed to save order')}), 500
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/track-order', methods=['POST'])
def api_track_order():
    """API endpoint to track order."""
    try:
        data = request.json
        search_type = data.get('search_type')
        search_value = data.get('search_value', '').strip()
        
        if not search_value:
            return jsonify({"success": False, "error": "Please provide search value"}), 400
        
        if search_type == 'order_id':
            order = get_order(order_id=search_value)
        elif search_type == 'phone':
            valid, msg = validate_phone(search_value)
            if not valid:
                return jsonify({"success": False, "error": msg}), 400
            order = get_order(phone_number=search_value)
        else:
            return jsonify({"success": False, "error": "Invalid search type"}), 400
        
        if order:
            return jsonify({
                "success": True,
                "order": {
                    "order_id": order['order_id'],
                    "name": order['full_name'],
                    "service": order['service_type'],
                    "date": order['pickup_date'],
                    "time": order['pickup_time'],
                    "status": order['status']
                }
            })
        else:
            # Log notification for team follow-up
            log_notification(
                phone_number=search_value if search_type == 'phone' else 'unknown',
                message=f"Order search failed: {search_type}={search_value}",
                query_type="order_not_found"
            )
            return jsonify({"success": False, "error": "Order not found"}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/search-faq', methods=['POST'])
def api_search_faq():
    """API endpoint to search FAQ."""
    try:
        data = request.json
        question = data.get('question', '').strip()
        
        if not question or len(question) < 3:
            return jsonify({"success": False, "error": "Please enter a valid question"}), 400
        
        result = search_faq(question)
        
        if result:
            return jsonify({
                "success": True,
                "question": result['question'],
                "answer": result['answer']
            })
        else:
            # Log for team
            log_notification(
                phone_number='unknown',
                message=f"Unanswered FAQ question: {question}",
                query_type="faq_unanswered"
            )
            return jsonify({"success": False, "error": "Let us take this forward for you. Kindly share your contact number and our team will contact you soon."}), 404
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/offers', methods=['GET'])
def api_offers():
    """API endpoint to get offers."""
    return jsonify({"success": True, "offers": OFFERS_DATA})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
