"""
Schedule Pickup page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, SERVICES, get_future_dates, get_time_slots
from database import save_order

def show():
    st.markdown(f"### 📅 Schedule Pickup & Delivery")
    st.markdown("Book your pickup at a time convenient for you. We offer FREE pickup and delivery service!")
    
    st.markdown("---")
    
    with st.form("schedule_pickup_form"):
        st.markdown("#### Your Details")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *")
            phone = st.text_input("Phone Number *", placeholder="+971 50 123 4567")
        with col2:
            email = st.text_input("Email (Optional)")
        
        st.markdown("#### Pickup Details")
        address = st.text_area("Pickup Address *", height=100, placeholder="Enter your complete address")
        
        col1, col2 = st.columns(2)
        with col1:
            dates = get_future_dates()
            pickup_date = st.selectbox("Pickup Date *", dates)
        with col2:
            times = get_time_slots()
            pickup_time = st.selectbox("Pickup Time *", times)
        
        st.markdown("#### Service Details")
        service_type = st.selectbox("Service Type *", SERVICES)
        notes = st.text_area("Special Instructions (Optional)", height=80, placeholder="Any special requests? Let us know...")
        
        submitted = st.form_submit_button("✅ Confirm & Schedule Pickup", use_container_width=True)
        
        if submitted:
            if not full_name or not phone or not address:
                st.error("❌ Please fill in all required fields (*)")
            else:
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
                    
                    # Success message
                    st.success(f"✅ **Order Confirmed!**\n\n**Order ID:** {order_id}")
                    
                    # Show order details
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"""
                        **Your Order Details:**
                        - Name: {full_name}
                        - Service: {service_type}
                        - Date: {pickup_date}
                        - Time: {pickup_time}
                        """)
                    with col2:
                        st.markdown(f"""
                        **Next Steps:**
                        1. Our team will contact you at **{phone}**
                        2. Confirm the pickup time
                        3. We'll arrive for pickup at your scheduled time
                        """)
                    
                    st.info("📱 You can track your order anytime using your Order ID!")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error scheduling pickup: {str(e)}")
    
    # Additional Info
    st.markdown("---")
    st.markdown("### 📋 Service Information")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        **Turnaround Times:**
        - Standard: 2 business days
        - Express: Next working day (+50%)
        - Wedding Gowns: 4-6 days
        - Bags: 7-10 days
        - Shoes: 5-7 days
        """)
    with col2:
        st.markdown(f"""
        **Coverage Areas:**
        - 📍 Dubai
        - 📍 Abu Dhabi
        - 📍 Sharjah
        - 📍 Ajman
        
        **Payment Options:**
        💳 Credit/Debit Card at doorstep
        """)
