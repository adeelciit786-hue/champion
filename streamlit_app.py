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
    
    :root {{
        --primary-color: {BRAND_COLORS['primary']};
        --secondary-color: {BRAND_COLORS['secondary']};
        --accent-blue: {BRAND_COLORS['accent_blue']};
        --light-bg: {BRAND_COLORS['light']};
        --text-dark: {BRAND_COLORS['text_dark']};
        --text-light: {BRAND_COLORS['text_light']};
        --success-color: {BRAND_COLORS['success']};
        --warning-color: {BRAND_COLORS['warning']};
        --error-color: {BRAND_COLORS['error']};
    }}
    
    html, body {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #f5f5f5 0%, #fafafa 100%);
        color: var(--text-dark);
        line-height: 1.6;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, #f5f5f5 0%, #fafafa 100%);
    }}
    
    /* Typography */
    h1, h2, h3 {{
        font-weight: 700;
        color: var(--text-dark);
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        letter-spacing: 0.5px;
    }}
    
    h1 {{
        font-size: 2.5rem;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    h2 {{
        font-size: 1.8rem;
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: 0.5rem;
    }}
    
    h3 {{
        font-size: 1.4rem;
        color: var(--primary-color);
    }}
    
    h4 {{
        font-size: 1.1rem;
        color: var(--secondary-color);
        font-weight: 600;
    }}
    
    /* Navbar */
    .navbar {{
        background: white;
        padding: 1.2rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border-bottom: 4px solid var(--primary-color);
        margin-bottom: 2rem;
        border-radius: 0 0 10px 10px;
    }}
    
    .navbar-brand {{
        font-size: 1.3rem;
        font-weight: 700;
        letter-spacing: 1px;
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }}
    
    .navbar-brand-champion {{
        color: var(--primary-color);
    }}
    
    .navbar-brand-cleaners {{
        color: var(--secondary-color);
    }}
    
    /* Buttons */
    .stButton > button {{
        background: linear-gradient(135deg, var(--primary-color), #28C258) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0, 166, 81, 0.3) !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(0, 166, 81, 0.4) !important;
        background: linear-gradient(135deg, #008C3F, #24A752) !important;
    }}
    
    .stButton > button:active {{
        transform: translateY(-1px) !important;
    }}
    
    /* Special Schedule Button */
    button[key*="nav_schedule"] {{
        background: linear-gradient(135deg, var(--secondary-color), #D63945) !important;
        box-shadow: 0 4px 15px rgba(193, 39, 45, 0.3) !important;
    }}
    
    button[key*="nav_schedule"]:hover {{
        background: linear-gradient(135deg, #A01F24, #E63946) !important;
        box-shadow: 0 8px 25px rgba(193, 39, 45, 0.4) !important;
    }}
    
    /* Form Elements */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stMultiSelect > div > div > div {{
        border: 2px solid {BRAND_COLORS['light_dark']} !important;
        border-radius: 8px !important;
        padding: 0.8rem !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        background-color: white !important;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus,
    .stMultiSelect > div > div > div:focus {{
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 3px rgba(0, 166, 81, 0.1) !important;
        outline: none !important;
    }}
    
    /* Cards and Containers */
    .stMetric {{
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border-left: 4px solid var(--primary-color);
        transition: all 0.3s ease;
    }}
    
    .stMetric:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }}
    
    /* Dividers */
    hr, .stDivider {{
        border: none !important;
        border-top: 2px solid var(--light-bg) !important;
        margin: 2rem 0 !important;
    }}
    
    /* Expander */
    .streamlit-expanderHeader {{
        background-color: white;
        border: 2px solid var(--light-bg);
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }}
    
    .streamlit-expanderHeader:hover {{
        border-color: var(--primary-color);
        box-shadow: 0 4px 12px rgba(0, 166, 81, 0.15);
    }}
    
    /* Alert/Messages */
    .stSuccess {{
        background-color: {BRAND_COLORS['primary_light']} !important;
        border-left: 4px solid var(--success-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }}
    
    .stWarning {{
        background-color: #FFF3E0 !important;
        border-left: 4px solid var(--warning-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }}
    
    .stError {{
        background-color: {BRAND_COLORS['secondary_light']} !important;
        border-left: 4px solid var(--error-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }}
    
    .stInfo {{
        background-color: #E3F2FD !important;
        border-left: 4px solid var(--accent-blue) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }}
    
    /* Header Sections */
    .header {{
        text-align: center;
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 15px;
        margin-bottom: 2.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }}
    
    .header::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 100%);
    }}
    
    .header h1 {{
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
        color: white;
        -webkit-text-fill-color: white;
    }}
    
    .header p {{
        font-size: 1.2rem;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }}
    
    /* Footer */
    .footer {{
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        text-align: center;
        padding: 3rem 2rem;
        margin-top: 3rem;
        border-radius: 15px 15px 0 0;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
    }}
    
    .footer p {{
        margin: 0.5rem 0;
        font-size: 0.95rem;
    }}
    
    /* Responsive */
    @media (max-width: 768px) {{
        h1 {{ font-size: 2rem; }}
        h2 {{ font-size: 1.5rem; }}
        h3 {{ font-size: 1.2rem; }}
        .header {{ padding: 2rem 1rem; }}
    }}
</style>
""", unsafe_allow_html=True)

# Session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Create navbar with logo and inline buttons all in one row
st.markdown(f"""
<div style="background-color: white; padding: 1rem 2rem; border-bottom: 4px solid {BRAND_COLORS['primary']};
            box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-radius: 0 0 10px 10px;
            margin: -1rem -1rem 2rem -1rem; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 2rem; width: 100%;">
        <span style="font-size: 1.3rem; font-weight: 700; letter-spacing: 1px; white-space: nowrap;">
            <span style="color: {BRAND_COLORS['primary']};">CHAMPION</span>
            <br>
            <span style="color: {BRAND_COLORS['secondary']};">CLEANERS</span>
        </span>
        <div style="display: flex; gap: 0.8rem; flex-wrap: wrap; align-items: center;">
            <!-- Navigation buttons will be placed here by columns -->
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Create inline navigation buttons
nav_cols = st.columns([0.6, 0.8, 1, 0.8, 1.1, 0.8, 1, 1])

nav_buttons = [
    ("🏠 HOME", "home", nav_cols[0]),
    ("📅 SCHEDULE", "schedule", nav_cols[1]),
    ("📍 TRACK", "track", nav_cols[2]),
    ("🧹 SERVICES", "services", nav_cols[3]),
    ("❓ FAQ", "faq", nav_cols[4]),
    ("🎁 OFFERS", "offers", nav_cols[5])
]

for button_text, page_name, col in nav_buttons:
    with col:
        if page_name == "schedule":
            # Special styling for Schedule button
            button_clicked = st.button(
                button_text,
                key=f"nav_{page_name}",
                use_container_width=True,
                help=f"Go to {page_name.capitalize()}"
            )
        else:
            button_clicked = st.button(
                button_text,
                key=f"nav_{page_name}",
                use_container_width=True,
                help=f"Go to {page_name.capitalize()}"
            )
        
        if button_clicked:
            st.session_state.page = page_name
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
