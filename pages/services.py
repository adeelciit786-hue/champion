"""
Services page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS

def show():
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
                color: white; padding: 2rem; border-radius: 12px; text-align: center;">
        <h1 style="color: white; border: none; margin-top: 0;">🧹 Our Premium Services</h1>
        <p style="opacity: 0.95; margin: 0;">Explore our world-class cleaning and laundry services designed for your needs</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Services data
    services_data = {
        "🎒 Bag & Shoes Spa": {
            "description": "Professional cleaning and restoration of high-end designer leather goods and accessories",
            "features": [
                "Oil extraction and conditioning",
                "Edge restoration and repair",
                "Marker and ink removal",
                "Strap repair and stitching",
                "Color restoration",
                "Eco-friendly leather care products"
            ],
            "turnaround": "Shoes: 5-7 days | Bags: 6-8 days",
            "price": "Contact for quote"
        },
        "👗 Wedding Gown Cleaning": {
            "description": "Specialized cleaning and preservation of wedding gowns using museum-quality methods",
            "features": [
                "Gentle cleaning techniques",
                "Premium cleaning solutions",
                "Museum Method (Hanging) preservation",
                "Champion Box method option",
                "Acid-free environment storage",
                "Dust protection and air circulation"
            ],
            "turnaround": "4-6 days",
            "price": "Contact for quote"
        },
        "👶 Stroller & Car Seat Cleaning": {
            "description": "Safe and thorough cleaning of essential baby items using gentle yet effective methods",
            "features": [
                "Deep sanitization process",
                "Eco-friendly cleaning solutions",
                "I-Genius Technology ozone",
                "Dust mite elimination",
                "Microorganism removal",
                "Safe for delicate materials"
            ],
            "turnaround": "3-4 days",
            "price": "AED 150-250"
        },
        "🧸 Soft Toy Cleaning": {
            "description": "Professional cleaning and sanitization of children's soft toys using safe methods",
            "features": [
                "Gentle cleaning process",
                "Complete sanitization",
                "I-Genius Technology",
                "Dust mite elimination",
                "Eco-friendly disinfection",
                "Safe for children"
            ],
            "turnaround": "2-3 days",
            "price": "AED 50-100 per toy"
        },
        "🛏️ Mattress Cleaning": {
            "description": "Comprehensive mattress cleaning and sanitization eliminating dust mites and microorganisms",
            "features": [
                "Aqua Jet Injection machines",
                "Dust mite elimination",
                "Microorganism removal",
                "Thorough deep cleaning",
                "Quick drying technology",
                "No mess or residue"
            ],
            "turnaround": "Same day - 24 hours",
            "price": "AED 200-400"
        },
        "✨ Super Crease": {
            "description": "Professional crease service creating long-lasting permanent creases on garments",
            "features": [
                "Professional techniques",
                "Permanent crease guarantee",
                "Lasts through multiple washes",
                "Perfect for formal wear",
                "Expert application",
                "Premium quality finish"
            ],
            "turnaround": "2-3 days",
            "price": "AED 50-100 per item"
        },
        "🪡 Alterations Clinique": {
            "description": "Professional alteration services by expert tailors for all types of garments",
            "features": [
                "Expert tailoring team",
                "All garment types",
                "Custom alterations",
                "Perfect fit guarantee",
                "Quality workmanship",
                "Competitive pricing"
            ],
            "turnaround": "5-7 days",
            "price": "Contact for quote"
        },
        "🧽 Home Cleaning Services": {
            "description": "Innovative cleaning solutions for carpets, rugs, curtains, sofas and upholstery",
            "features": [
                "Carpet and rug cleaning",
                "Curtain cleaning",
                "Sofa and upholstery care",
                "Dust mite elimination",
                "Microorganism removal",
                "Quick drying technology"
            ],
            "turnaround": "Same day available",
            "price": "Contact for quote"
        }
    }
    
    # Display services with professional styling
    for idx, (service_name, service_info) in enumerate(services_data.items()):
        with st.expander(f"**{service_name}**", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                <div style="color: {BRAND_COLORS['text_dark']};">
                    <p style="font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">{service_info['description']}</p>
                    <h4 style="color: {BRAND_COLORS['primary']}; margin-bottom: 0.5rem;">✓ Key Features:</h4>
                </div>
                """, unsafe_allow_html=True)
                
                for feature in service_info['features']:
                    st.markdown(f"• {feature}")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                           padding: 1.5rem; border-radius: 12px;
                           border-left: 5px solid {BRAND_COLORS['primary']};
                           box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
                    <div style="margin-bottom: 1rem;">
                        <p style="font-weight: 600; color: {BRAND_COLORS['primary']}; margin-bottom: 0.3rem;">⏱️ Turnaround Time</p>
                        <p style="color: {BRAND_COLORS['text_dark']}; margin: 0; font-size: 0.95rem;">{service_info['turnaround']}</p>
                    </div>
                    <div>
                        <p style="font-weight: 600; color: {BRAND_COLORS['secondary']}; margin-bottom: 0.3rem;">💰 Starting Price</p>
                        <p style="color: {BRAND_COLORS['text_dark']}; margin: 0; font-size: 0.95rem;">{service_info['price']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Green Technologies
    st.markdown("---")
    st.markdown(f"### ♻️ Our Eco-Friendly Technologies")
    st.markdown("We are proud to use world-class, environmentally responsible cleaning technologies")
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                    padding: 1.5rem; border-radius: 12px;
                    border-top: 4px solid {BRAND_COLORS['primary']};
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center;">
            <h3 style="color: {BRAND_COLORS['primary']}; margin-top: 0; font-size: 1.1rem;">🌍 Green Earth</h3>
            <p style="color: {BRAND_COLORS['text_light']}; margin: 0; font-size: 0.9rem;">
                <strong style="color: {BRAND_COLORS['text_dark']};">Liquid Silicone Based</strong><br>
                Odourless, non-toxic &<br>eco-friendly cleaning
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {BRAND_COLORS['secondary_light']}, white);
                    padding: 1.5rem; border-radius: 12px;
                    border-top: 4px solid {BRAND_COLORS['secondary']};
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center;">
            <h3 style="color: {BRAND_COLORS['secondary']}; margin-top: 0; font-size: 1.1rem;">💧 Excello Wash</h3>
            <p style="color: {BRAND_COLORS['text_light']}; margin: 0; font-size: 0.9rem;">
                <strong style="color: {BRAND_COLORS['text_dark']};">Advanced Soft Wash</strong><br>
                Gentle on fabrics &<br>environmentally safe
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E3F2FD, white);
                    padding: 1.5rem; border-radius: 12px;
                    border-top: 4px solid {BRAND_COLORS['accent_blue']};
                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                    text-align: center;">
            <h3 style="color: {BRAND_COLORS['accent_blue']}; margin-top: 0; font-size: 1.1rem;">⚡ I-Genius</h3>
            <p style="color: {BRAND_COLORS['text_light']}; margin: 0; font-size: 0.9rem;">
                <strong style="color: {BRAND_COLORS['text_dark']};">Chemical-Free Ozone</strong><br>
                Complete sanitization &<br>safe & effective
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Schedule CTA
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
                color: white; padding: 3rem 2rem; border-radius: 15px;
                text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
        <h2 style="color: white; border: none; margin-top: 0;">🎯 Ready to Schedule Your Service?</h2>
        <p style="opacity: 0.95; font-size: 1.05rem;">Choose your service and book a convenient pickup time</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Schedule Service Now", use_container_width=True):
            st.session_state.page = 'schedule'
            st.rerun()
