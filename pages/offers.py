"""
Offers page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, OFFERS_DATA

def show():
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['secondary']}, {BRAND_COLORS['primary']});
                color: white; padding: 2rem; border-radius: 12px; text-align: center;">
        <h1 style="color: white; border: none; margin-top: 0;">🎁 Special Offers & Promotions</h1>
        <p style="opacity: 0.95; margin: 0;">Check out our latest deals and exclusive offers for you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Display all offers
    cols = st.columns(2)
    
    for idx, offer in enumerate(OFFERS_DATA):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, white, {BRAND_COLORS['primary_light']});
                       padding: 1.8rem; border-radius: 12px; 
                       border-top: 4px solid {BRAND_COLORS['secondary']};
                       box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                       transition: all 0.3s;">
                <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 0; margin-bottom: 0.5rem;">
                    ✨ {offer['name']}
                </h4>
                <p style="color: {BRAND_COLORS['text_light']}; margin: 1rem 0; line-height: 1.6;">
                    {offer['description']}
                </p>
                <div style="background: linear-gradient(135deg, {BRAND_COLORS['secondary']}, #D63945); 
                           color: white; padding: 1rem; border-radius: 8px; text-align: center;
                           margin: 1rem 0;">
                    <h3 style="margin: 0; color: white; font-size: 1.8rem;">{offer['discount']}</h3>
                    <p style="margin: 0.3rem 0; font-size: 0.9rem; opacity: 0.95;">Discount</p>
                </div>
                <p style="text-align: center; color: {BRAND_COLORS['text_light']}; font-size: 0.85rem; margin: 1rem 0 0 0;">
                    ⏰ Valid until: <strong style="color: {BRAND_COLORS['text_dark']};">{offer['valid_until']}</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # How to claim offers
    st.markdown("---")
    st.markdown(f"### 📋 How to Claim These Offers")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    steps = [
        ("1️⃣", "Schedule Pickup", "Click on 'Schedule Pickup' and book your service"),
        ("2️⃣", "Mention Code", "Tell our team about the offer code during confirmation"),
        ("3️⃣", "Enjoy Discount", "Receive your discount on the final bill")
    ]
    
    for idx, (num, title, desc) in enumerate(steps):
        with [col1, col2, col3][idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                        padding: 1.5rem; border-radius: 12px;
                        border-left: 5px solid {BRAND_COLORS['primary']};
                        text-align: center;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{num}</div>
                <h4 style="color: {BRAND_COLORS['primary']}; margin: 0.5rem 0;">{title}</h4>
                <p style="color: {BRAND_COLORS['text_light']}; margin: 0; font-size: 0.9rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Terms and conditions
    st.markdown("---")
    with st.expander("📄 Terms & Conditions"):
        st.markdown(f"""
        ✓ Offers are valid for the mentioned period only
        
        ✓ Cannot be combined with other promotions
        
        ✓ Applicable for new and existing customers
        
        ✓ Valid in all coverage areas (Dubai, Abu Dhabi, Sharjah, Ajman)
        
        ✓ Minimum order value may apply (check individual offer)
        
        ✓ Offer code must be mentioned at the time of scheduling
        
        ✓ Champion Cleaners reserves the right to modify or withdraw offers
        
        ✓ Not applicable on previously booked orders
        
        **For more details, contact:**
        - 📞 +971 4 2858581
        - 📞 Toll-Free: 800 4556
        - 📧 mail@champion-cleaners.com
        """)
    
    # Subscribe to offers
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                padding: 2rem; border-radius: 12px;
                border-left: 5px solid {BRAND_COLORS['primary']};
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
        <h2 style="color: {BRAND_COLORS['primary']}; border: none; margin-top: 0;">📧 Never Miss an Offer</h2>
        <p style="color: {BRAND_COLORS['text_light']}; margin-bottom: 1.5rem;">Subscribe to our newsletter for exclusive deals and updates!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("", placeholder="your@email.com", label_visibility="collapsed")
    with col2:
        if st.button("✉️ Subscribe", use_container_width=True):
            if email and "@" in email:
                st.success("✅ Thank you! You'll receive updates soon!")
            else:
                st.error("Please enter a valid email")
    
    # Call to action
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
                color: white; padding: 3rem 2rem; border-radius: 15px;
                text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
        <h2 style="color: white; border: none; margin-top: 0;">⚡ Don't Miss Out!</h2>
        <p style="opacity: 0.95; font-size: 1.05rem;">Grab these amazing offers today and save on your next service</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 Schedule Now to Claim Offer", use_container_width=True):
            st.session_state.page = 'schedule'
            st.rerun()
