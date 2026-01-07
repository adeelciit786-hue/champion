"""
Home page for Champion Cleaners - Fully Responsive & Optimized
"""

import streamlit as st
from config import BRAND_COLORS

def show():
    # Set page background to white
    st.markdown("""
    <style>
        .main { background-color: white; }
        body { background-color: white; }
        [data-testid="stAppViewContainer"] { background-color: white; }
        h1, h2, h3, h4, h5, h6 { color: #333333; margin-bottom: 0.5rem; }
        .stMarkdown { margin-bottom: 0.5rem; }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']} 0%, {BRAND_COLORS['secondary']} 100%);
                color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
        <h1 style="color: white; margin: 0; font-size: 2.5rem;">🏢 Welcome to Champion Cleaners</h1>
        <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; opacity: 0.95;">Your Trusted Laundry & Dry Cleaning Service in the UAE</p>
        <p style="color: white; font-size: 0.95rem; margin-top: 1rem; opacity: 0.9;">Established 1997 | Premium Quality | 20+ Years of Excellence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Access Section - Consistent Cards with Single CTA
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>🚀 Quick Access</h2>", unsafe_allow_html=True)
    
    # Define quick access items with icon, title, description, and navigation
    quick_actions = [
        {
            "icon": "📅",
            "title": "Schedule Pickup",
            "description": "Book a convenient pickup time",
            "key": "quick_schedule",
            "page": "schedule",
            "color": "primary"  # Green
        },
        {
            "icon": "📍",
            "title": "Track Order",
            "description": "Check your order status",
            "key": "quick_track",
            "page": "track",
            "color": "secondary"  # Red
        },
        {
            "icon": "❓",
            "title": "FAQs",
            "description": "Find answers to common questions",
            "key": "quick_faq",
            "page": "faq",
            "color": "primary"  # Green
        },
        {
            "icon": "🎁",
            "title": "Special Offers",
            "description": "View our latest deals",
            "key": "quick_offers",
            "page": "offers",
            "color": "secondary"  # Red
        }
    ]
    
    # Cards row - Fixed height and alignment
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    cols = [col1, col2, col3, col4]
    
    for idx, action in enumerate(quick_actions):
        color_key = action['color']
        primary_color = BRAND_COLORS[color_key]
        light_color = BRAND_COLORS[f'{color_key}_light']
        
        with cols[idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {light_color} 0%, white 100%);
                        padding: 1.5rem; border-radius: 12px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                        border: 2px solid {primary_color};
                        border-top: 4px solid {primary_color};
                        border-bottom: 4px solid {primary_color};
                        transition: all 0.3s;
                        cursor: pointer;
                        min-height: 200px;
                        height: 200px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        box-sizing: border-box;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem; line-height: 1;">{action['icon']}</div>
                <h4 style="color: {primary_color}; margin: 0.3rem 0; font-size: 1rem; font-weight: 600; line-height: 1.3;">{action['title']}</h4>
                <p style="color: #666666; font-size: 0.85rem; margin: 0; line-height: 1.4;">{action['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Buttons row - separate from cards
    st.markdown("")  # Small spacing
    btn1, btn2, btn3, btn4 = st.columns(4, gap="medium")
    button_cols = [btn1, btn2, btn3, btn4]
    
    for idx, action in enumerate(quick_actions):
        with button_cols[idx]:
            if st.button("Learn More →", key=action['key'], use_container_width=True):
                st.session_state.page = action['page']
                st.rerun()
    
    # About section with professional styling
    st.markdown("---")
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>🏆 About Champion Cleaners</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                border-left: 5px solid {BRAND_COLORS['primary']};">
        <p style="color: #333333; line-height: 1.8; margin: 0;">
            <strong>Champion Cleaners</strong> was established in the UAE in <strong>1997</strong>. The company's aim has always been to provide 
            <strong style="color: {BRAND_COLORS['primary']};">5-star premium dry cleaning and laundry services</strong> to high-income affluent expat and local 
            populations of Dubai and the United Arab Emirates. 
        </p>
        <p style="color: #333333; margin-top: 1rem; margin-bottom: 0;">
            Champion Cleaners UAE receives in excess of <strong>1.3 million retail garments annually</strong> and has more than <strong>19K Facebook</strong> & <strong>10.4K Instagram</strong> followers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Services highlights
    st.markdown("---")
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>✨ Our Value-Added Services</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    services_list = [
        ("👜", "Bag & Shoes Spa", "Leather restoration", "primary"),
        ("👗", "Wedding Gowns", "Premium preservation", "secondary"),
        ("👶", "Baby Care", "Stroller & Car seat cleaning", "primary"),
        ("🧸", "Soft Toys", "Safe sanitization", "secondary")
    ]
    
    for idx, (emoji, name, desc, color_key) in enumerate(services_list):
        primary_color = BRAND_COLORS[color_key]
        light_color = BRAND_COLORS[f'{color_key}_light']
        
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {light_color} 0%, white 100%);
                        padding: 1rem; border-radius: 10px;
                        text-align: center; border: 2px solid {primary_color};
                        border-top: 4px solid {primary_color};
                        border-bottom: 4px solid {primary_color};
                        transition: all 0.3s;
                        min-height: 155px;
                        height: 155px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        box-sizing: border-box;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem; line-height: 1;">{emoji}</div>
                <p style="font-weight: 600; color: {primary_color}; margin: 0; font-size: 0.95rem;">{name}</p>
                <p style="color: #666666; font-size: 0.8rem; margin: 0.5rem 0 0 0; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    services_list2 = [
        ("🛏️", "Mattress Cleaning", "Dust mite elimination", "secondary"),
        ("👔", "Super Crease", "Long-lasting creases", "primary"),
        ("✂️", "Alterations", "Professional tailoring", "secondary"),
        ("🌱", "Green Tech", "Eco-friendly solutions", "primary")
    ]
    
    for idx, (emoji, name, desc, color_key) in enumerate(services_list2):
        primary_color = BRAND_COLORS[color_key]
        light_color = BRAND_COLORS[f'{color_key}_light']
        
        with [col1, col2, col3, col4][idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {light_color} 0%, white 100%);
                        padding: 1rem; border-radius: 10px;
                        text-align: center; border: 2px solid {primary_color};
                        border-top: 4px solid {primary_color};
                        border-bottom: 4px solid {primary_color};
                        transition: all 0.3s;
                        min-height: 155px;
                        height: 155px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        box-sizing: border-box;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem; line-height: 1;">{emoji}</div>
                <p style="font-weight: 600; color: {primary_color}; margin: 0; font-size: 0.95rem;">{name}</p>
                <p style="color: #666666; font-size: 0.8rem; margin: 0.5rem 0 0 0; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contact information with enhanced styling
    st.markdown("---")
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>📞 Contact Information</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="medium")
    
    contact_info = [
        ("📞 Phone", "+971 4 2858581", "tel:+97142858581", "primary"),
        ("💬 WhatsApp", "+971 50 213 0159", "https://wa.me/971502130159", "secondary"),
        ("📧 Email", "mail@champion-cleaners.com", "mailto:mail@champion-cleaners.com", "primary")
    ]
    
    cols_contact = [col1, col2, col3]
    for idx, (title, value, link, color_key) in enumerate(contact_info):
        primary_color = BRAND_COLORS[color_key]
        light_color = BRAND_COLORS[f'{color_key}_light']
        
        with cols_contact[idx]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {light_color}, white);
                        padding: 2rem; border-radius: 12px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                        text-align: center; border: 2px solid {primary_color};
                        border-top: 4px solid {primary_color};
                        transition: all 0.3s;
                        min-height: 200px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        box-sizing: border-box;">
                <h3 style="color: {primary_color}; font-size: 1.1rem; margin-bottom: 1rem;">{title}</h3>
                <a href="{link}" style="color: {primary_color}; text-decoration: none; font-weight: 700; font-size: 1.05rem;">
                    {value}
                </a>
                <p style="margin: 1rem 0 0 0; color: #666666; font-size: 0.9rem;">
                    {'Toll-Free: 800 4556' if '📞' in title else 'Chat with us instantly' if '💬' in title else 'Get in touch'}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # Premium Services Grid
    st.markdown("---")
    st.markdown("<h2 style='margin-bottom: 1.5rem;'>🌟 Premium Services</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    services = [
        ("📦", "Free Pick-up & Delivery", "Door-to-door convenience in Dubai, Abu Dhabi, Sharjah & Ajman", "primary"),
        ("🛋️", "Carpet & Upholstery Cleaning", "Advanced technology cleaning for all types of fabrics", "secondary"),
        ("👜", "Bag & Shoe Spa", "Luxury leather restoration and care", "primary"),
        ("👗", "Wedding Gown Preservation", "Museum-quality preservation methods", "secondary"),
        ("👔", "Super Crease", "Long-lasting freshness and perfect creases", "primary"),
        ("🧸", "Soft Toy Cleaning", "Safe and sanitized play items", "secondary")
    ]
    
    cols = [col1, col2, col3]
    for idx, (emoji, title, desc, color_key) in enumerate(services):
        primary_color = BRAND_COLORS[color_key]
        light_color = BRAND_COLORS[f'{color_key}_light']
        
        with cols[idx % 3]:
            st.markdown(f"""
            <div style="background: linear-gradient(180deg, {light_color} 0%, white 100%);
                        padding: 1.5rem; border-radius: 12px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                        border: 2px solid {primary_color};
                        border-top: 4px solid {primary_color};
                        border-bottom: 4px solid {primary_color};
                        transition: all 0.3s;
                        cursor: pointer;
                        min-height: 200px;
                        height: 200px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        box-sizing: border-box;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem; line-height: 1;">{emoji}</div>
                <h4 style="color: {primary_color}; margin: 0.3rem 0; font-size: 1rem; font-weight: 600;">{title}</h4>
                <p style="color: #666666; font-size: 0.85rem; margin: 0; line-height: 1.4;">{desc}</p>
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
