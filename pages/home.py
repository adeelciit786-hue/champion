"""
Home page for Champion Cleaners - Matches Flask template exactly
"""

import streamlit as st
from config import BRAND_COLORS

def show():
    # Header
    st.markdown(f"""
    <div class="header">
        <h1>🏢 Welcome to Champion Cleaners</h1>
        <p>Your Trusted Laundry & Dry Cleaning Service in the UAE</p>
        <p style="font-size: 0.95rem; margin-top: 1rem; opacity: 0.9;">Established 1997 | Premium Quality | 20+ Years of Excellence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick access cards - clickable with professional styling
    st.markdown(f"### 🚀 Quick Access")
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    
    quick_actions = [
        ("📅 Schedule Pickup", "Book a convenient\npickup time", "quick_schedule"),
        ("📍 Track Order", "Check your\norder status", "quick_track"),
        ("❓ FAQs", "Find answers to\ncommon questions", "quick_faq"),
        ("🎁 Special Offers", "View our latest\ndeals", "quick_offers")
    ]
    
    for idx, (title, desc, key) in enumerate(quick_actions):
        with [col1, col2, col3, col4][idx]:
            # Determine where to navigate
            nav_page = ""
            if key == "quick_schedule":
                nav_page = "schedule"
            elif key == "quick_track":
                nav_page = "track"
            elif key == "quick_faq":
                nav_page = "faq"
            elif key == "quick_offers":
                nav_page = "offers"
            
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {BRAND_COLORS['primary_light']} 0%, white 100%);
                        padding: 1.5rem; border-radius: 12px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                        border: 3px solid {BRAND_COLORS['primary']};
                        border-top: 4px solid {BRAND_COLORS['primary']};
                        border-bottom: 4px solid {BRAND_COLORS['primary']};
                        transition: all 0.3s;
                        min-height: 155px;
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        align-items: stretch;
                        margin-bottom: 0.5rem;">
                <div style="text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="color: {BRAND_COLORS['primary']}; margin: 0 0 0.5rem 0; font-size: 1.1rem;">{title}</h4>
                    <p style="color: {BRAND_COLORS['text_light']}; font-size: 0.85rem; margin: 0; line-height: 1.4;">{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Learn More →", key=key, use_container_width=True):
                st.session_state.page = nav_page
                st.rerun()
    
    # About section with professional styling
    st.markdown("---")
    st.markdown(f"""
    ### 🏆 About Champion Cleaners
    
    <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                border-left: 5px solid {BRAND_COLORS['primary']};">
        <p style="color: {BRAND_COLORS['text_dark']}; line-height: 1.8; margin: 0;">
            <strong>Champion Cleaners</strong> was established in the UAE in <strong>1997</strong>. The company's aim has always been to provide 
            <strong style="color: {BRAND_COLORS['primary']};">5-star premium dry cleaning and laundry services</strong> to high-income affluent expat and local 
            populations of Dubai and the United Arab Emirates. 
        </p>
        <p style="color: {BRAND_COLORS['text_dark']}; margin-top: 1rem; margin-bottom: 0;">
            Champion Cleaners UAE receives in excess of <strong>1.3 million retail garments annually</strong> and has more than <strong>19K Facebook</strong> & <strong>10.4K Instagram</strong> followers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Services highlights
    st.markdown(f"### ✨ Our Value-Added Services")
    
    col1, col2, col3, col4 = st.columns(4, gap="small")
    services_list = [
        ("👜", "Bag & Shoes Spa", "Leather restoration"),
        ("👗", "Wedding Gowns", "Premium preservation"),
        ("👶", "Baby Care", "Stroller & Car seat cleaning"),
        ("🧸", "Soft Toys", "Safe sanitization")
    ]
    
    for idx, (emoji, name, desc) in enumerate(services_list):
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {BRAND_COLORS['primary_light']} 0%, white 100%);
                        padding: 1rem; border-radius: 10px;
                        text-align: center; border: 2px solid {BRAND_COLORS['primary']};
                        border-top: 4px solid {BRAND_COLORS['primary']};
                        border-bottom: 4px solid {BRAND_COLORS['primary']};
                        transition: all 0.3s;
                        min-height: 140px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{emoji}</div>
                <p style="font-weight: 600; color: {BRAND_COLORS['primary']}; margin: 0; font-size: 0.95rem;">{name}</p>
                <p style="color: {BRAND_COLORS['text_light']}; font-size: 0.8rem; margin: 0.5rem 0 0 0; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="small")
    services_list2 = [
        ("🛏️", "Mattress Cleaning", "Dust mite elimination"),
        ("👔", "Super Crease", "Long-lasting creases"),
        ("✂️", "Alterations", "Professional tailoring"),
        ("🌱", "Green Tech", "Eco-friendly solutions")
    ]
    
    for idx, (emoji, name, desc) in enumerate(services_list2):
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {BRAND_COLORS['primary_light']} 0%, white 100%);
                        padding: 1rem; border-radius: 10px;
                        text-align: center; border: 2px solid {BRAND_COLORS['primary']};
                        border-top: 4px solid {BRAND_COLORS['primary']};
                        border-bottom: 4px solid {BRAND_COLORS['primary']};
                        transition: all 0.3s;
                        min-height: 140px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{emoji}</div>
                <p style="font-weight: 600; color: {BRAND_COLORS['primary']}; margin: 0; font-size: 0.95rem;">{name}</p>
                <p style="color: {BRAND_COLORS['text_light']}; font-size: 0.8rem; margin: 0.5rem 0 0 0; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contact information with enhanced styling
    st.markdown("---")
    st.markdown("### 📞 Contact Information")
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                    padding: 2rem; border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center; border: 2px solid {BRAND_COLORS['primary']};
                    border-top: 4px solid {BRAND_COLORS['primary']};
                    transition: all 0.3s;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.1rem; margin-bottom: 1rem;">📞 Phone</h3>
            <a href="tel:+97142858581" style="color: {BRAND_COLORS['primary']}; text-decoration: none; font-weight: 700; font-size: 1.05rem;">
                +971 4 2858581
            </a>
            <p style="margin: 1rem 0 0 0; color: {BRAND_COLORS['text_light']}; font-size: 0.9rem;">
                <a href="tel:8004556" style="color: {BRAND_COLORS['secondary']}; text-decoration: none; font-weight: 600;">Toll-Free: 800 4556</a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                    padding: 2rem; border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center; border: 2px solid {BRAND_COLORS['primary']};
                    border-top: 4px solid {BRAND_COLORS['primary']};
                    transition: all 0.3s;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.1rem; margin-bottom: 1rem;">💬 WhatsApp</h3>
            <a href="https://wa.me/971502130159" target="_blank" style="color: {BRAND_COLORS['primary']}; text-decoration: none; font-weight: 700; font-size: 1.05rem;">
                +971 50 213 0159
            </a>
            <p style="margin: 1rem 0 0 0; color: {BRAND_COLORS['text_light']}; font-size: 0.9rem;">
                Chat with us instantly
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                    padding: 2rem; border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center; border: 2px solid {BRAND_COLORS['primary']};
                    border-top: 4px solid {BRAND_COLORS['primary']};
                    transition: all 0.3s;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.1rem; margin-bottom: 1rem;">📧 Email & Web</h3>
            <a href="mailto:mail@champion-cleaners.com" style="color: {BRAND_COLORS['primary']}; text-decoration: none; font-weight: 600;">
                mail@champion-cleaners.com
            </a>
            <p style="margin: 1rem 0 0 0;">
                <a href="https://champion-cleaners.com" target="_blank" style="color: {BRAND_COLORS['primary']}; text-decoration: none; font-weight: 600; font-size: 0.95rem;">
                    🌐 Visit Website
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Premium Services Grid
    st.markdown("---")
    st.markdown(f"### 🌟 Premium Services")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    services = [
        ("📦", "Free Pick-up & Delivery", "Door-to-door convenience in Dubai, Abu Dhabi, Sharjah & Ajman"),
        ("🛋️", "Carpet & Upholstery Cleaning", "Advanced technology cleaning for all types of fabrics"),
        ("👜", "Bag & Shoe Spa", "Luxury leather restoration and care"),
        ("👗", "Wedding Gown Preservation", "Museum-quality preservation methods"),
        ("👔", "Super Crease", "Long-lasting freshness and perfect creases"),
        ("🧸", "Soft Toy Cleaning", "Safe and sanitized play items")
    ]
    
    cols = [col1, col2, col3]
    for idx, (emoji, title, desc) in enumerate(services):
        with cols[idx % 3]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {BRAND_COLORS['primary_light']} 0%, white 100%);
                        padding: 1.5rem; border-radius: 12px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                        border: 3px solid {BRAND_COLORS['primary']};
                        border-top: 4px solid {BRAND_COLORS['primary']};
                        border-bottom: 4px solid {BRAND_COLORS['primary']};
                        transition: all 0.3s;
                        cursor: pointer;
                        min-height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        align-items: stretch;">
                <div style="text-align: center; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem; text-align: center;">{emoji}</div>
                    <h4 style="color: {BRAND_COLORS['primary']}; margin: 0.3rem 0; text-align: center; font-size: 1rem;">{title}</h4>
                    <p style="color: {BRAND_COLORS['text_light']}; font-size: 0.85rem; margin: 0; text-align: center; line-height: 1.4;">{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Learn More →", key=f"service_{idx}", use_container_width=True):
                st.session_state.page = 'services'
                st.rerun()
    
    # Call to action banner
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
                color: white; padding: 3rem 2rem; border-radius: 15px;
                text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
        <h2 style="color: white; border: none; margin-top: 0;">🎯 Ready to Experience Premium Cleaning?</h2>
        <p style="font-size: 1.1rem; margin: 1rem 0; opacity: 0.95;">Schedule your pickup today and enjoy our premium services at your doorstep!</p>
    </div>
    """, unsafe_allow_html=True)
