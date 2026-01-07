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
        search_query = st.text_input("Search FAQ...", placeholder="e.g., 'turnaround time', 'bag cleaning', 'babies'", key="faq_search")
    with col2:
        search_button = st.button("Search", use_container_width=True)
    
    # Display search results or all FAQs
    if search_button and search_query:
        result = search_faq(search_query)
        
        if result:
            # Found matching FAQ
            st.markdown(f"""
            <div style="background: #E8F9F3; padding: 1rem; border-radius: 8px; border-left: 4px solid #00A651; margin: 1rem 0;">
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
            
            # Schedule form after finding answer
            st.markdown(f"""
            <h2 style="color: {BRAND_COLORS['primary']}; margin-bottom: 1rem;">Schedule Pickup Now</h2>
            """, unsafe_allow_html=True)
            
            with st.form("schedule_form_faq"):
                col1, col2 = st.columns(2)
                with col1:
                    full_name = st.text_input("Full Name *", key="faq_name")
                with col2:
                    phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567", key="faq_phone")
                
                email = st.text_input("Email (Optional)", placeholder="your@email.com", key="faq_email")
                address = st.text_area("Pickup Address *", placeholder="Enter your full address", key="faq_address")
                
                col3, col4 = st.columns(2)
                with col3:
                    dates = get_future_dates(30)
                    pickup_date = st.selectbox("Pickup Date *", options=dates, key="faq_date")
                with col4:
                    times = get_time_slots()
                    pickup_time = st.selectbox("Pickup Time *", options=times, key="faq_time")
                
                service_type = st.selectbox("Service Type *", options=SERVICES, key="faq_service")
                notes = st.text_area("Special Instructions (Optional)", placeholder="Any special requests?", key="faq_notes")
                
                if st.form_submit_button("Confirm & Schedule Pickup", use_container_width=True):
                    if not full_name or not phone or not address:
                        st.error("Please fill in all required fields")
                    else:
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
                        st.success(f"✓ Order Confirmed! Order ID: {order_id}. Our team will contact you shortly.")
                        st.balloons()
        
        else:
            # No matching FAQ found
            st.markdown(f"""
            <div style="background: #FCE8E8; padding: 1rem; border-radius: 8px; border-left: 4px solid #C1272D; margin: 1rem 0;">
                <p style="color: #C1272D; font-weight: 600;">❌ No matching answer found</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <h2 style="color: {BRAND_COLORS['secondary']}; margin-bottom: 1rem;">Need More Help?</h2>
            <p style="color: #555; margin-bottom: 1.5rem;">Please share your contact number and your issue, and our team will get back to you shortly.</p>
            """, unsafe_allow_html=True)
            
            with st.form("contact_form"):
                contact_phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567")
                issue = st.text_area("Describe Your Issue", placeholder="Tell us more about your question")
                
                if st.form_submit_button("Submit Contact", use_container_width=True):
                    if contact_phone and issue:
                        st.success("✓ Thank You! We have received your contact details and issue description.")
                        st.info(f"Our team will get in touch with you shortly. Alternatively, you can reach us directly via [WhatsApp](https://wa.me/971507738025)")
                    else:
                        st.error("Please fill in all fields")
    
    else:
        # Show all FAQs
        st.markdown("### Browse All FAQs")
        
        for faq in FAQ_DATA:
            with st.expander(f"❓ {faq['question']}", expanded=False):
                st.markdown(f"""
                <div style="color: #555; line-height: 1.6;">
                    {faq['answer']}
                </div>
                """, unsafe_allow_html=True)
                st.markdown("Ready to get your items cleaned? Fill in the details below:")
                
                with st.form("schedule_from_faq"):
                    col1, col2 = st.columns(2)
                    with col1:
                        full_name = st.text_input("Full Name *", key="faq_name")
                        phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567", key="faq_phone")
                    with col2:
                        email = st.text_input("Email (Optional)", key="faq_email")
                        address = st.text_area("Pickup Address *", height=80, key="faq_address")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        from config import get_future_dates, get_time_slots
                        dates = get_future_dates()
                        times = get_time_slots()
                        pickup_date = st.selectbox("Pickup Date *", dates, key="faq_date")
                        service_type = st.selectbox("Service Type *", 
                                                    ["Bag & Shoes Spa", "Wedding Gown", "Mattress Cleaning", 
                                                     "Soft Toy Cleaning", "Stroller & Car Seat", "Super Crease", 
                                                     "Alterations"], key="faq_service")
                    with col2:
                        pickup_time = st.selectbox("Pickup Time *", times, key="faq_time")
                        notes = st.text_area("Special Instructions (Optional)", key="faq_notes")
                    
                    submitted = st.form_submit_button("✅ Confirm & Schedule Pickup", use_container_width=True)
                    
                    if submitted:
                        if not full_name or not phone or not address:
                            st.error("Please fill in all required fields (*)")
                        else:
                            from database import save_order
                            try:
                                order_id = save_order(
                                    full_name=full_name,
                                    phone_number=phone,
                                    email=email,
                                    address=address,
                                    pickup_date=pickup_date,
                                    pickup_time=pickup_time,
                                    service_type=service_type,
                                    notes=notes
                                )
                                st.success(f"✅ Order Confirmed! Order ID: **{order_id}**\n\nOur team will contact you shortly to confirm the pickup details.")
                                st.balloons()
                            except Exception as e:
                                st.error(f"Error scheduling pickup: {str(e)}")
            else:
                st.error("❌ No matching answer found. Please try a different search term.")
                
                st.markdown("---")
                st.markdown(f"### 📞 Let us take this forward for you")
                st.markdown("Kindly share your contact details and we'll get back to you soon.")
                
                with st.form("contact_form"):
                    phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567")
                    issue = st.text_area("Describe your query *", placeholder="Tell us about your question...")
                    
                    submitted = st.form_submit_button("📤 Submit", use_container_width=True)
                    
                    if submitted:
                        if not phone or not issue:
                            st.error("Please fill in all fields")
                        else:
                            from database import log_notification
                            try:
                                log_notification(phone, f"Unanswered FAQ: {issue}", "faq_contact")
                                st.success("✅ Thank you! We've received your details. Our team will contact you shortly.")
                                st.info("You can also reach us via WhatsApp: +971 50 7738025")
                            except Exception as e:
                                st.error(f"Error submitting form: {str(e)}")
    else:
        # Show all FAQs
        st.markdown(f"### All FAQs ({len(FAQ_DATA)})")
        
        for idx, faq in enumerate(FAQ_DATA):
            with st.expander(faq['question']):
                st.write(faq['answer'])
