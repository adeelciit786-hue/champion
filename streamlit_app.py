"""
Champion Cleaners - Streamlit Application
A complete replica of the Flask application in Streamlit
"""

import streamlit as st
from pages import home, faq, schedule, track, services, offers
from config import BRAND_COLORS

st.set_page_config(
    page_title="Champion Cleaners",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match Flask templates exactly
st.markdown(f"""
<style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    body {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f5f5f5;
        color: #333;
    }}
    
    .navbar {{
        background-color: white;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-bottom: 4px solid {BRAND_COLORS['primary']};
        margin-bottom: 2rem;
    }}
    
    .navbar h1 {{
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .navbar-brand-champion {{
        color: {BRAND_COLORS['primary']};
    }}
    
    .navbar-brand-cleaners {{
        color: {BRAND_COLORS['secondary']};
    }}
    
    .header {{
        text-align: center;
        background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']}, #FFFFFF);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }}
    
    .header h1 {{
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}
    
    .header p {{
        font-size: 1.2rem;
        opacity: 0.95;
    }}
    
    .footer {{
        background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
        color: white;
        text-align: center;
        padding: 2.5rem;
        margin-top: 3rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }}
    
    .stApp {{
        background-color: #f5f5f5;
    }}
    
    .stButton > button {{
        background: linear-gradient(135deg, {BRAND_COLORS['primary']}, #28C258) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: transform 0.3s, box-shadow 0.3s !important;
        box-shadow: 0 4px 15px {BRAND_COLORS['primary']}40 !important;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px {BRAND_COLORS['primary']}50 !important;
    }}
</style>
""", unsafe_allow_html=True)

# Session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Create navbar with logo and inline buttons
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1.2, 1, 1, 1, 1, 1, 1, 0.5])

with col1:
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: flex-start; padding: 0.5rem 1rem;">
        <span style="font-size: 1.3rem; font-weight: 700; letter-spacing: 1px;">
            <span style="color: {BRAND_COLORS['primary']};">CHAMPION</span>
            <br>
            <span style="color: {BRAND_COLORS['secondary']};">CLEANERS</span>
        </span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🏠 Home", key="nav_home", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()

with col3:
    if st.button("📅 Schedule", key="nav_schedule", use_container_width=True):
        st.session_state.page = 'schedule'
        st.rerun()

with col4:
    if st.button("📍 Track", key="nav_track", use_container_width=True):
        st.session_state.page = 'track'
        st.rerun()

with col5:
    if st.button("🧹 Services", key="nav_services", use_container_width=True):
        st.session_state.page = 'services'
        st.rerun()

with col6:
    if st.button("❓ FAQ", key="nav_faq", use_container_width=True):
        st.session_state.page = 'faq'
        st.rerun()

with col7:
    if st.button("🎁 Offers", key="nav_offers", use_container_width=True):
        st.session_state.page = 'offers'
        st.rerun()

st.divider()

# Page routing
if st.session_state.page == 'home':
    home.show()
elif st.session_state.page == 'faq':
    faq.show()
elif st.session_state.page == 'schedule':
    schedule.show()
elif st.session_state.page == 'track':
    track.show()
elif st.session_state.page == 'services':
    services.show()
elif st.session_state.page == 'offers':
    offers.show()
else:
    home.show()

st.divider()

# Footer
st.markdown(f"""
<div class="footer">
    <p>&copy; 2025 Champion Cleaners. Your Trusted Laundry Partner.</p>
    <p>📞 +971 4 2858581 | 📧 mail@champion-cleaners.com | 🌐 champion-cleaners.com</p>
</div>
""", unsafe_allow_html=True)
