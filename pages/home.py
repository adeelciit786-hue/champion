"""
Home page for Champion Cleaners - Matches Flask template exactly
"""

import streamlit as st
from config import BRAND_COLORS

def show():
    # Header
    st.markdown(f"""
    <div class="header">
        <h1>Welcome to Champion Cleaners</h1>
        <p>Your Trusted Laundry & Dry Cleaning Service in the UAE</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick action cards
    st.markdown("### Quick Access")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid {BRAND_COLORS['primary']}; border-left: 4px solid {BRAND_COLORS['secondary']};">
            <h2 style="font-size: 2rem; margin: 0;">📅</h2>
            <h3 style="color: {BRAND_COLORS['primary']};">Schedule Pickup</h3>
            <p style="color: #666;">Book a convenient pickup time for your laundry</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid {BRAND_COLORS['primary']}; border-left: 4px solid {BRAND_COLORS['secondary']};">
            <h2 style="font-size: 2rem; margin: 0;">📍</h2>
            <h3 style="color: {BRAND_COLORS['primary']};">Track Order</h3>
            <p style="color: #666;">Check the status of your order</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid {BRAND_COLORS['primary']}; border-left: 4px solid {BRAND_COLORS['secondary']};">
            <h2 style="font-size: 2rem; margin: 0;">❓</h2>
            <h3 style="color: {BRAND_COLORS['primary']};">FAQs</h3>
            <p style="color: #666;">Find answers to common questions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid {BRAND_COLORS['primary']}; border-left: 4px solid {BRAND_COLORS['secondary']};">
            <h2 style="font-size: 2rem; margin: 0;">🎉</h2>
            <h3 style="color: {BRAND_COLORS['primary']};">Offers & Promotions</h3>
            <p style="color: #666;">Check out our latest deals</p>
        </div>
        """, unsafe_allow_html=True)
    
    # About section
    st.markdown("---")
    st.markdown(f"""
    ### About Champion Cleaners
    
    Champion Cleaners was established in the UAE in 1997. The company's aim has always been to provide 5 star premium dry cleaning and laundry services to high-income affluent expat and local populations of Dubai and the United Arab Emirates. Champion Cleaners UAE receives in excess of 1.3 million retail garments annually and has more than 19K Facebook & 10.4K IG followers.
    
    #### Our Value Added Services:
    - 👜 Bag & Shoes Spa
    - 👗 Wedding Gown Cleaning & Preservation
    - 👶 Strollers and Baby Car seat Cleaning and Sanitization
    - 🧸 Soft Toy Cleaning & Sanitization
    - 🛏️ Comprehensive Mattress Cleaning and Sanitization Solution
    - 👔 Super Crease
    - ✂️ Alterations Clinique
    
    Champion Cleaners is proud to have out-performed its commitments to operating a green business by introduction of a slate of international initiatives.
    """)
    
    # Contact info
    st.markdown("---")
    st.markdown("### Contact Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem;">📞 Phone</h3>
            <p><strong>+971 4 2858581</strong><br><strong>Toll-Free:</strong> 800 4556</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem;">📧 Email</h3>
            <p>mail@champion-cleaners.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem;">🌐 Website</h3>
            <p>champion-cleaners.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Services Section
    st.markdown("---")
    st.markdown("### Our Premium Services")
    
    col1, col2, col3 = st.columns(3)
    
    services = [
        ("📦", "Free Pick-up & Delivery", "Door-to-door convenience"),
        ("🛋️", "Carpet & Upholstery", "Advanced technology cleaning"),
        ("👜", "Bag & Shoe Spa", "Luxury leather restoration"),
        ("👗", "Wedding Gown", "Premium preservation"),
        ("👔", "Super Crease", "Long-lasting freshness"),
        ("🧸", "Soft Toy Cleaning", "Safe & sanitized")
    ]
    
    cols = [col1, col2, col3]
    for idx, (emoji, title, desc) in enumerate(services):
        with cols[idx % 3]:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 4px solid {BRAND_COLORS['primary']}; cursor: pointer; transition: transform 0.3s;">
                <div style="font-size: 2.5rem;">{emoji}</div>
                <h4 style="color: {BRAND_COLORS['primary']}; margin: 0.5rem 0;">{title}</h4>
                <p style="color: #666; font-size: 0.9rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
        
        ✅ **1.3M+ Garments Annually** - Trusted by thousands
        
        ✅ **Eco-Friendly Solutions** - Green cleaning technology
        """)
    
    with col2:
        st.markdown(f"""
        ✅ **Premium Quality** - 5-star service standards
        
        ✅ **Multiple Coverage Areas** - Dubai, Abu Dhabi, Sharjah, Ajman
        
        ✅ **Competitive Pricing** - Best value in the market
        
        ✅ **Professional Team** - Trained & experienced experts
        """)
    
    # About Company
    st.markdown("---")
    st.markdown(f"### 🏢 About Champion Cleaners")
    st.info(COMPANY_DESCRIPTION)
    
    # Quick Stats
    st.markdown("---")
    st.markdown(f"### 📊 By The Numbers")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Years in Business", "25+")
    with col2:
        st.metric("Garments/Year", "1.3M+")
    with col3:
        st.metric("Locations", "50+")
    with col4:
        st.metric("Happy Customers", "19K+")
    
    # Call to Action
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 Schedule Your First Pickup Now", use_container_width=True):
            st.switch_page("pages/schedule.py")
    
    # Contact Info
    st.markdown("---")
    st.markdown(f"### 📞 Contact Us")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **Phone**
        
        📱 +971 4 2858581
        
        📞 Toll-Free: 800 4556
        """)
    
    with col2:
        st.markdown(f"""
        **Email**
        
        ✉️ mail@champion-cleaners.com
        
        🌐 www.champion-cleaners.com
        """)
    
    with col3:
        st.markdown(f"""
        **Coverage Areas**
        
        📍 Dubai
        📍 Abu Dhabi
        📍 Sharjah
        📍 Ajman
        """)
