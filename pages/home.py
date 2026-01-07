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
    
    # Quick access cards - clickable with proper sizing
    st.markdown("### Quick Access")
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    
    with col1:
        if st.button("📅 Schedule Pickup\n\nBook a convenient pickup time for your laundry", key="quick_schedule", use_container_width=True, help="Click to schedule pickup"):
            st.session_state.page = 'schedule'
            st.rerun()
    
    with col2:
        if st.button("📍 Track Order\n\nCheck the status of your order", key="quick_track", use_container_width=True, help="Click to track order"):
            st.session_state.page = 'track'
            st.rerun()
    
    with col3:
        if st.button("❓ FAQs\n\nFind answers to common questions", key="quick_faq", use_container_width=True, help="Click to view FAQs"):
            st.session_state.page = 'faq'
            st.rerun()
    
    with col4:
        if st.button("🎁 Offers\n\nCheck out our latest deals", key="quick_offers", use_container_width=True, help="Click to view offers"):
            st.session_state.page = 'offers'
            st.rerun()
    
    # About section
    st.markdown("---")
    st.markdown("""
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
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; cursor: pointer;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem; margin-bottom: 1rem;">📞 Phone</h3>
            <a href="tel:+97142858581" style="color: #333; text-decoration: none; font-size: 1rem; font-weight: 600;">
                <p style="margin: 0.5rem 0;">+971 4 2858581</p>
            </a>
            <a href="tel:8004556" style="color: #333; text-decoration: none; font-size: 0.9rem;">
                <p style="margin: 0.5rem 0;"><strong>Toll-Free:</strong> 800 4556</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; cursor: pointer;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem; margin-bottom: 1rem;">💬 WhatsApp</h3>
            <a href="https://wa.me/971502130159" target="_blank" style="color: #25D366; text-decoration: none; font-weight: 600;">
                <p style="margin: 0.5rem 0; font-size: 1rem;">+971 50 213 0159</p>
            </a>
            <p style="margin: 0.5rem 0; font-size: 0.85rem; color: #666;">Chat with us instantly</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; cursor: pointer;">
            <h3 style="color: {BRAND_COLORS['primary']}; font-size: 1.2rem; margin-bottom: 1rem;">📧 Email</h3>
            <a href="mailto:mail@champion-cleaners.com" style="color: #333; text-decoration: none;">
                <p style="margin: 0.5rem 0; font-size: 0.95rem;">mail@champion-cleaners.com</p>
            </a>
            <a href="https://champion-cleaners.com" target="_blank" style="color: #333; text-decoration: none; font-size: 0.9rem;">
                <p style="margin: 0.5rem 0;">champion-cleaners.com</p>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # Services Section
    st.markdown("---")
    st.markdown("### Our Premium Services")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
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
            if st.button(f"{emoji} {title}\n\n{desc}", key=f"service_{idx}", use_container_width=True, help="Click to view details"):
                st.session_state.page = 'services'
                st.rerun()
