"""
Home page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, APP_TITLE, APP_SUBTITLE, SERVICES, COMPANY_DESCRIPTION

def show():
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="header-title">CHAMPION CLEANERS</div>
        <div class="header-subtitle">Your Trusted Laundry & Dry Cleaning Service in the UAE</div>
        """, unsafe_allow_html=True)
    
    # Featured Services Section
    st.markdown(f"### 🌟 Our Premium Services")
    
    cols = st.columns(3)
    service_list = [
        ("🎒", "Bag & Shoes Spa", "Designer brand cleaning & restoration"),
        ("👗", "Wedding Gowns", "Premium preservation & cleaning"),
        ("👶", "Baby Items", "Stroller & car seat sanitization"),
        ("🧸", "Soft Toys", "Gentle cleaning & sanitization"),
        ("🛏️", "Mattress Cleaning", "Deep cleaning & sanitization"),
        ("✨", "Super Crease", "Professional crease services")
    ]
    
    for idx, (emoji, title, desc) in enumerate(service_list):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="service-card">
                <div style="font-size: 2rem;">{emoji}</div>
                <h4 style="color: {BRAND_COLORS['primary']}; margin: 10px 0;">{title}</h4>
                <p style="font-size: 0.9rem; color: #666;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Why Choose Us Section
    st.markdown("---")
    st.markdown(f"### ✨ Why Choose Champion Cleaners?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        ✅ **FREE Pickup & Delivery** - Convenient service at your doorstep
        
        ✅ **25+ Years of Excellence** - Serving UAE since 1997
        
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
