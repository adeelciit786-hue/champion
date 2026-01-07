"""
Utility functions for Champion Cleaners
Extracted from app.py to avoid Flask dependencies in Streamlit
"""

from config import FAQ_DATA

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
        return word[:-2]  # shoes -> shoe
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
    
    if not query_keywords:
        return None
    
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
        
        # 2. Answer keyword matching (medium weight)
        answer_matches = 0
        for keyword in query_keywords:
            norm_keyword = normalize_word(keyword)
            if keyword in faq_a_keywords or norm_keyword in [normalize_word(w) for w in faq_a_keywords]:
                answer_matches += 1
        
        if answer_matches > 0:
            score += answer_matches * 50  # Medium weight for answer matches
        
        # 3. Substring phrase matching in question (good weight)
        for i in range(len(query_keywords)):
            for j in range(i+1, min(i+3, len(query_keywords)+1)):
                phrase = ' '.join(query_keywords[i:j])
                if phrase in faq_question:
                    score += 60  # Bonus for phrase matching in question
        
        # 4. Substring phrase matching in answer
        for i in range(len(query_keywords)):
            for j in range(i+1, min(i+3, len(query_keywords)+1)):
                phrase = ' '.join(query_keywords[i:j])
                if phrase in faq_answer:
                    score += 25  # Smaller bonus for phrase matching in answer
        
        # 5. Intersection of normalized keywords
        keyword_intersection = len(normalized_query & normalized_faq)
        if keyword_intersection > 0:
            score += keyword_intersection * 30  # Intersection match score
        
        # Update best match
        if score > best_score:
            best_score = score
            best_match = faq
    
    return best_match if best_score > 0 else None
