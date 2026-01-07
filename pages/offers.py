"""
Offers page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, OFFERS_DATA

def show():
    st.markdown(f"### 🎁 Special Offers & Promotions")
    st.markdown("Check out our latest deals and exclusive offers for you!")
    
    st.markdown("---")
    
    # Display all offers
    cols = st.columns(2)
    
    for idx, offer in enumerate(OFFERS_DATA):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #FFFFFF, #F0F9FF); 
                       padding: 20px; border-radius: 10px; 
                       border-top: 3px solid {BRAND_COLORS['secondary']};
                       box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 0;">
                    {offer['name']}
                </h4>
                <p style="color: #666; margin: 10px 0;">
                    {offer['description']}
                </p>
                <div style="background: {BRAND_COLORS['secondary']}; 
                           color: white; padding: 10px; border-radius: 5px; text-align: center;">
                    <h3 style="margin: 0; color: white;">{offer['discount']}</h3>
                </div>
                <p style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 10px;">
                    Valid until: {offer['valid_until']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # How to claim offers
    st.markdown("---")
    st.markdown(f"### 📋 How to Claim These Offers")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **Step 1: Schedule**
        
        Click on "Schedule Pickup" 
        and book your service
        """)
    
    with col2:
        st.markdown(f"""
        **Step 2: Mention Code**
        
        Tell our team about 
        the offer code during confirmation
        """)
    
    with col3:
        st.markdown(f"""
        **Step 3: Enjoy Discount**
        
        Receive your discount 
        on the final bill
        """)
    
    # Terms and conditions
    st.markdown("---")
    with st.expander("📄 Terms & Conditions"):
        st.markdown("""
        - Offers are valid for the mentioned period only
        - Cannot be combined with other promotions
        - Applicable for new and existing customers
        - Valid in all coverage areas (Dubai, Abu Dhabi, Sharjah, Ajman)
        - Minimum order value may apply (check individual offer)
        - Offer code must be mentioned at the time of scheduling
        - Champion Cleaners reserves the right to modify or withdraw offers
        - Not applicable on previously booked orders
        
        For more details, contact:
        - 📞 +971 4 2858581
        - 📞 Toll-Free: 800 4556
        - 📧 mail@champion-cleaners.com
        """)
    
    # Subscribe to offers
    st.markdown("---")
    st.markdown(f"### 📧 Never Miss an Offer")
    st.markdown("Subscribe to our newsletter for exclusive deals and updates!")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Enter your email", placeholder="your@email.com")
    with col2:
        if st.button("✉️ Subscribe", use_container_width=True):
            if email and "@" in email:
                st.success("✅ Thank you! You'll receive updates soon!")
            else:
                st.error("Please enter a valid email")
    
    # Call to action
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 Grab These Offers Now", use_container_width=True):
            st.switch_page("pages/schedule.py")
