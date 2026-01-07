# Champion Cleaners Web Application 🧹

A professional Flask-based web application for Champion Cleaners laundry & dry cleaning service in the UAE.

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/adeelciit786-hue/champion.git
cd champion

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open browser to http://localhost:5000
```

## Features

### 1. 📅 Schedule Pickup & Delivery
- Customer information form with validation
- Date and time selection
- Service type selection
  - Free Pick-up & Delivery
  - Carpet & Upholstery Cleaning
  - Bag & Shoe Spa
  - Permanent Creasing
  - Wedding Gown Restoration
  - Soft Toy Cleaning
  - Alteration Clinique
  - Hanger Amnesty
  - Hygienizing & Sanitizing Service
  - Wash & Fold Service
- **Input Validation**: Real-time validation for phone numbers, email, dates, and addresses
- **Order Confirmation**: Automated confirmation with Order ID and booking details
- **Offer Integration**: Display applicable offers during scheduling

### 2. 📍 Track Order
- **Dual Search Methods**: 
  - Search by Order ID
  - Search by Phone Number
- **Order Details**: Display customer name, service type, pickup date, and status
- **Team Notification**: Automatic logging for follow-up on unfound orders
- **Professional Feedback**: Helpful messages whether order is found or not

### 3. ❓ FAQ & Information Retrieval
- **Intelligent Search**: Keyword-based matching system for customer questions
- **Comprehensive FAQ Database**: 20+ FAQs covering:
  - Service information (turnaround times, coverage areas, pricing)
  - Cleaning techniques (delicate items, stains, wedding gowns)
  - Special services (bag spa, sanitizing, alterations)
  - Account & ordering help
- **Confidence Scoring**: Only shows answers with sufficient confidence match
- **Related Questions**: Suggests related FAQs when user's question matches
- **Fallback Support**: Logs unanswered questions for team follow-up

### 4. 🎉 Offers & Promotions
- **Dynamic Offer Management**: Display active, date-validated offers
- **Tiered Eligibility**: Target offers by audience (new customers, returning, all)
- **Promotion Types**: Support for percentage discounts, fixed amount discounts, or special services
- **Email Subscription**: Allow customers to subscribe for offer notifications
- **Team Notifications**: Track subscription requests for marketing follow-up

## Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Python web framework for rapid UI development
- **Backend**: SQLite - Lightweight local database for orders and offers
- **Language**: Python 3.8+
- **Styling**: Custom HTML/CSS with Champion Cleaners brand colors

## Project Structure

```
champion-bot/
├── app.py                 # Main Streamlit application (all 4 features)
├── config.py             # Configuration, constants, and brand colors
├── backend.py            # Database operations (SQLite)
├── faq_data.py           # FAQ data and retrieval system
├── utils.py              # Validation and utility functions
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── champion_orders.db    # Orders database (auto-created)
└── champion_offers.db    # Offers database (auto-created)
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download
```bash
cd "path/to/Champion bot"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Configuration

### Brand Customization

Edit `config.py` to customize:

```python
BRAND_COLORS = {
    "primary": "#1a3a52",      # Deep blue
    "secondary": "#e74c3c",    # Red accent
    "accent": "#f39c12",       # Gold accent
    # ... other colors
}

SERVICES = [
    "Free Pick-up & Delivery",
    "Carpet & Upholstery Cleaning",
    # ... other services
]

COVERAGE_AREAS = [
    "Dubai",
    "Abu Dhabi",
    # ... other areas
]
```

### Contact Information

Update contact details in `config.py`:

```python
PHONE = "+971 4 XXX XXXX"
EMAIL = "info@champion-cleaners.com"
WEBSITE = "https://www.champion-cleaners.com"
```

### Database Paths

By default, databases are created in the application directory:
- `champion_orders.db` - Customer orders and notifications
- `champion_offers.db` - Active promotions

To change paths, modify `config.py`:

```python
DB_PATH = "custom/path/champion_orders.db"
OFFERS_DB_PATH = "custom/path/champion_offers.db"
```

## Deployment

### Streamlit Community Cloud (Recommended)

1. **Prepare Your Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo>
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [Streamlit Community Cloud](https://share.streamlit.io/)
   - Sign in with GitHub account
   - Click "New app"
   - Select your repository, branch, and `app.py` as main file
   - Click "Deploy"

3. **Environment Variables (if needed)**
   - Go to app settings
   - Add secrets in the "Secrets" section if using API keys

### Local Server (Self-Hosted)

```bash
# Using Streamlit's built-in server
streamlit run app.py --server.port 8501

# Using Gunicorn (production)
pip install gunicorn
gunicorn --workers 4 "streamlit.web.cli:_main_run_clsSomeClass" app.py
```

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:

```bash
docker build -t champion-cleaners-bot .
docker run -p 8501:8501 champion-cleaners-bot
```

## Database Schema

### Orders Table

| Column | Type | Description |
|--------|------|-------------|
| order_id | TEXT (PK) | Unique order identifier (e.g., CC20250101ABCD1234) |
| full_name | TEXT | Customer full name |
| phone_number | TEXT | Customer contact number |
| email | TEXT | Customer email (optional) |
| pickup_address | TEXT | Delivery address |
| pickup_date | TEXT | Scheduled pickup date (YYYY-MM-DD) |
| pickup_time | TEXT | Scheduled pickup time (HH:MM) |
| service_type | TEXT | Type of service selected |
| status | TEXT | Order status (Scheduled, Confirmed, Completed) |
| created_at | TIMESTAMP | Order creation timestamp |
| notes | TEXT | Special instructions/notes |

### Notifications Table

| Column | Type | Description |
|--------|------|-------------|
| notification_id | INTEGER (PK) | Auto-increment ID |
| order_id | TEXT (FK) | Associated order ID |
| phone_number | TEXT | Customer phone |
| query_type | TEXT | Type of query (track_order, faq_unanswered, etc.) |
| message | TEXT | Notification message |
| created_at | TIMESTAMP | Notification timestamp |

### Offers Table

| Column | Type | Description |
|--------|------|-------------|
| offer_id | INTEGER (PK) | Auto-increment ID |
| offer_name | TEXT | Offer title |
| description | TEXT | Offer description |
| discount_percent | REAL | Percentage discount (optional) |
| discount_amount | REAL | Fixed amount discount (optional) |
| valid_from | TEXT | Start date (YYYY-MM-DD) |
| valid_to | TEXT | End date (YYYY-MM-DD) |
| target_audience | TEXT | Audience filter (new_customers, returning, all) |
| active | BOOLEAN | Active/inactive flag |
| created_at | TIMESTAMP | Creation timestamp |

## Usage Examples

### Scheduling a Pickup

1. Click "Schedule Pickup" from main menu
2. Enter customer details (name, phone, address)
3. Select pickup date and time from dropdowns
4. Choose service type
5. Add optional special instructions
6. Click "Confirm & Schedule Pickup"
7. Receive Order ID and confirmation

### Tracking an Order

1. Click "Track Order" from main menu
2. Choose search method (Order ID or Phone Number)
3. Enter search details
4. View order status and details

### Finding FAQ Answers

1. Click "FAQs & Information"
2. Type your question (e.g., "How long does dry cleaning take?")
3. Click "Find Answer"
4. View relevant answer and related questions

### Viewing Current Offers

1. Click "Current Offers"
2. Browse all active promotions
3. Subscribe for notifications
4. Offers auto-apply during scheduling when eligible

## Input Validation

The application includes comprehensive validation:

- **Phone Numbers**: Accepts UAE formats (+971, 0, 971 prefixes)
- **Emails**: Standard email format validation
- **Names**: 3-100 characters, letters/spaces/hyphens only
- **Addresses**: 5-200 characters
- **Pickup Dates**: 24 hours to 30 days in future
- **Pickup Times**: Valid HH:MM format (08:00 - 20:00)

All invalid inputs show helpful error messages guiding users to correct format.

## Error Handling

The application includes robust error handling for:

- Missing required fields
- Invalid input formats
- Database connection issues
- File system errors
- Graceful degradation when offers/notifications unavailable

## Customization Guide

### Adding New Services

1. Edit `config.py`:
   ```python
   SERVICES = [
       # ... existing services
       "Your New Service"
   ]
   ```

2. Update FAQs in `faq_data.py` if needed

### Adding New Offers

Offers are auto-created on first run. To add more:

1. Use the backend function:
   ```python
   from backend import add_offer
   
   add_offer(
       offer_name="Super Summer Sale",
       description="30% off all services",
       discount_percent=30,
       discount_amount=None,
       valid_from="2025-06-01",
       valid_to="2025-08-31",
       target_audience="all"
   )
   ```

2. Or manually edit `champion_offers.db` using SQLite tools

### Updating FAQ Content

Edit `faq_data.py` FAQ_DATA list:

```python
FAQ_DATA = [
    {
        "question": "Your question?",
        "answer": "Your detailed answer...",
        "keywords": ["keyword1", "keyword2"]
    },
    # ... more FAQs
]
```

## Modular Architecture

The codebase is designed for easy integration with external systems:

### Using Backend Functions Separately

```python
from backend import save_order, get_order, get_active_offers

# Save an order programmatically
success, order_id = save_order(
    full_name="John Doe",
    phone_number="+971501234567",
    email="john@example.com",
    pickup_address="123 Main St, Dubai",
    pickup_date="2025-01-25",
    pickup_time="14:30",
    service_type="Dry Cleaning"
)

# Retrieve an order
order = get_order(order_id=order_id)

# Get active offers
offers = get_active_offers(target_audience="all")
```

### Using FAQ System

```python
from faq_data import retrieve_faq_answer, search_faq

# Get best match for a question
question, answer, confidence = retrieve_faq_answer("How long does cleaning take?")

# Search for multiple matches
results = search_faq("carpet cleaning")
```

### Using Validation

```python
from utils import validate_phone_number, validate_email

is_valid, error_msg = validate_phone_number("+971501234567")
is_valid, error_msg = validate_email("user@example.com")
```

## Future Enhancements

These modules are designed to support:

- **WhatsApp Integration**: Reuse backend and FAQ functions for WhatsApp messaging
- **Email Notifications**: Send order confirmations and updates via email
- **Google Sheets Backend**: Replace SQLite with Google Sheets for cloud sync
- **SMS Notifications**: Send OTP or order updates via SMS
- **Admin Dashboard**: Add admin page for managing orders and offers
- **Analytics**: Track user interactions and popular queries
- **Multi-language Support**: Add Arabic language support
- **Payment Integration**: Process online payments (Stripe, PayPal)

## Security Considerations

- **Input Validation**: All user inputs are validated before storage
- **Error Messages**: Generic errors shown to users; detailed logs kept for debugging
- **Database**: SQLite is local; for production, consider encrypted cloud database
- **API Keys**: Keep all API keys in environment variables (not committed to repo)
- **Deployment**: Use HTTPS in production

## Troubleshooting

### Port Already in Use
```bash
# Streamlit uses port 8501 by default
streamlit run app.py --server.port 8502
```

### Database Locked
- Close other connections to the database
- Delete `.streamlit/` cache: `rm -rf .streamlit/`

### Module Not Found
```bash
# Ensure you're in the correct directory
cd "path/to/Champion bot"
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Styling Not Applied
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

## Performance Notes

- **Database Size**: SQLite handles up to 100K orders efficiently
- **FAQ Retrieval**: Keyword matching is O(n) but fast for <50 FAQs
- **Concurrent Users**: Streamlit single-threaded; consider deployment options for scaling

For high-traffic deployments, consider:
- Load balancing with multiple instances
- Dedicated database server (PostgreSQL/MySQL)
- Caching layer (Redis)
- Separate API backend

## Support & Maintenance

### Backup Database

```bash
# Windows
copy champion_orders.db champion_orders.db.backup

# macOS/Linux
cp champion_orders.db champion_orders.db.backup
```

### View All Orders

```python
from backend import get_all_orders

orders = get_all_orders()
for order in orders:
    print(f"{order['order_id']}: {order['full_name']}")
```

### Check Team Notifications

```python
from backend import get_notifications

notifications = get_notifications()
for notif in notifications:
    print(f"{notif['query_type']}: {notif['message']}")
```

## License

This application is proprietary to Champion Cleaners. All rights reserved.

## Contact & Support

For questions, bug reports, or feature requests:

- **Phone**: +971 4 XXX XXXX
- **Email**: info@champion-cleaners.com
- **Website**: https://www.champion-cleaners.com

---

**Champion Cleaners © 2025**  
*Your Trusted Laundry & Dry Cleaning Partner in the UAE*
