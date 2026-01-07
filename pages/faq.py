"""
FAQ page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, FAQ_DATA
from app import search_faq

def show():
    st.markdown(f"### ❓ Frequently Asked Questions")
    st.markdown("Search our FAQs to find answers to common questions about our services.")
    
    st.markdown("---")
    
    # Search Box
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input("Search FAQs...", placeholder="e.g., 'turnaround time', 'bag cleaning', 'babies'")
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    st.markdown("---")
    
    # Display results
    if search_button or search_query:
        if not search_query:
            st.warning("Please enter a search term")
        else:
            result = search_faq(search_query)
            
            if result:
                # Show answer
                with st.container():
                    st.success("✅ Answer Found!")
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #FFFFFF, #F0F9FF); 
                                padding: 20px; border-radius: 10px; border-left: 4px solid {BRAND_COLORS['primary']};">
                        <h4 style="color: {BRAND_COLORS['primary']}; margin-top: 0;">
                            {result['question']}
                        </h4>
                        <p style="color: #333; line-height: 1.6;">
                            {result['answer']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Show schedule form after finding answer
                st.markdown(f"### 📅 Schedule Pickup")
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
