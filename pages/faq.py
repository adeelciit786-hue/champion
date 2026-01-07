"""
FAQ page for Champion Cleaners - Matches Flask template exactly
"""

import streamlit as st
from config import BRAND_COLORS, FAQ_DATA, get_future_dates, get_time_slots, SERVICES
from app import search_faq
from database import save_order

def show():
    st.markdown(f"""
    <h1 style="color: {BRAND_COLORS['primary']}; text-align: center; margin-bottom: 2rem;">Frequently Asked Questions</h1>
    """, unsafe_allow_html=True)
    
    # Search Box
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input("Search FAQ...", placeholder="e.g., 'turnaround time', 'bag cleaning'", key="faq_search")
    with col2:
        search_button = st.button("Search", use_container_width=True)
    
    st.markdown("---")
    
    # Display search results or all FAQs
    if search_button and search_query:
        result = search_faq(search_query)
        
        if result:
            # Found matching FAQ
            st.markdown(f"""
            <div style="background: #E8F9F3; padding: 1rem; border-radius: 8px; border-left: 4px solid #00A651;">
                <p style="color: #00A651; font-weight: 600;">✅ Answer Found!</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 3px solid {BRAND_COLORS['primary']}; margin: 1rem 0;">
                <div style="color: {BRAND_COLORS['primary']}; font-weight: 600; margin-bottom: 1rem; font-size: 1.05rem;">
                    {result['question']}
                </div>
                <div style="color: #555; line-height: 1.6;">
                    {result['answer']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown(f"<h2 style='color: {BRAND_COLORS['primary']};'>Schedule Pickup Now</h2>", unsafe_allow_html=True)
            
            with st.form("schedule_form_faq"):
                col1, col2 = st.columns(2)
                with col1:
                    full_name = st.text_input("Full Name *")
                with col2:
                    phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567")
                
                email = st.text_input("Email (Optional)")
                address = st.text_area("Pickup Address *", placeholder="Enter your full address")
                
                col3, col4 = st.columns(2)
                with col3:
                    dates = get_future_dates(30)
                    pickup_date = st.selectbox("Pickup Date *", options=dates)
                with col4:
                    times = get_time_slots()
                    pickup_time = st.selectbox("Pickup Time *", options=times)
                
                service_type = st.selectbox("Service Type *", options=SERVICES)
                notes = st.text_area("Special Instructions (Optional)")
                
                if st.form_submit_button("Confirm & Schedule Pickup"):
                    if not full_name or not phone or not address:
                        st.error("Please fill in all required fields")
                    else:
                        try:
                            order_id = save_order({
                                'full_name': full_name,
                                'phone_number': phone,
                                'email': email,
                                'address': address,
                                'pickup_date': pickup_date,
                                'pickup_time': pickup_time,
                                'service_type': service_type,
                                'notes': notes
                            })
                            st.success(f"✅ Order Confirmed! Order ID: {order_id}")
                            st.balloons()
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        else:
            # No matching FAQ found
            st.markdown(f"""
            <div style="background: #FCE8E8; padding: 1rem; border-radius: 8px; border-left: 4px solid #C1272D;">
                <p style="color: #C1272D; font-weight: 600;">❌ No matching answer found</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<h2 style='color: {BRAND_COLORS['secondary']};'>Need More Help?</h2>", unsafe_allow_html=True)
            
            with st.form("contact_form"):
                contact_phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567")
                issue = st.text_area("Describe Your Issue")
                
                if st.form_submit_button("Submit Contact"):
                    if contact_phone and issue:
                        st.success("✅ Thank You! We have received your details.")
                        st.info("Our team will contact you shortly or reach us via WhatsApp: +971 50 7738025")
                    else:
                        st.error("Please fill in all fields")
    else:
        # Show all FAQs
        st.markdown("### Browse All FAQs")
        for faq in FAQ_DATA:
            with st.expander(f"❓ {faq['question']}"):
                st.write(faq['answer'])
