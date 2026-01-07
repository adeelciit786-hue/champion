"""
Track Order page for Champion Cleaners
"""

import streamlit as st
from config import BRAND_COLORS
from database import get_order

def show():
    st.markdown(f"### 📍 Track Your Order")
    st.markdown("Enter your order ID or phone number to track your pickup and delivery status.")
    
    st.markdown("---")
    
    # Search type selection
    search_type = st.radio("Search by:", ("Order ID", "Phone Number"), horizontal=True)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        if search_type == "Order ID":
            search_value = st.text_input("Enter Order ID", placeholder="e.g., CC20250101ABCD1234")
        else:
            search_value = st.text_input("Enter Phone Number", placeholder="+971 50 123 4567")
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    st.markdown("---")
    
    if search_button:
        if not search_value:
            st.warning("⚠️ Please enter a search value")
        else:
            try:
                order = get_order(search_value, search_type.lower().replace(" ", "_"))
                
                if order:
                    # Display order details
                    st.success("✅ Order Found!")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"""
                        <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid {BRAND_COLORS['primary']};">
                            <h4 style="color: {BRAND_COLORS['primary']}; margin-top: 0;">Order Details</h4>
                            <p><strong>Order ID:</strong> {order['order_id']}</p>
                            <p><strong>Name:</strong> {order['full_name']}</p>
                            <p><strong>Phone:</strong> {order.get('phone_number', 'N/A')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid {BRAND_COLORS['secondary']};">
                            <h4 style="color: {BRAND_COLORS['secondary']}; margin-top: 0;">Service Details</h4>
                            <p><strong>Service:</strong> {order['service_type']}</p>
                            <p><strong>Date:</strong> {order['pickup_date']}</p>
                            <p><strong>Time:</strong> {order['pickup_time']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Status tracker
                    st.markdown("---")
                    st.markdown(f"### 📊 Order Status")
                    
                    status = order.get('status', 'Pending')
                    status_colors = {
                        'Pending': '🔵',
                        'Confirmed': '🟢',
                        'Picked Up': '🟡',
                        'Processing': '🟠',
                        'Ready': '💚',
                        'Delivered': '✅'
                    }
                    
                    st.markdown(f"**Current Status:** {status_colors.get(status, '❓')} {status}")
                    
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
