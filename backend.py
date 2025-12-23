"""
Backend database operations for Champion Cleaners orders and offers
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import os
from config import DB_PATH, OFFERS_DB_PATH


def init_orders_db():
    """Initialize orders database with required tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT,
            pickup_address TEXT NOT NULL,
            pickup_date TEXT NOT NULL,
            pickup_time TEXT NOT NULL,
            service_type TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            notes TEXT
        )
    """)
    
    # Team notifications table for tracking attempts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,
            phone_number TEXT,
            query_type TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (order_id) REFERENCES orders (order_id)
        )
    """)
    
    conn.commit()
    conn.close()


def init_offers_db():
    """Initialize offers database."""
    conn = sqlite3.connect(OFFERS_DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS offers (
            offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            offer_name TEXT NOT NULL,
            description TEXT NOT NULL,
            discount_percent REAL,
            discount_amount REAL,
            valid_from TEXT NOT NULL,
            valid_to TEXT NOT NULL,
            target_audience TEXT,
            active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Seed with sample offers
    cursor.execute("SELECT COUNT(*) FROM offers")
    if cursor.fetchone()[0] == 0:
        sample_offers = [
            ("New Customer Welcome", "20% off your first order", 20, None, "2025-01-01", "2025-12-31", "new_customers"),
            ("Winter Special", "Free sanitizing with any order", None, 0, "2025-01-01", "2025-02-28", "all"),
            ("Loyalty Reward", "15% off for returning customers", 15, None, "2025-01-01", "2025-12-31", "returning"),
        ]
        
        for offer in sample_offers:
            cursor.execute("""
                INSERT INTO offers (offer_name, description, discount_percent, discount_amount, 
                                   valid_from, valid_to, target_audience)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, offer)
    
    conn.commit()
    conn.close()


def generate_order_id() -> str:
    """Generate a unique order ID."""
    import uuid
    return f"CC{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:8].upper()}"


def save_order(full_name: str, phone_number: str, email: Optional[str],
               pickup_address: str, pickup_date: str, pickup_time: str,
               service_type: str, notes: Optional[str] = None) -> Tuple[bool, str]:
    """
    Save a new order to the database.
    
    Returns:
        Tuple of (success, order_id or error_message)
    """
    try:
        init_orders_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        order_id = generate_order_id()
        
        cursor.execute("""
            INSERT INTO orders 
            (order_id, full_name, phone_number, email, pickup_address, 
             pickup_date, pickup_time, service_type, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (order_id, full_name, phone_number, email, pickup_address,
              pickup_date, pickup_time, service_type, notes))
        
        conn.commit()
        conn.close()
        
        return (True, order_id)
    
    except Exception as e:
        return (False, f"Database error: {str(e)}")


def get_order(order_id: Optional[str] = None, phone_number: Optional[str] = None) -> Optional[Dict]:
    """
    Retrieve an order by order_id or phone_number.
    
    Returns:
        Order dictionary or None if not found
    """
    try:
        if not os.path.exists(DB_PATH):
            return None
        
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if order_id:
            cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        elif phone_number:
            cursor.execute("SELECT * FROM orders WHERE phone_number = ? ORDER BY created_at DESC LIMIT 1", 
                          (phone_number,))
        else:
            conn.close()
            return None
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    except Exception as e:
        print(f"Error retrieving order: {str(e)}")
        return None


def get_all_orders() -> List[Dict]:
    """Get all orders from database."""
    try:
        if not os.path.exists(DB_PATH):
            return []
        
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    except Exception as e:
        print(f"Error retrieving orders: {str(e)}")
        return []


def update_order_status(order_id: str, status: str) -> bool:
    """Update order status."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE orders SET status = ? WHERE order_id = ?", 
                      (status, order_id))
        
        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        print(f"Error updating order: {str(e)}")
        return False


def log_notification(order_id: Optional[str], phone_number: str, 
                    query_type: str, message: str) -> bool:
    """
    Log a team notification for manual follow-up.
    
    Args:
        order_id: Optional order ID
        phone_number: Customer phone number
        query_type: Type of query (track_order, contact_request, etc.)
        message: Notification message
        
    Returns:
        Success status
    """
    try:
        init_orders_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO notifications (order_id, phone_number, query_type, message)
            VALUES (?, ?, ?, ?)
        """, (order_id, phone_number, query_type, message))
        
        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        print(f"Error logging notification: {str(e)}")
        return False


def get_notifications(limit: int = 50) -> List[Dict]:
    """Get recent notifications for team review."""
    try:
        if not os.path.exists(DB_PATH):
            return []
        
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM notifications 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (limit,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    except Exception as e:
        print(f"Error retrieving notifications: {str(e)}")
        return []


# Offers database functions

def get_active_offers(target_audience: Optional[str] = None) -> List[Dict]:
    """
    Get active offers, optionally filtered by target audience.
    
    Args:
        target_audience: Filter by target audience (new_customers, returning, all, etc.)
        
    Returns:
        List of active offers
    """
    try:
        init_offers_db()
        if not os.path.exists(OFFERS_DB_PATH):
            return []
        
        conn = sqlite3.connect(OFFERS_DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        query = """
            SELECT * FROM offers 
            WHERE active = 1 
            AND valid_from <= ? 
            AND valid_to >= ?
        """
        params = [today, today]
        
        if target_audience:
            query += " AND (target_audience = ? OR target_audience = 'all')"
            params.append(target_audience)
        
        query += " ORDER BY offer_name"
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    except Exception as e:
        print(f"Error retrieving offers: {str(e)}")
        return []


def add_offer(offer_name: str, description: str, discount_percent: Optional[float],
             discount_amount: Optional[float], valid_from: str, valid_to: str,
             target_audience: str = "all") -> bool:
    """Add a new offer."""
    try:
        init_offers_db()
        conn = sqlite3.connect(OFFERS_DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO offers 
            (offer_name, description, discount_percent, discount_amount, 
             valid_from, valid_to, target_audience)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (offer_name, description, discount_percent, discount_amount,
              valid_from, valid_to, target_audience))
        
        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        print(f"Error adding offer: {str(e)}")
        return False


# Initialize databases on import
if not os.path.exists(DB_PATH):
    init_orders_db()
if not os.path.exists(OFFERS_DB_PATH):
    init_offers_db()
