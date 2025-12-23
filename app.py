"""
Champion Cleaners Assistant - Main Streamlit Application
A professional chatbot for scheduling pickups, tracking orders, accessing FAQs, and viewing offers.
"""

import streamlit as st
from datetime import datetime
from typing import Optional
import sys
import os

# Import custom modules
from config import BRAND_COLORS, SERVICES, COVERAGE_AREAS, APP_TITLE, APP_SUBTITLE, WEBSITE, EMAIL, PHONE
from backend import (
    save_order, get_order, log_notification, 
    get_active_offers, get_all_orders, get_notifications
)
from faq_data import retrieve_faq_answer, search_faq
from utils import (
    validate_phone_number, validate_email, validate_pickup_date,
    validate_pickup_time, validate_full_name, validate_address,
    format_phone_for_display, get_future_dates, get_time_slots,
    get_greeting_message, truncate_text
)


# ========================
# Page Configuration
# ========================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ========================
# Custom CSS Styling
# ========================

def apply_custom_styling():
    """Apply Champion Cleaners brand styling."""
    st.markdown(f"""
    <style>
    /* Main color scheme */
    :root {{
        --primary-color: {BRAND_COLORS['primary']};
        --secondary-color: {BRAND_COLORS['secondary']};
        --accent-color: {BRAND_COLORS['accent']};
        --text-dark: {BRAND_COLORS['text_dark']};
        --success-color: {BRAND_COLORS['success']};
        --warning-color: {BRAND_COLORS['warning']};
        --error-color: {BRAND_COLORS['error']};
    }}
    
    /* Header styling */
    .main-header {{
        background: linear-gradient(135deg, {BRAND_COLORS['primary']} 0%, {BRAND_COLORS['primary']}dd 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    
    .main-header h1 {{
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }}
    
    .main-header p {{
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }}
    
    /* Button styling */
    .stButton > button {{
        background-color: {BRAND_COLORS['primary']};
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }}
    
    .stButton > button:hover {{
        background-color: {BRAND_COLORS['secondary']};
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    
    /* Success message */
    .success-box {{
        background-color: {BRAND_COLORS['success']};
        color: white;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }}
    
    /* Info message */
    .info-box {{
        background-color: #3498db;
        color: white;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }}
    
    /* Warning message */
    .warning-box {{
        background-color: {BRAND_COLORS['warning']};
        color: white;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }}
    
    /* Error message */
    .error-box {{
        background-color: {BRAND_COLORS['error']};
        color: white;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }}
    
    /* Form styling */
    .form-section {{
        background-color: {BRAND_COLORS['light']};
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 4px solid {BRAND_COLORS['primary']};
    }}
    
    /* Sidebar styling */
    .sidebar .sidebar-content {{
        background-color: #f8f9fa;
    }}
    
    /* Card styling */
    .card {{
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}
    
    /* Offer card */
    .offer-card {{
        background: linear-gradient(135deg, {BRAND_COLORS['accent']}15 0%, {BRAND_COLORS['secondary']}15 100%);
        border-left: 4px solid {BRAND_COLORS['accent']};
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
    }}
    
    /* Text styling */
    h1, h2, h3 {{
        color: {BRAND_COLORS['primary']};
    }}
    
    .text-secondary {{
        color: {BRAND_COLORS['secondary']};
    }}
    
    .text-muted {{
        color: #7f8c8d;
    }}
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {{
        border: 2px solid {BRAND_COLORS['light']};
        border-radius: 6px;
    }}
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: {BRAND_COLORS['primary']};
    }}
    
    /* Divider */
    .divider {{
        border-bottom: 2px solid {BRAND_COLORS['light']};
        margin: 1.5rem 0;
    }}
    </style>
    """, unsafe_allow_html=True)


# ========================
# Initialization
# ========================

apply_custom_styling()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "customer_info" not in st.session_state:
    st.session_state.customer_info = {}


# ========================
# UI Components
# ========================

def render_header():
    """Render application header."""
    st.markdown(f"""
    <div class="main-header">
        <h1>🧹 {APP_TITLE}</h1>
        <p>{APP_SUBTITLE}</p>
    </div>
    """, unsafe_allow_html=True)


def render_success_message(message: str):
    """Render success message."""
    st.markdown(f'<div class="success-box">✓ {message}</div>', unsafe_allow_html=True)


def render_info_message(message: str):
    """Render info message."""
    st.markdown(f'<div class="info-box">ℹ {message}</div>', unsafe_allow_html=True)


def render_warning_message(message: str):
    """Render warning message."""
    st.markdown(f'<div class="warning-box">⚠ {message}</div>', unsafe_allow_html=True)


def render_error_message(message: str):
    """Render error message."""
    st.markdown(f'<div class="error-box">✗ {message}</div>', unsafe_allow_html=True)


def render_offer_card(offer: dict):
    """Render an offer card."""
    discount_text = ""
    if offer.get("discount_percent"):
        discount_text = f"<strong>{offer['discount_percent']:.0f}% OFF</strong>"
    elif offer.get("discount_amount"):
        discount_text = f"<strong>AED {offer['discount_amount']:.0f} OFF</strong>"
    
    valid_to = offer.get("valid_to", "N/A")
    
    return f"""
    <div class="offer-card">
        <div style="font-weight: 600; color: {BRAND_COLORS['secondary']}; margin-bottom: 0.5rem;">
            {discount_text} - {offer.get('offer_name', 'Special Offer')}
        </div>
        <div style="font-size: 0.9rem; color: #555; margin-bottom: 0.3rem;">
            {offer.get('description', '')}
        </div>
        <div style="font-size: 0.85rem; color: #999;">
            Valid until {valid_to}
        </div>
    </div>
    """


# ========================
# Feature: Schedule Pickup
# ========================

def page_schedule_pickup():
    """Schedule pickup page."""
    st.markdown("## 📅 Schedule Pickup & Delivery")
    st.markdown("---")
    
    # Check for applicable offers
    applicable_offers = get_active_offers("all")
    if applicable_offers:
        st.markdown("### 🎉 Available Offers")
        for offer in applicable_offers[:3]:  # Show top 3 offers
            st.markdown(render_offer_card(offer), unsafe_allow_html=True)
        st.markdown("---")
    
    # Form
    st.markdown("### Your Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        full_name = st.text_input(
            "Full Name *",
            placeholder="Enter your full name",
            key="pickup_name"
        )
    
    with col2:
        phone = st.text_input(
            "Phone Number *",
            placeholder="+971 50 123 4567",
            key="pickup_phone"
        )
    
    email = st.text_input(
        "Email Address (Optional)",
        placeholder="your.email@example.com",
        key="pickup_email"
    )
    
    pickup_address = st.text_area(
        "Pickup Address *",
        placeholder="Enter your full address including building, villa number, etc.",
        height=80,
        key="pickup_address"
    )
    
    st.markdown("### Pickup Schedule")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pickup_date = st.selectbox(
            "Preferred Pickup Date *",
            options=get_future_dates(30),
            format_func=lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%A, %d %B %Y"),
            key="pickup_date"
        )
    
    with col2:
        pickup_time = st.selectbox(
            "Preferred Pickup Time *",
            options=get_time_slots(30),
            key="pickup_time"
        )
    
    st.markdown("### Service Selection")
    
    service_type = st.selectbox(
        "Service Type *",
        options=SERVICES,
        key="pickup_service"
    )
    
    notes = st.text_area(
        "Special Instructions (Optional)",
        placeholder="Any special requests or notes about your items?",
        height=60,
        key="pickup_notes"
    )
    
    # Validation and submission
    st.markdown("---")
    
    if st.button("📤 Confirm & Schedule Pickup", use_container_width=True):
        # Validate inputs
        errors = []
        
        if not full_name:
            errors.append("Full name is required")
        else:
            valid, msg = validate_full_name(full_name)
            if not valid:
                errors.append(msg)
        
        if not phone:
            errors.append("Phone number is required")
        else:
            valid, msg = validate_phone_number(phone)
            if not valid:
                errors.append(msg)
        
        if email:
            valid, msg = validate_email(email)
            if not valid:
                errors.append(msg)
        
        if not pickup_address:
            errors.append("Pickup address is required")
        else:
            valid, msg = validate_address(pickup_address)
            if not valid:
                errors.append(msg)
        
        if not pickup_date:
            errors.append("Pickup date is required")
        else:
            valid, msg = validate_pickup_date(pickup_date)
            if not valid:
                errors.append(msg)
        
        if not pickup_time:
            errors.append("Pickup time is required")
        else:
            valid, msg = validate_pickup_time(pickup_time)
            if not valid:
                errors.append(msg)
        
        # Show validation errors
        if errors:
            for error in errors:
                render_error_message(error)
        else:
            # Save order
            success, result = save_order(
                full_name=full_name,
                phone_number=phone,
                email=email if email else None,
                pickup_address=pickup_address,
                pickup_date=pickup_date,
                pickup_time=pickup_time,
                service_type=service_type,
                notes=notes if notes else None
            )
            
            if success:
                order_id = result
                # Log notification for team
                log_notification(
                    order_id=order_id,
                    phone_number=phone,
                    query_type="new_pickup_scheduled",
                    message=f"New pickup order scheduled: {service_type} on {pickup_date} at {pickup_time}"
                )
                
                # Show confirmation
                render_success_message("Thank you! Your pickup order has been scheduled.")
                st.markdown(f"""
                <div class="card">
                    <h4>Order Confirmation</h4>
                    <table style="width: 100%; font-size: 0.95rem;">
                        <tr><td style="font-weight: 600;">Order ID:</td><td style="text-align: right; color: {BRAND_COLORS['secondary']};">{order_id}</td></tr>
                        <tr><td style="font-weight: 600;">Name:</td><td style="text-align: right;">{full_name}</td></tr>
                        <tr><td style="font-weight: 600;">Phone:</td><td style="text-align: right;">{format_phone_for_display(phone)}</td></tr>
                        <tr><td style="font-weight: 600;">Service:</td><td style="text-align: right;">{service_type}</td></tr>
                        <tr><td style="font-weight: 600;">Pickup Date:</td><td style="text-align: right;">{datetime.strptime(pickup_date, '%Y-%m-%d').strftime('%d %b %Y')}</td></tr>
                        <tr><td style="font-weight: 600;">Pickup Time:</td><td style="text-align: right;">{pickup_time}</td></tr>
                    </table>
                </div>
                """, unsafe_allow_html=True)
                
                render_info_message("Our team will contact you shortly to confirm the pickup. Please save your Order ID for reference.")
                
                st.markdown("---")
                st.markdown(f"**Questions?** Contact us at {EMAIL} or {PHONE}")
            else:
                render_error_message(f"Could not save order: {result}")


# ========================
# Feature: Track Order
# ========================

def page_track_order():
    """Track order page."""
    st.markdown("## 📍 Track Your Order")
    st.markdown("---")
    
    st.markdown("### How would you like to search?")
    
    search_method = st.radio(
        "Search by:",
        options=["Order ID", "Phone Number"],
        horizontal=True
    )
    
    if search_method == "Order ID":
        order_id = st.text_input(
            "Enter your Order ID *",
            placeholder="e.g., CC20250101ABCD1234",
            key="track_order_id"
        )
        
        if st.button("🔍 Search Order", use_container_width=True):
            if not order_id:
                render_error_message("Please enter an Order ID")
            else:
                order = get_order(order_id=order_id)
                
                if order:
                    render_success_message("Order Found!")
                    st.markdown(f"""
                    <div class="card">
                        <h4>Order Details</h4>
                        <table style="width: 100%; font-size: 0.95rem;">
                            <tr><td style="font-weight: 600;">Order ID:</td><td style="text-align: right; color: {BRAND_COLORS['secondary']};">{order['order_id']}</td></tr>
                            <tr><td style="font-weight: 600;">Name:</td><td style="text-align: right;">{order['full_name']}</td></tr>
                            <tr><td style="font-weight: 600;">Service:</td><td style="text-align: right;">{order['service_type']}</td></tr>
                            <tr><td style="font-weight: 600;">Pickup Date:</td><td style="text-align: right;">{order['pickup_date']}</td></tr>
                            <tr><td style="font-weight: 600;">Status:</td><td style="text-align: right; color: {BRAND_COLORS['success']}; font-weight: 600;">{order['status']}</td></tr>
                        </table>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    render_info_message("We have your order! Our team will contact you shortly with an update.")
                else:
                    render_warning_message("Order not found with that ID.")
                    # Log notification
                    log_notification(
                        order_id=None,
                        phone_number="unknown",
                        query_type="order_not_found",
                        message=f"Customer searched for non-existent order ID: {order_id}"
                    )
                    render_info_message("Our team will reach out to you shortly to help locate your order.")
    
    else:  # Phone Number search
        phone = st.text_input(
            "Enter your Phone Number *",
            placeholder="+971 50 123 4567",
            key="track_phone"
        )
        
        if st.button("🔍 Search Order", use_container_width=True):
            if not phone:
                render_error_message("Please enter a phone number")
            else:
                valid, msg = validate_phone_number(phone)
                if not valid:
                    render_error_message(msg)
                else:
                    order = get_order(phone_number=phone)
                    
                    if order:
                        render_success_message("Order Found!")
                        st.markdown(f"""
                        <div class="card">
                            <h4>Your Latest Order</h4>
                            <table style="width: 100%; font-size: 0.95rem;">
                                <tr><td style="font-weight: 600;">Order ID:</td><td style="text-align: right; color: {BRAND_COLORS['secondary']};">{order['order_id']}</td></tr>
                                <tr><td style="font-weight: 600;">Service:</td><td style="text-align: right;">{order['service_type']}</td></tr>
                                <tr><td style="font-weight: 600;">Pickup Date:</td><td style="text-align: right;">{order['pickup_date']}</td></tr>
                                <tr><td style="font-weight: 600;">Status:</td><td style="text-align: right; color: {BRAND_COLORS['success']}; font-weight: 600;">{order['status']}</td></tr>
                            </table>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        render_info_message("We have your order! Our team will contact you shortly with an update.")
                    else:
                        render_warning_message("No orders found for this phone number.")
                        # Log notification
                        log_notification(
                            order_id=None,
                            phone_number=phone,
                            query_type="order_not_found",
                            message=f"Customer searched for order with phone: {format_phone_for_display(phone)}"
                        )
                        render_info_message("Our team will reach out to you shortly to help. Don't worry!")


# ========================
# Feature: FAQ
# ========================

def page_faq():
    """FAQ page."""
    st.markdown("## ❓ Frequently Asked Questions")
    st.markdown("---")
    
    st.markdown("### Ask a Question")
    
    user_question = st.text_input(
        "What would you like to know?",
        placeholder="Type your question here...",
        key="faq_input"
    )
    
    if st.button("🔍 Find Answer", use_container_width=True) or user_question:
        if user_question and len(user_question.strip()) >= 3:
            # Retrieve FAQ answer
            q, answer, confidence = retrieve_faq_answer(user_question)
            
            if confidence > 0.15 and answer:
                render_success_message("Found a relevant answer!")
                st.markdown(f"""
                <div class="card">
                    <h4 style="color: {BRAND_COLORS['primary']};">Q: {q}</h4>
                    <p style="font-size: 1rem; line-height: 1.6;">{answer}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown("### Related Questions")
                
                # Show related FAQs
                related = search_faq(user_question)
                if related:
                    for i, faq in enumerate(related[1:4], 1):  # Show next 3 most relevant
                        with st.expander(f"{i}. {truncate_text(faq['question'], 60)}"):
                            st.write(faq['answer'])
            else:
                render_warning_message("I couldn't find an exact match for your question.")
                render_info_message("Suggested: Please try asking with different keywords, or our team will get back to you shortly with help.")
                
                # Log for team follow-up
                log_notification(
                    order_id=None,
                    phone_number="unknown",
                    query_type="faq_unanswered",
                    message=f"Customer asked unanswered question: {user_question}"
                )
                
                st.markdown("---")
                st.markdown("### Popular Questions")
                
                # Show all FAQs
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**General Information**")
                    faq_list = [
                        "Do you provide free pickup and delivery?",
                        "What areas do you cover?",
                        "How do I schedule a pickup?"
                    ]
                    for q in faq_list:
                        answer, _, _ = retrieve_faq_answer(q)
                        if answer:
                            with st.expander(q):
                                a, _, _ = retrieve_faq_answer(q)
                                st.write(a)
                
                with col2:
                    st.markdown("**Services**")
                    faq_list = [
                        "What is the Bag & Shoe Spa service?",
                        "Do you offer carpet and upholstery cleaning?",
                        "How do you clean delicate fabrics?"
                    ]
                    for q in faq_list:
                        if retrieve_faq_answer(q)[0]:
                            with st.expander(q):
                                a, _, _ = retrieve_faq_answer(q)
                                st.write(a)


# ========================
# Feature: Offers
# ========================

def page_offers():
    """Offers page."""
    st.markdown("## 🎉 Current Offers & Promotions")
    st.markdown("---")
    
    # Get active offers
    all_offers = get_active_offers()
    
    if all_offers:
        st.markdown(f"### Active Offers ({len(all_offers)})")
        
        for offer in all_offers:
            st.markdown(render_offer_card(offer), unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### How to Claim")
        st.markdown("""
        1. **Schedule your pickup** - Click "Schedule Pickup" in the menu
        2. **Valid offers apply automatically** - Eligible discounts will be applied to your order
        3. **Confirmation** - You'll see the offer details in your order confirmation
        
        *Offers are subject to terms and conditions. Not combinable with other promotions.*
        """)
    else:
        render_warning_message("No current offers available at the moment.")
        render_info_message("Check back soon for special promotions! Sign up for notifications on our website.")
    
    st.markdown("---")
    
    # Subscription section
    st.markdown("### 📧 Get Notified About Offers")
    
    email = st.text_input(
        "Enter your email to receive updates about new offers",
        placeholder="your.email@example.com",
        key="offer_notification_email"
    )
    
    if st.button("✉️ Subscribe to Offers", use_container_width=True):
        if not email:
            render_error_message("Please enter your email address")
        else:
            valid, msg = validate_email(email)
            if not valid:
                render_error_message(msg)
            else:
                # In production: subscribe to email list
                render_success_message("Thank you! You'll receive notifications about our latest offers.")
                log_notification(
                    order_id=None,
                    phone_number="unknown",
                    query_type="offer_subscription",
                    message=f"Customer subscribed to offers: {email}"
                )


# ========================
# Home / Main Menu
# ========================

def page_home():
    """Home page with main menu."""
    render_header()
    
    st.markdown(f"### {get_greeting_message()}")
    
    st.markdown("""
    Welcome to Champion Cleaners Assistant! We're here to help you schedule pickups, 
    track your orders, answer questions, and share our latest offers.
    
    Choose what you'd like to do below:
    """)
    
    st.markdown("---")
    
    # Main menu buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📅 Schedule Pickup", use_container_width=True, key="btn_schedule"):
            st.session_state.page = "schedule"
            st.rerun()
        
        if st.button("📍 Track Order", use_container_width=True, key="btn_track"):
            st.session_state.page = "track"
            st.rerun()
    
    with col2:
        if st.button("❓ FAQs & Information", use_container_width=True, key="btn_faq"):
            st.session_state.page = "faq"
            st.rerun()
        
        if st.button("🎉 Current Offers", use_container_width=True, key="btn_offers"):
            st.session_state.page = "offers"
            st.rerun()
    
    st.markdown("---")
    
    # Quick contact info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **📞 Phone**  
        {PHONE}
        """)
    
    with col2:
        st.markdown(f"""
        **📧 Email**  
        {EMAIL}
        """)
    
    with col3:
        st.markdown(f"""
        **🌐 Website**  
        [champion-cleaners.com]({WEBSITE})
        """)
    
    st.markdown("---")
    
    # Company info
    st.markdown("""
    ### About Champion Cleaners
    
    Champion Cleaners is your trusted laundry & dry cleaning service in the UAE. 
    With over 20 years of experience, we provide professional cleaning services across Dubai, Abu Dhabi, and other emirates.
    
    **Why Choose Us?**
    - ✓ Free Pickup & Delivery
    - ✓ Expert Handling of Delicate Items
    - ✓ Quick Turnaround Times
    - ✓ Professional Service with Care
    - ✓ Eco-Friendly Solutions
    """)


# ========================
# Sidebar Navigation
# ========================

with st.sidebar:
    st.markdown(f"## 🧹 {APP_TITLE}")
    st.markdown("---")
    
    # Navigation menu
    st.markdown("### Navigation")
    
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.session_state.page = "home"
        st.rerun()
    
    if st.button("📅 Schedule Pickup", use_container_width=True, key="nav_schedule"):
        st.session_state.page = "schedule"
        st.rerun()
    
    if st.button("📍 Track Order", use_container_width=True, key="nav_track"):
        st.session_state.page = "track"
        st.rerun()
    
    if st.button("❓ FAQs", use_container_width=True, key="nav_faq"):
        st.session_state.page = "faq"
        st.rerun()
    
    if st.button("🎉 Offers", use_container_width=True, key="nav_offers"):
        st.session_state.page = "offers"
        st.rerun()
    
    st.markdown("---")
    st.markdown("### Quick Contact")
    st.markdown(f"""
    **Phone:** {PHONE}  
    **Email:** {EMAIL}  
    
    **Working Hours**  
    Saturday - Thursday: 8 AM - 8 PM  
    Friday: 10 AM - 8 PM
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.85rem; color: #7f8c8d; text-align: center;">
    Champion Cleaners © 2025  
    Your Trusted Laundry Partner
    </div>
    """, unsafe_allow_html=True)


# ========================
# Main Application Flow
# ========================

def main():
    """Main application flow."""
    # Route to correct page
    if st.session_state.page == "home":
        page_home()
    elif st.session_state.page == "schedule":
        page_schedule_pickup()
    elif st.session_state.page == "track":
        page_track_order()
    elif st.session_state.page == "faq":
        page_faq()
    elif st.session_state.page == "offers":
        page_offers()
    else:
        st.session_state.page = "home"
        st.rerun()


if __name__ == "__main__":
    main()
