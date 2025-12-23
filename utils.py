"""
Utility functions for Champion Cleaners Assistant
"""

import re
from datetime import datetime, timedelta
from typing import Tuple, Optional


def validate_phone_number(phone: str) -> Tuple[bool, str]:
    """
    Validate UAE phone number format.
    
    Args:
        phone: Phone number to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Remove spaces and special characters
    phone_clean = re.sub(r'[^\d+]', '', phone)
    
    # UAE phone patterns: +971XXXXXXXXX or 0501234567 or 971501234567
    uae_patterns = [
        r'^\+971\d{9}$',     # +971 format
        r'^0\d{9}$',         # 0 format
        r'^971\d{9}$'        # 971 format
    ]
    
    for pattern in uae_patterns:
        if re.match(pattern, phone_clean):
            return (True, "")
    
    return (False, "Please enter a valid UAE phone number (e.g., +971501234567 or 0501234567)")


def validate_email(email: str) -> Tuple[bool, str]:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return (True, "")
    return (False, "Please enter a valid email address")


def validate_pickup_date(date_str: str) -> Tuple[bool, str]:
    """
    Validate pickup date (must be in future and not more than 30 days away).
    
    Args:
        date_str: Date string in format YYYY-MM-DD
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        pickup_date = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.now()
        
        # Must be at least 24 hours in future
        min_date = today + timedelta(hours=24)
        if pickup_date < min_date:
            return (False, "Pickup date must be at least 24 hours in the future")
        
        # Must not be more than 30 days in future
        max_date = today + timedelta(days=30)
        if pickup_date > max_date:
            return (False, "Pickup date must be within 30 days")
        
        return (True, "")
    
    except ValueError:
        return (False, "Please enter a valid date (YYYY-MM-DD)")


def validate_pickup_time(time_str: str) -> Tuple[bool, str]:
    """
    Validate pickup time format.
    
    Args:
        time_str: Time string in format HH:MM (24-hour)
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        datetime.strptime(time_str, "%H:%M")
        return (True, "")
    except ValueError:
        return (False, "Please enter time in HH:MM format (24-hour, e.g., 14:30)")


def validate_full_name(name: str) -> Tuple[bool, str]:
    """Validate full name."""
    name = name.strip()
    if len(name) < 3:
        return (False, "Name must be at least 3 characters")
    if len(name) > 100:
        return (False, "Name must not exceed 100 characters")
    if not re.match(r"^[a-zA-Z\s\-']+$", name):
        return (False, "Name can only contain letters, spaces, hyphens, and apostrophes")
    return (True, "")


def validate_address(address: str) -> Tuple[bool, str]:
    """Validate pickup address."""
    address = address.strip()
    if len(address) < 5:
        return (False, "Address must be at least 5 characters")
    if len(address) > 200:
        return (False, "Address must not exceed 200 characters")
    return (True, "")


def format_phone_for_display(phone: str) -> str:
    """Format phone number for display."""
    phone_clean = re.sub(r'[^\d+]', '', phone)
    if phone_clean.startswith('+971'):
        return phone_clean
    elif phone_clean.startswith('0'):
        return '+971' + phone_clean[1:]
    elif phone_clean.startswith('971'):
        return '+' + phone_clean
    return phone


def get_future_dates(days: int = 30) -> list:
    """Get list of valid future dates for date picker."""
    dates = []
    today = datetime.now()
    start_date = today + timedelta(days=1)
    
    for i in range(days):
        date = start_date + timedelta(days=i)
        dates.append(date.strftime("%Y-%m-%d"))
    
    return dates


def get_time_slots(interval_minutes: int = 30) -> list:
    """Get list of time slots for pickup."""
    slots = []
    hour = 8  # Start at 8 AM
    minute = 0
    
    while hour < 20:  # End at 8 PM
        time_str = f"{hour:02d}:{minute:02d}"
        slots.append(time_str)
        
        minute += interval_minutes
        if minute >= 60:
            minute = 0
            hour += 1
    
    return slots


def get_greeting_message(hour: Optional[int] = None) -> str:
    """Get time-appropriate greeting."""
    if hour is None:
        hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning! 🌅"
    elif hour < 17:
        return "Good afternoon! ☀️"
    else:
        return "Good evening! 🌙"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to maximum length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def log_user_interaction(interaction_type: str, data: dict) -> None:
    """
    Log user interactions for analytics (placeholder for future enhancement).
    
    Args:
        interaction_type: Type of interaction (schedule, track, faq, etc.)
        data: Interaction data
    """
    timestamp = datetime.now().isoformat()
    # In future: send to analytics service or log file
    pass
