"""
Track Order page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS
from database import get_order

def show():
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary']}, {BRAND_COLORS['secondary']});
                color: white; padding: 2rem; border-radius: 12px; text-align: center;">
        <h1 style="color: white; border: none; margin-top: 0;">📍 Track Your Order</h1>
        <p style="opacity: 0.95; margin: 0;">Enter your order ID or phone number to check your pickup and delivery status</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Search type selection
    search_type = st.radio("🔍 **Search by:**", ("Order ID", "Phone Number"), horizontal=True)
    
    col1, col2 = st.columns([3.5, 1])
    
    with col1:
        st.markdown(f"<p style='color: #333; font-weight: 600; margin-bottom: 0.3rem;'>Enter {search_type}</p>", unsafe_allow_html=True)
        if search_type == "Order ID":
            search_value = st.text_input("", placeholder="e.g., CC20250101ABCD1234", label_visibility="collapsed")
        else:
            search_value = st.text_input("", placeholder="+971 50 123 4567", label_visibility="collapsed")
    
    with col2:
        st.markdown(f"<p style='color: transparent; margin-bottom: 0.3rem;'>.</p>", unsafe_allow_html=True)
        search_button = st.button("🔍 Search", use_container_width=True)
    
    st.markdown("---")
    
    if search_button:
        if not search_value:
            st.warning("⚠️ Please enter a search value")
        else:
            try:
                order = get_order(search_value, search_type.lower().replace(" ", "_"))
                
                if order:
                    # Display order details with professional styling
                    st.success("✅ Order Found!")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {BRAND_COLORS['primary_light']}, white);
                                    padding: 1.5rem; border-radius: 12px;
                                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                                    border-left: 5px solid {BRAND_COLORS['primary']};">
                            <h4 style="color: {BRAND_COLORS['primary']}; margin-top: 0;">📋 Order Details</h4>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Order ID:</strong> <span style="color: {BRAND_COLORS['primary']}; font-weight: 600;">{order['order_id']}</span></p>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Name:</strong> {order['full_name']}</p>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Phone:</strong> {order.get('phone_number', 'N/A')}</p>
                            <p style="margin: 0.5rem 0; color: {BRAND_COLORS['text_light']}; font-size: 0.85rem; margin-top: 1rem;">Order placed on {order.get('created_at', 'N/A')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {BRAND_COLORS['secondary_light']}, white);
                                    padding: 1.5rem; border-radius: 12px;
                                    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                                    border-left: 5px solid {BRAND_COLORS['secondary']};">
                            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 0;">🧹 Service Details</h4>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Service:</strong> {order['service_type']}</p>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Pickup Date:</strong> {order['pickup_date']}</p>
                            <p style="margin: 0.5rem 0;"><strong style="color: {BRAND_COLORS['text_dark']};">Pickup Time:</strong> {order['pickup_time']}</p>
                            <p style="margin: 0.5rem 0; color: {BRAND_COLORS['text_light']}; font-size: 0.85rem; margin-top: 1rem;">Estimated completion: 2-3 business days</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Status tracker
                    st.markdown("---")
                    st.markdown(f"### 📊 Order Status & Timeline")
                    
                    status = order.get('status', 'Pending')
                    status_info = {
                        'Pending': ('🔵', 'Your order is pending confirmation', {BRAND_COLORS['info']}),
                        'Confirmed': ('✅', 'Order confirmed and scheduled', {BRAND_COLORS['primary']}),
                        'Picked Up': ('📦', 'Items have been picked up', {BRAND_COLORS['primary']}),
                        'Processing': ('⚙️', 'Items are being processed', {BRAND_COLORS['warning']}),
                        'Ready': ('🎯', 'Items are ready for delivery', {BRAND_COLORS['success']}),
                        'Delivered': ('✨', 'Items have been delivered', {BRAND_COLORS['success']})
                    }
                    
                    icon, msg, color = status_info.get(status, ('❓', 'Unknown status', {BRAND_COLORS['text_light']}))
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, white, {BRAND_COLORS['primary_light']});
                                padding: 2rem; border-radius: 12px;
                                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                                border-left: 5px solid {BRAND_COLORS['primary']};
                                text-align: center;">
                        <h2 style="color: {BRAND_COLORS['primary']}; border: none; margin-top: 0;">{icon} {status}</h2>
                        <p style="color: {BRAND_COLORS['text_light']}; font-size: 1rem; margin: 0.5rem 0;">{msg}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Timeline
                    st.markdown("---")
                    st.markdown(f"### 📅 Order Timeline")
                    
                    timeline_items = {
                        'Pending': '🔵 Awaiting confirmation',
                        'Confirmed': '🟢 Confirmed - Ready for pickup',
                        'Picked Up': '🟡 Items picked up from your location',
                        'Processing': '🟠 Currently being cleaned/processed',
                        'Ready': '💚 Ready for delivery',
                        'Delivered': '✅ Delivered successfully'
                    }
                    
                    for step, description in timeline_items.items():
                        if step == status:
                            st.markdown(f"<h4 style='color: {BRAND_COLORS['primary']};'>{description} ← Current</h4>", unsafe_allow_html=True)
                        else:
                            st.markdown(description)
                    
                    # Additional actions
                    st.markdown("---")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        if st.button("📞 Contact Support", use_container_width=True):
                            st.info("Call us at: +971 4 2858581 or Toll-Free: 800 4556")
                    
                    with col2:
                        if st.button("💬 Chat on WhatsApp", use_container_width=True):
                            st.info("WhatsApp: +971 50 7738025")
                    
                    with col3:
                        if st.button("🔄 New Search", use_container_width=True):
                            st.rerun()
                
                else:
                    st.error("❌ Order not found. Please check your details and try again.")
                    st.markdown("---")
                    st.markdown("""
                    **Troubleshooting:**
                    - Make sure you entered the correct Order ID or Phone Number
                    - Check if there are any extra spaces in your input
                    - For further assistance, please contact us:
                        - 📞 +971 4 2858581
                        - 📞 Toll-Free: 800 4556
                        - 💬 WhatsApp: +971 50 7738025
                    """)
            
            except Exception as e:
                st.error(f"❌ Error searching for order: {str(e)}")
