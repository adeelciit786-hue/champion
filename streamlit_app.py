"""
Champion Cleaners - Streamlit Application
A multi-page web application for laundry and dry cleaning services
"""

import streamlit as st
from config import BRAND_COLORS, APP_TITLE, APP_SUBTITLE

# Set page configuration
st.set_page_config(
    page_title="Champion Cleaners",
    page_icon="🧼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
def load_custom_css():
    st.markdown(f"""
    <style>
        :root {{
            --primary-color: {BRAND_COLORS['primary']};
            --secondary-color: {BRAND_COLORS['secondary']};
        }}
        
        .main {{
            background-color: #f5f5f5;
        }}
        
        .stButton > button {{
            background: linear-gradient(135deg, {BRAND_COLORS['primary']}, #28C258);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            width: 100%;
        }}
        
        .stButton > button:hover {{
            box-shadow: 0 6px 20px {BRAND_COLORS['primary']}80;
        }}
        
        .header-title {{
            color: {BRAND_COLORS['primary']};
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        
        .header-subtitle {{
            color: {BRAND_COLORS['secondary']};
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }}
        
        .service-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-top: 3px solid {BRAND_COLORS['primary']};
            text-align: center;
        }}
        
        .alert-success {{
            background-color: #E8F9F3;
            color: #00A651;
            border-left: 4px solid #00A651;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
        
        .alert-error {{
            background-color: #FCE8E8;
            color: #C1272D;
            border-left: 4px solid #C1272D;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 1rem;
        }}
    </style>
    """, unsafe_allow_html=True)

load_custom_css()

# Sidebar navigation
st.sidebar.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: {BRAND_COLORS['primary']}; margin: 0;">CHAMPION</h1>
        <p style="color: {BRAND_COLORS['secondary']}; margin: 0; font-size: 0.9rem;">CLEANERS</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Navigation pages
pages = {
    "🏠 Home": "home",
    "📋 Schedule Pickup": "schedule",
    "📍 Track Order": "track",
    "🧹 Services": "services",
    "❓ FAQs": "faq",
    "🎁 Offers": "offers"
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
    <div style="text-align: center; font-size: 0.85rem; color: #666;">
        <p><strong>📞 Call Us</strong><br>+971 4 2858581<br>Toll-Free: 800 4556</p>
        <p><strong>📧 Email</strong><br>mail@champion-cleaners.com</p>
    </div>
""", unsafe_allow_html=True)

# Main content area
if selected_page == "🏠 Home":
    from pages import home
    home.show()
elif selected_page == "📋 Schedule Pickup":
    from pages import schedule
    schedule.show()
elif selected_page == "📍 Track Order":
    from pages import track
    track.show()
elif selected_page == "🧹 Services":
    from pages import services
    services.show()
elif selected_page == "❓ FAQs":
    from pages import faq
    faq.show()
elif selected_page == "🎁 Offers":
    from pages import offers
    offers.show()

# Footer
st.markdown("---")
st.markdown(f"""
    <div style="text-align: center; padding: 20px; color: #666; font-size: 0.9rem;">
        <p>&copy; 2025 Champion Cleaners. Your Trusted Laundry Partner.</p>
        <p>Following us on social media for updates and offers</p>
    </div>
""", unsafe_allow_html=True)
