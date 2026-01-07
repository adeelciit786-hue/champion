"""
Database operations for Champion Cleaners
"""

import sqlite3
import os
from datetime import datetime
from config import DB_PATH

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT,
            address TEXT NOT NULL,
            pickup_date TEXT NOT NULL,
            pickup_time TEXT NOT NULL,
            service_type TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Notifications table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT,
            message TEXT,
            query_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

def save_order(full_name, phone_number, email, address, pickup_date, pickup_time, service_type, notes):
    """Save a new order."""
    try:
        init_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        import uuid
        order_id = f"CC{datetime.now().strftime('%Y%m%d')}{uuid.uuid4().hex[:8].upper()}"
        
        cursor.execute("""
            INSERT INTO orders (order_id, full_name, phone_number, email, address, 
                              pickup_date, pickup_time, service_type, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (order_id, full_name, phone_number, email, address, 
              pickup_date, pickup_time, service_type, notes))
        
        conn.commit()
        conn.close()
        
        return {"success": True, "order_id": order_id}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_order(order_id=None, phone_number=None):
    """Get an order by ID or phone number."""
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
            return None
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return dict(result)
        return None
    except Exception as e:
        return None

def log_notification(phone_number, message, query_type):
    """Log a notification for team follow-up."""
    try:
        init_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO notifications (phone_number, message, query_type)
            VALUES (?, ?, ?)
        """, (phone_number, message, query_type))
        
        conn.commit()
        conn.close()
        return True
    except:
        return False
