"""
FAQ data and retrieval system for Champion Cleaners
"""

import re
from typing import List, Tuple

# Comprehensive FAQ data from Champion Cleaners
FAQ_DATA = [
    {
        "question": "What is your turnaround time for dry cleaning?",
        "answer": "Standard dry cleaning typically takes 3-5 business days. Express service is available for an additional fee and takes 24-48 hours. Please check our website for current timelines.",
        "keywords": ["turnaround", "time", "days", "delivery", "ready"]
    },
    {
        "question": "Do you provide free pickup and delivery?",
        "answer": "Yes! We offer FREE pickup and delivery across Dubai, Abu Dhabi, and Sharjah for orders over the minimum service charge. Simply schedule your pickup through our app or website.",
        "keywords": ["free", "pickup", "delivery", "collection"]
    },
    {
        "question": "What areas do you cover?",
        "answer": "We provide services throughout Dubai, Abu Dhabi, Sharjah, Ajman, and Ras Al Khaimah. Check our coverage map on the website or contact us for your specific area.",
        "keywords": ["coverage", "area", "location", "serve", "deliver"]
    },
    {
        "question": "How do you clean delicate fabrics and wedding gowns?",
        "answer": "Our wedding gown restoration service uses specialized cleaning techniques for delicate and vintage fabrics. We handle silk, lace, beading, and embroidery with utmost care. Our experts inspect each item and use appropriate cleaning methods.",
        "keywords": ["wedding", "gown", "delicate", "fabric", "silk", "lace", "special"]
    },
    {
        "question": "What is your compensation policy for damaged items?",
        "answer": "We take great care with every item. In the unlikely event of damage, we assess it thoroughly and work with you on a fair resolution. Please report any issues within 24 hours of delivery.",
        "keywords": ["damage", "compensation", "claim", "issue", "problem"]
    },
    {
        "question": "Do you offer carpet and upholstery cleaning?",
        "answer": "Yes! Our Carpet & Upholstery Cleaning service removes deep-set dirt, stains, and odors. We use professional-grade equipment and eco-friendly solutions suitable for all fabric types.",
        "keywords": ["carpet", "upholstery", "sofa", "furniture", "cushion", "stain"]
    },
    {
        "question": "What is the Bag & Shoe Spa service?",
        "answer": "Our Bag & Shoe Spa service professionally cleans, conditions, and restores handbags, shoes, and leather accessories. We handle designer items with care and expertise.",
        "keywords": ["bag", "shoe", "spa", "leather", "cleaning", "restore"]
    },
    {
        "question": "Can you do permanent creasing?",
        "answer": "Yes! Our Permanent Creasing service creates and sets sharp creases on trousers and other garments. The creases last through multiple washes for a crisp, professional look.",
        "keywords": ["creasing", "crease", "trousers", "pants", "permanent"]
    },
    {
        "question": "Do you offer sanitizing services?",
        "answer": "Absolutely! Our Hygienizing & Sanitizing Service kills 99.9% of bacteria and viruses on fabrics. It's perfect for masks, frequent-wear items, and family protection.",
        "keywords": ["sanitizing", "sanitize", "hygienizing", "bacteria", "virus", "sterilize"]
    },
    {
        "question": "What is the Wash & Fold service?",
        "answer": "Our Wash & Fold service handles everyday laundry. We wash, dry, fold, and return your clothes clean and fresh. Perfect for busy individuals and families.",
        "keywords": ["wash", "fold", "laundry", "ironing"]
    },
    {
        "question": "How do I schedule a pickup?",
        "answer": "You can schedule a pickup directly through our app by selecting 'Schedule Pickup,' entering your details, preferred date and time, and service type. We'll confirm within 24 hours.",
        "keywords": ["schedule", "pickup", "booking", "appointment", "order"]
    },
    {
        "question": "How can I track my order?",
        "answer": "Use the 'Track Order' feature in our app. Enter your Order ID or phone number, and you'll see the status of your cleaning. You can also receive SMS updates.",
        "keywords": ["track", "order", "status", "update"]
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept cash, credit cards, debit cards, and digital wallets. Payment can be made online or upon delivery.",
        "keywords": ["payment", "pay", "card", "cash", "method"]
    },
    {
        "question": "Do you have any current offers?",
        "answer": "Check our 'Offers' section in the app for the latest promotions and discounts. We regularly update our offers for new and returning customers.",
        "keywords": ["offer", "discount", "promotion", "deal", "special"]
    },
    {
        "question": "What do you do with delicate items?",
        "answer": "We handle delicate items with specialized care. Each item is inspected, and we use appropriate cleaning methods for silks, wools, lace, and other delicate fabrics.",
        "keywords": ["delicate", "care", "handle", "special", "gentle"]
    },
    {
        "question": "Can you remove stains?",
        "answer": "Our expert staff can treat most stains, including oil, wine, ink, and more. The success depends on the fabric and stain type. Bring items as soon as possible for best results.",
        "keywords": ["stain", "remove", "spot", "mark"]
    },
    {
        "question": "How much does it cost?",
        "answer": "Pricing varies by service type and item. Standard dry cleaning, washing, and specialized services each have different rates. Contact us for a quote or visit our website for pricing.",
        "keywords": ["cost", "price", "rate", "fee", "charge"]
    },
    {
        "question": "Can you handle soft toy cleaning?",
        "answer": "Yes! Our Soft Toy Cleaning service safely cleans stuffed animals and plush toys while preserving their softness and color. Perfect for children's items.",
        "keywords": ["soft", "toy", "stuffed", "animal", "plush"]
    },
    {
        "question": "What is Alteration Clinique?",
        "answer": "Our Alteration Clinique provides professional tailoring and alterations for perfect fit. From hemming to major tailoring, our experts handle all modifications.",
        "keywords": ["alteration", "tailor", "fit", "hem", "adjust"]
    },
    {
        "question": "What is Hanger Amnesty?",
        "answer": "Our Hanger Amnesty program ensures your garments are returned on appropriate, quality hangers. We take care with presentation and protection of your cleaned items.",
        "keywords": ["hanger", "amnesty", "hangers"]
    }
]


def calculate_similarity(query: str, faq_item: dict) -> float:
    """
    Calculate similarity score between query and FAQ item using keyword matching.
    
    Args:
        query: User's question
        faq_item: FAQ dictionary with question, answer, keywords
        
    Returns:
        Similarity score (0-1)
    """
    query_lower = query.lower()
    score = 0.0
    
    # Check against keywords (higher weight)
    keywords = faq_item.get("keywords", [])
    keyword_matches = sum(1 for kw in keywords if kw in query_lower)
    score += keyword_matches * 0.4
    
    # Check against question words
    question_words = faq_item.get("question", "").lower().split()
    question_matches = sum(1 for word in question_words if len(word) > 3 and word in query_lower)
    score += min(question_matches * 0.1, 0.3)
    
    # Normalize score
    score = min(score, 1.0)
    return score


def retrieve_faq_answer(query: str) -> Tuple[str, str, float]:
    """
    Retrieve the best matching FAQ answer for a user query.
    
    Args:
        query: User's question
        
    Returns:
        Tuple of (question, answer, confidence_score)
    """
    if not query or len(query.strip()) < 3:
        return ("", "Please ask a more specific question.", 0.0)
    
    best_match = None
    best_score = 0.0
    
    for faq in FAQ_DATA:
        score = calculate_similarity(query, faq)
        if score > best_score:
            best_score = score
            best_match = faq
    
    # Return match only if confidence is reasonable
    if best_match and best_score > 0.15:
        return (
            best_match["question"],
            best_match["answer"],
            best_score
        )
    
    return ("", "", 0.0)


def get_all_faq() -> List[dict]:
    """Get all FAQ items."""
    return FAQ_DATA


def search_faq(query: str) -> List[dict]:
    """
    Search FAQ for items matching the query.
    
    Args:
        query: Search query
        
    Returns:
        List of matching FAQ items with scores
    """
    results = []
    for faq in FAQ_DATA:
        score = calculate_similarity(query, faq)
        if score > 0.1:
            results.append({
                **faq,
                "score": score
            })
    
    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
