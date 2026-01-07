"""
FAQ page for Champion Cleaners - Matches Flask template exactly
"""

import streamlit as st
from config import BRAND_COLORS, FAQ_DATA, get_future_dates, get_time_slots, SERVICES
from utils import search_faq
from database import save_order

def show():
    st.markdown(f"""
    <h1 style="color: {BRAND_COLORS['primary']}; text-align: center; margin-bottom: 2rem;">Frequently Asked Questions</h1>
    """, unsafe_allow_html=True)
    
    # Search Box with professional styling
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.5rem;'>🔍 Search FAQ</p>", unsafe_allow_html=True)
        search_query = st.text_input("", placeholder="e.g., 'turnaround time', 'bag cleaning'", label_visibility="collapsed", key="faq_search")
    with col2:
        st.markdown(f"<p style='color: transparent; font-weight: 600; margin-bottom: 0.5rem;'>.</p>", unsafe_allow_html=True)
        search_button = st.button("🔍 Search", use_container_width=True)
    
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
            st.markdown(f"<h2 style='color: {BRAND_COLORS['primary']};'>📅 Schedule Pickup Now</h2>", unsafe_allow_html=True)
            
            with st.form("schedule_form_faq"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Full Name *</p>", unsafe_allow_html=True)
                    full_name = st.text_input("", placeholder="Enter your full name", label_visibility="collapsed", key="faq_name")
                with col2:
                    st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Phone Number *</p>", unsafe_allow_html=True)
                    phone = st.text_input("", placeholder="+971 50 123 4567", label_visibility="collapsed", key="faq_phone")
                
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Email (Optional)</p>", unsafe_allow_html=True)
                email = st.text_input("", placeholder="your.email@example.com", label_visibility="collapsed", key="faq_email")
                
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Pickup Address *</p>", unsafe_allow_html=True)
                address = st.text_area("", placeholder="Enter your full address", label_visibility="collapsed", key="faq_address", height=80)
                
                col3, col4 = st.columns(2)
                with col3:
                    st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Pickup Date *</p>", unsafe_allow_html=True)
                    dates = get_future_dates(30)
                    pickup_date = st.selectbox("", options=dates, label_visibility="collapsed", key="faq_date")
                with col4:
                    st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Pickup Time *</p>", unsafe_allow_html=True)
                    times = get_time_slots()
                    pickup_time = st.selectbox("", options=times, label_visibility="collapsed", key="faq_time")
                
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Service Type *</p>", unsafe_allow_html=True)
                service_type = st.selectbox("", options=SERVICES, label_visibility="collapsed", key="faq_service")
                
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Special Instructions (Optional)</p>", unsafe_allow_html=True)
                notes = st.text_area("", placeholder="Any special requests? Let us know...", label_visibility="collapsed", key="faq_notes", height=80)
                
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
                <p style="color: #C1272D; font-weight: 600;">❌ No matching answer was found. Please try refining your search or fill in your contact details below, and our team will get in touch with you.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<h2 style='color: {BRAND_COLORS['secondary']};'>Need More Help?</h2>", unsafe_allow_html=True)
            
            with st.form("contact_form"):
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Phone Number *</p>", unsafe_allow_html=True)
                contact_phone = st.text_input("", placeholder="+971 50 123 4567", label_visibility="collapsed", key="contact_phone")
                
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Describe Your Issue</p>", unsafe_allow_html=True)
                issue = st.text_area("", placeholder="Tell us what you need help with...", label_visibility="collapsed", key="contact_issue", height=100)
                
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
