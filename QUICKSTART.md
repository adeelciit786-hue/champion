# ⚡ Quick Start Guide - Champion Cleaners Streamlit App

## 🎯 5-Minute Setup

### Step 1: Clone Repository (1 minute)
```bash
git clone https://github.com/adeelciit786-hue/champion.git
cd champion
```

### Step 2: Install Dependencies (2 minutes)
```bash
# On Windows
pip install -r requirements.txt

# On Mac/Linux
pip3 install -r requirements.txt
```

### Step 3: Run Application (1 minute)
```bash
streamlit run streamlit_app.py
```

### Step 4: Open Browser
```
http://localhost:8501
```

**✅ Done! Your app is now running!**

---

## 🚀 Deploying to Production

### Option 1: Streamlit Cloud (Easiest - Free)
1. Visit https://streamlit.io/cloud
2. Click "New App"
3. Select repository: `champion`
4. Branch: `master`
5. Main file: `streamlit_app.py`
6. Click "Deploy"

**Your app is live in 2 minutes!**
URL: `https://your-username-champion.streamlit.app`

### Option 2: Heroku (10 minutes)
```bash
# 1. Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# 2. Create runtime.txt
echo "python-3.11.5" > runtime.txt

# 3. Login to Heroku
heroku login

# 4. Create and deploy
heroku create champion-cleaners
git push heroku master

# 5. Open app
heroku open
```

### Option 3: Docker (15 minutes)
```bash
# Build image
docker build -t champion .

# Run container
docker run -p 8501:8501 champion

# Access at http://localhost:8501
```

---

## 📋 Features Overview

| Feature | Description |
|---------|-------------|
| 🏠 Home | Welcome page with company info |
| ❓ FAQ | Search FAQs with intelligent matching |
| 📅 Schedule | Book pickup online |
| 📍 Track | Track your order status |
| 🧹 Services | View all services offered |
| 🎁 Offers | Current promotions |

---

## 🔍 Testing the App

### Test FAQ Search
1. Go to "❓ FAQs" page
2. Search: "bag cleaning"
3. Should show: "What is the Bag & Shoe Spa service?"
4. Click "Confirm & Schedule Pickup"
5. Fill form and submit

### Test Schedule
1. Go to "📅 Schedule Pickup"
2. Fill in your details
3. Select date and time
4. Click "Confirm & Schedule Pickup"
5. See order ID

### Test Track Order
1. Go to "📍 Track Order"
2. Select "Order ID" or "Phone Number"
3. Enter a test value
4. Click "Search"

---

## ⚙️ Configuration

### Change Colors
Edit `config.py`:
```python
BRAND_COLORS = {
    "primary": "#00A651",      # Green
    "secondary": "#C1272D",    # Red
}
```

### Change Theme
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#00A651"
backgroundColor = "#f5f5f5"
```

### Change Port
```bash
streamlit run streamlit_app.py --server.port=9000
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
streamlit run streamlit_app.py --server.port=8502
```

### Dependencies Not Found
```bash
# Reinstall
pip install --upgrade -r requirements.txt
```

### Database Issues
```bash
# Reset database
rm champion_orders.db
```

### Clear Streamlit Cache
```bash
streamlit cache clear
```

---

## 📁 File Structure

```
champion/
├── streamlit_app.py          ← Run this
├── requirements.txt          ← pip install this
├── config.py                 ← Configuration
├── database.py               ← Database
├── pages/                    ← App pages
│   ├── home.py
│   ├── faq.py
│   ├── schedule.py
│   ├── track.py
│   ├── services.py
│   └── offers.py
└── .streamlit/
    └── config.toml           ← Theme settings
```

---

## 📚 Detailed Guides

- **Full Setup:** See [STREAMLIT_README.md](./STREAMLIT_README.md)
- **Deployment:** See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
- **Summary:** See [STREAMLIT_DEPLOYMENT_SUMMARY.md](./STREAMLIT_DEPLOYMENT_SUMMARY.md)

---

## 🎯 Next Steps

### Development
1. ✅ Run locally
2. ✅ Test all features
3. ✅ Customize branding
4. ✅ Add your data

### Deployment
1. ✅ Choose platform
2. ✅ Follow guide
3. ✅ Monitor performance
4. ✅ Share with users

### Optimization
1. ✅ Gather feedback
2. ✅ Optimize search
3. ✅ Add new features
4. ✅ Scale infrastructure

---

## 💡 Pro Tips

### Speed Up Search
- Reduce FAQ data size
- Add caching

### Improve UX
- Add more features
- Customize colors
- Add logo/images

### Scale App
- Use load balancer
- Add database
- Setup monitoring

---

## 📞 Support

Need help?
- 📧 Email: mail@champion-cleaners.com
- 📞 Phone: +971 4 2858581
- 💬 WhatsApp: +971 50 7738025

---

## 🎓 Learn More

- [Streamlit Docs](https://docs.streamlit.io)
- [Python Guide](https://www.python.org/doc/)
- [Git Guide](https://git-scm.com/docs)

---

## ✨ You're All Set!

```bash
# Run this one command:
streamlit run streamlit_app.py

# Then visit:
http://localhost:8501
```

**Enjoy your new Streamlit app! 🚀**

---

**Last Updated:** January 7, 2026
**Version:** 2.0.0
