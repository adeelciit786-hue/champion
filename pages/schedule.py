"""
Schedule Pickup page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS, SERVICES, get_future_dates, get_time_slots
from database import save_order

def show():
    st.markdown(f"""
    <h1 style="color: {BRAND_COLORS['primary']}; text-align: center; margin-bottom: 2rem;">Schedule Pickup & Delivery</h1>
    """, unsafe_allow_html=True)
    
    # Main layout with sidebar form
    col_form, col_info = st.columns([1.2, 1], gap="large")
    
    with col_form:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FFFFFF, #F0F9FF); padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-left: 6px solid {BRAND_COLORS['primary']}; border-top: 2px solid {BRAND_COLORS['secondary']};">
        """, unsafe_allow_html=True)
        
        with st.form("schedule_pickup_form"):
            # Full Name
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Full Name *</p>", unsafe_allow_html=True)
            full_name = st.text_input("", placeholder="Enter your full name", label_visibility="collapsed", key="full_name")
            
            # Phone
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Phone Number *</p>", unsafe_allow_html=True)
            phone = st.text_input("", placeholder="+971 50 123 4567", label_visibility="collapsed", key="phone_input")
            
            # Email
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Email (Optional)</p>", unsafe_allow_html=True)
            email = st.text_input("", placeholder="your.email@example.com", label_visibility="collapsed", key="email_input")
            
            # Pickup Details Section
            st.markdown(f"<h4 style='color: {BRAND_COLORS['primary']}; margin-top: 1.5rem; margin-bottom: 1rem;'>📍 Pickup Details</h4>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Pickup Address *</p>", unsafe_allow_html=True)
            address = st.text_area("", height=100, placeholder="Enter your complete address", label_visibility="collapsed", key="address_input")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Pickup Date *</p>", unsafe_allow_html=True)
                dates = get_future_dates()
                pickup_date = st.selectbox("", dates, label_visibility="collapsed", key="date_select")
            with col2:
                st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Pickup Time *</p>", unsafe_allow_html=True)
                times = get_time_slots()
                pickup_time = st.selectbox("", times, label_visibility="collapsed", key="time_select")
            
            # Service Details Section
            st.markdown(f"<h4 style='color: {BRAND_COLORS['primary']}; margin-top: 1.5rem; margin-bottom: 1rem;'>🧹 Service Details</h4>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Service Type *</p>", unsafe_allow_html=True)
            service_type = st.selectbox("", SERVICES, label_visibility="collapsed", key="service_select")
            
            st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem; margin-top: 1rem;'>Special Instructions (Optional)</p>", unsafe_allow_html=True)
            notes = st.text_area("", height=80, placeholder="Any special requests? Let us know...", label_visibility="collapsed", key="notes_input")
            
            submitted = st.form_submit_button("✅ Confirm & Schedule Pickup", use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
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
    
    with col_info:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E8F9F3, #F0F9FF); padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-left: 6px solid {BRAND_COLORS['secondary']}; border-top: 2px solid {BRAND_COLORS['primary']}; height: 100%;">
            <h3 style="color: {BRAND_COLORS['primary']}; margin-top: 0;">📋 Service Information</h3>
            
            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 1.5rem;">⏱️ Turnaround Times</h4>
            <p style="color: #555; margin: 0.5rem 0;">
                <strong>Standard:</strong> 2 business days<br>
                <strong>Express:</strong> Next working day (+50%)<br>
                <strong>Wedding Gowns:</strong> 4-6 days<br>
                <strong>Bags:</strong> 7-10 days<br>
                <strong>Shoes:</strong> 5-7 days
            </p>
            
            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 1.5rem;">📍 Coverage Areas</h4>
            <p style="color: #555; margin: 0.5rem 0;">
                ✓ Dubai<br>
                ✓ Abu Dhabi<br>
                ✓ Sharjah<br>
                ✓ Ajman
            </p>
            
            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 1.5rem;">💳 Payment Options</h4>
            <p style="color: #555; margin: 0.5rem 0;">
                Credit/Debit Card at doorstep<br>
                Cash Payment Available
            </p>
            
            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 1.5rem;">✨ Why Choose Us?</h4>
            <p style="color: #555; margin: 0.5rem 0;">
                🚚 Free Pickup & Delivery<br>
                👥 Expert Staff<br>
                🏆 20+ Years Experience<br>
                ✅ Quality Guaranteed
            </p>
        </div>
        """, unsafe_allow_html=True)
