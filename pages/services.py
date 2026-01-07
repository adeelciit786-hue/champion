"""
Services page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS

def show():
    st.markdown(f"### 🧹 Our Services")
    st.markdown("Explore our premium cleaning and laundry services designed for your needs")
    
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
    
    # Display services
    for service_name, service_info in services_data.items():
        with st.expander(f"### {service_name}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**{service_info['description']}**")
                st.markdown("**Key Features:**")
                for feature in service_info['features']:
                    st.markdown(f"• {feature}")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #F0F9FF, #FFFFFF); 
                           padding: 15px; border-radius: 10px; border-left: 3px solid {BRAND_COLORS['primary']};">
                    <p style="margin-top: 0;"><strong>⏱️ Turnaround</strong><br>{service_info['turnaround']}</p>
                    <p><strong>💰 Price</strong><br>{service_info['price']}</p>
                    <button onclick="window.location.href='/schedule'">📅 Schedule</button>
                </div>
                """, unsafe_allow_html=True)
    
    # Green Technologies
    st.markdown("---")
    st.markdown(f"### ♻️ Our Eco-Friendly Technologies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **Green Earth Technology**
        
        • Liquid silicone based
        • Odourless & non-toxic
        • Eco-friendly cleaning
        • Approved by authorities
        """)
    
    with col2:
        st.markdown(f"""
        **Excello Wet Cleaning**
        
        • Most advanced soft wash
        • Gentle on fabrics
        • Environmental safe
        • Premium quality
        """)
    
    with col3:
        st.markdown(f"""
        **I-Genius Technology**
        
        • Chemical-free ozone
        • Complete sanitization
        • Microorganism removal
        • Safe & effective
        """)
    
    # Schedule CTA
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📅 Schedule Your Service Now", use_container_width=True):
            st.switch_page("pages/schedule.py")
