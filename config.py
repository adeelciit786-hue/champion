"""
Configuration for Champion Cleaners Web Application
"""

# Brand Colors - Champion Cleaners Official Colors
BRAND_COLORS = {
    "primary": "#00A651",      # Green
    "primary_light": "#E8F9F3",  # Light Green
    "primary_dark": "#008C3F",   # Dark Green
    "secondary": "#C1272D",    # Red
    "secondary_light": "#FCE8E8",  # Light Red
    "secondary_dark": "#A01F24",   # Dark Red
    "accent": "#FFFFFF",       # White
    "accent_blue": "#007BFF",  # Blue for CTAs
    "light": "#F5F5F5",        # Light Gray
    "light_dark": "#E8E8E8",   # Medium Light Gray
    "white": "#FFFFFF",        # White
    "text_dark": "#333333",    # Dark Gray
    "text_light": "#666666",   # Light Gray
    "success": "#00A651",      # Green
    "warning": "#FFC107",      # Yellow/Gold
    "error": "#C1272D",        # Red
    "info": "#007BFF"          # Blue
}

# Services
SERVICES = [
    "Bag & Shoes Spa",
    "Wedding Gown Cleaning & Preservation",
    "Strollers and Baby Car seat Cleaning and Sanitization",
    "Soft Toy Cleaning & Sanitization",
    "Comprehensive Mattress Cleaning and Sanitization Solution",
    "Super crease",
    "Alterations Clinique"
]

# Coverage Areas
COVERAGE_AREAS = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]

# Database
DB_PATH = "champion_orders.db"

# App Settings
APP_TITLE = "Champion Cleaners Assistant"
APP_SUBTITLE = "Your trusted laundry & dry cleaning service in the UAE"
PHONE = "+971 4 2858581"
TOLL_FREE = "800 4556"
EMAIL = "mail@champion-cleaners.com"
WEBSITE = "https://www.champion-cleaners.com"
COMPANY_DESCRIPTION = "Champion Cleaners was established in the UAE in 1997. The company's aim has always been to provide 5 star premium dry cleaning and laundry services to high-income affluent expat and local populations of Dubai and the United Arab Emirates. Champion Cleaners UAE receives in excess of 1.3 million retail garments annually and has more than 19K Facebook & 10.4K IG followers. Our value added services include Bag & Shoes Spa, Wedding Gown Cleaning & Preservation, Strollers and Baby Car seat Cleaning and Sanitization, Soft Toy Cleaning & Sanitization, Comprehensive Mattress Cleaning and Sanitization Solution, Super crease, and Alterations Clinique. Champion Cleaners is proud to have out-performed its commitments to operating a green business by introduction of a slate of international initiatives."

# FAQ Data
FAQ_DATA = [
    {
        "question": "Do you provide free pickup and delivery?",
        "answer": "Yes! Champion Cleaners provides completely FREE pickup and delivery service to your location in Dubai, Abu Dhabi, and Sharjah. We also offer pay port options for customers to pay via credit or debit cards at their doorstep."
    },
    {
        "question": "What areas do you cover?",
        "answer": "We have an expansive retail network of strategically located outlets in community malls and convenience stops across Dubai, Abu Dhabi, Sharjah, and Ajman. Our team will reach your location for pickup and delivery throughout the UAE."
    },
    {
        "question": "How do I schedule a pickup?",
        "answer": "You can schedule a pickup through our mobile application (Android or iPhone), website, use this chatbot or by calling our Toll-Free number 800-4556. Simply select 'Schedule Pickup', fill in your details, choose your preferred date and time, and confirm. Our team will contact you shortly."
    },
    {
        "question": "What is the turnaround time?",
        "answer": "Standard turnaround time is 2 business days. Express service (next working day) is available with 50% additional cost. Wedding gowns require 4 to 6 days, Bags require 7 to 10 days, and Shoes require 5 to 7 days for proper restoration."
    },
    {
        "question": "What is the Bag & Shoe Spa service?",
        "answer": "Champion Cleaners specializes in cleaning and restoration of high-end designer brands of leather goods and accessories. Our exclusive leather care products are carefully selected and eco-friendly. Services include oil extraction, edge restoration, marker and ink removal, strap repair, stitching, and color restoration. Processing time: 4 to 6 days for shoes and 6 to 8 days for bags."
    },
    {
        "question": "How do you clean and preserve wedding gowns?",
        "answer": "Our specialized Wedding Gown Preservation service uses gentle techniques and premium cleaning solutions. We are members of the Association of Wedding Gown Specialists in USA. We offer two preservation methods: Museum Method (Hanging) or Champion Cleaners Box method. Both provide acid-free environment, dust protection, and best air circulation to keep your gown in pristine condition for generations."
    },
    {
        "question": "Do you offer cleaning for delicate fabrics?",
        "answer": "Yes! We specialize in handling delicate and premium fabrics including silk, wool, cashmere, satin, lace, beadwork, and sequins. We use our state-of-the-art washing and dry cleaning systems with mild chemicals and the best spotting agents in the industry."
    },
    {
        "question": "What is your compensation policy?",
        "answer": "Champion Cleaners takes care of your items seriously. In case of any damage or loss, we provide fair compensation as per our service terms."
    },
    {
        "question": "What green technologies does Champion Cleaners use?",
        "answer": "We are proud to use eco-friendly cleaning technologies including: Green Earth Dry Cleaning Technology (liquid silicone based, odourless and non-toxic), Excello Wet Cleaning Technology (most advanced green soft wash), and I-Genius Technology (chemical-free ozone cabinet for sanitization). All our detergents and products are approved by local authorities as environmentally friendly."
    },
    {
        "question": "What is your Super Crease service?",
        "answer": "Our Super Crease service creates long-lasting, permanent creases on trousers and other garments using professional techniques that last through multiple washes."
    },
    {
        "question": "Do you provide mattress cleaning and sanitization?",
        "answer": "Yes! Our Comprehensive Mattress Cleaning and Sanitization Solution eliminates dust mites and microorganisms. We use state-of-the-art Aqua Jet Injection machines for thorough cleaning that dries quickly without mess."
    },
    {
        "question": "Do you clean and sanitize soft toys?",
        "answer": "Yes! Our Soft Toy Cleaning & Sanitization service carefully cleans and sanitizes all children's soft toys using eco-friendly methods and I-Genius Technology (ozone-safe technology)."
    },
    {
        "question": "Do you clean strollers and baby car seats?",
        "answer": "Yes! Our Strollers and Baby Car Seat Cleaning and Sanitization service ensures safe, thorough cleaning of these essential baby items using our gentle yet effective cleaning methods."
    },
    {
        "question": "What is the Alterations Clinique service?",
        "answer": "Our Alterations Clinique provides professional alteration services for all your garments, handled by expert tailors."
    },
    {
        "question": "How many outlets does Champion Cleaners have?",
        "answer": "Champion Cleaners has strategically located outlets across the UAE in community malls and convenience stops, with an extensive retail network serving all major emirates."
    },
    {
        "question": "How much do you process annually?",
        "answer": "Champion Cleaners UAE receives in excess of 1.3 million retail garments annually, making us one of the largest cleaning operations in the region."
    },
    {
        "question": "What cleaning systems do you use?",
        "answer": "We use fully automatic state-of-the-art washing and dry cleaning systems with automatic dosing units. We have a long-term partnership with Johnson Diversey, the globally number one liquid detergents brand."
    },
    {
        "question": "What payment options are available?",
        "answer": "We offer flexible payment options including credit card payment at your doorstep through our pay port options. You can also pay when scheduling your order."
    },
    {
        "question": "Can I place orders online?",
        "answer": "Yes! Champion Cleaners has Android, iPhone, and Web applications that enable online customer orders at all times. You can also use this chatbot to schedule your pickup."
    },
    {
        "question": "What awards has Champion Cleaners won?",
        "answer": "Champion Cleaners has received prestigious awards including: 2018 UAE Best Operator Award by CINET, Superbrand 2020, and 2020 Global Best Practice Award – Sustainability from CINET."
    },
    {
        "question": "How can I follow Champion Cleaners on social media?",
        "answer": "Follow us on: Facebook: https://www.facebook.com/champions.ae | Twitter: https://twitter.com/championsdubai | Instagram: https://www.instagram.com/championsDubai/"
    },
    {
        "question": "What is your company philosophy?",
        "answer": "Since 1997, Champion Cleaners' aim has been to provide 5-star premium dry cleaning and laundry services to high-income affluent expat and local populations. We are committed to retaining our leadership position in the UAE and penetrating other GCC markets through innovation and sustainability."
    },
    {
        "question": "What fresh and clean home services do you offer?",
        "answer": "We specialize in cleaning carpets, rugs, curtains, sofas, upholstery, and soft furniture. Our innovative cleaning solutions eliminate dust mites and microorganisms using state-of-the-art Aqua Jet Injection machines that allow for convenient surface cleaning with quick drying."
    },
    {
        "question": "Are your products environmentally friendly?",
        "answer": "Yes! All our detergents, additives, and restoration products are carefully selected and approved by local authorities as the most environmentally friendly cleaning options available."
    }
]

# Sample Offers
OFFERS_DATA = [
    {
        "name": "New Customer Welcome",
        "description": "20% off your first order",
        "discount": "20%",
        "valid_until": "2025-12-31",
        "audience": "New customers"
    },
    {
        "name": "Winter Special",
        "description": "Free sanitizing service with any order above AED 50",
        "discount": "Free Service",
        "valid_until": "2025-02-28",
        "audience": "All customers"
    },
    {
        "name": "Loyalty Reward",
        "description": "15% off for customers with 5+ orders",
        "discount": "15%",
        "valid_until": "2025-12-31",
        "audience": "Returning customers"
    }
]

# Social Media Links
SOCIAL_MEDIA = {
    "facebook": "https://www.facebook.com/champions.ae",
    "twitter": "https://twitter.com/championsdubai",
    "instagram": "https://www.instagram.com/championsDubai/"
}

# Company Awards and Achievements
ACHIEVEMENTS = [
    "2018 UAE Best Operator Award by CINET",
    "Superbrand 2020",
    "2020 Global Best Practice Award – Sustainability – From CINET"
]
# Helper Functions
from datetime import datetime, timedelta

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