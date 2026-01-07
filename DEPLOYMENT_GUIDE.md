# 🚀 Deployment Guide - Champion Cleaners Streamlit App

## Deployment Options Comparison

| Platform | Cost | Ease | Scale | Features |
|----------|------|------|-------|----------|
| Streamlit Cloud | Free | ⭐⭐⭐⭐⭐ | Medium | Built for Streamlit |
| Heroku | $5-50/month | ⭐⭐⭐⭐ | Small | Full control |
| AWS | Variable | ⭐⭐⭐ | Large | Very scalable |
| Azure | Variable | ⭐⭐⭐ | Large | Enterprise ready |
| DigitalOcean | $5+/month | ⭐⭐⭐ | Medium | Developer friendly |

## 1. Streamlit Cloud (Recommended - Free)

### Prerequisites
- GitHub account with the repository
- Streamlit Cloud account

### Steps

1. **Push Code to GitHub**
   ```bash
   git add -A
   git commit -m "Deploy to Streamlit Cloud"
   git push origin master
   ```

2. **Connect to Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Click "New app"
   - Select your repository, branch, and main file
   - Main file: `streamlit_app.py`

3. **Configure Secrets (if needed)**
   - In Streamlit Cloud dashboard
   - Go to App settings → Secrets
   - Add environment variables:
     ```
     DATABASE_URL=file:///app/champion_orders.db
     ```

4. **Deploy**
   - Streamlit Cloud automatically deploys on push
   - Your app is live at: `https://your-username-champion.streamlit.app`

### Advantages
- ✅ Free hosting
- ✅ Automatic deployments
- ✅ No server management
- ✅ Custom domain support
- ✅ Analytics included

---

## 2. Heroku Deployment

### Prerequisites
- Heroku account (heroku.com)
- Heroku CLI installed

### Steps

1. **Create Procfile**
   ```bash
   echo "web: streamlit run streamlit_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

2. **Create runtime.txt**
   ```bash
   echo "python-3.11.5" > runtime.txt
   ```

3. **Create .streamlit/config.toml**
   ```toml
   [client]
   showErrorDetails = false

   [server]
   headless = true
   port = $PORT
   ```

4. **Login to Heroku**
   ```bash
   heroku login
   ```

5. **Create Heroku App**
   ```bash
   heroku create champion-cleaners
   ```

6. **Deploy**
   ```bash
   git push heroku master
   ```

7. **View Logs**
   ```bash
   heroku logs --tail
   ```

### Cost
- Free tier (limited, may sleep)
- Paid: $5-50/month

---

## 3. AWS EC2 Deployment

### Prerequisites
- AWS account
- EC2 instance (t2.micro free tier eligible)
- SSH key pair

### Steps

1. **Create EC2 Instance**
   - Choose Ubuntu 22.04 LTS AMI
   - Instance type: t2.micro (free tier)
   - Security group: Allow HTTP (80), HTTPS (443), SSH (22)

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Setup Server**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   
   # Clone repository
   git clone https://github.com/adeelciit786-hue/champion.git
   cd champion
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Use Systemd to Run Streamlit**
   ```bash
   sudo nano /etc/systemd/system/streamlit.service
   ```
   
   Paste:
   ```ini
   [Unit]
   Description=Streamlit Champion Cleaners App
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/champion
   ExecStart=/home/ubuntu/champion/venv/bin/streamlit run streamlit_app.py --server.port=8501
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

5. **Enable and Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable streamlit
   sudo systemctl start streamlit
   sudo systemctl status streamlit
   ```

6. **Setup Nginx Reverse Proxy**
   ```bash
   sudo apt install nginx
   sudo nano /etc/nginx/sites-available/default
   ```
   
   Replace with:
   ```nginx
   server {
       listen 80 default_server;
       listen [::]:80 default_server;
       
       server_name _;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

7. **Restart Nginx**
   ```bash
   sudo systemctl restart nginx
   ```

---

## 4. Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Create .dockerignore

```
__pycache__
.venv
venv
.git
.gitignore
*.pyc
.DS_Store
champion_orders.db
```

### Build and Run

```bash
# Build image
docker build -t champion-cleaners .

# Run container
docker run -p 8501:8501 champion-cleaners

# Run with database persistence
docker run -p 8501:8501 -v $(pwd)/data:/app/data champion-cleaners
```

---

## 5. Docker Compose (Production)

### Create docker-compose.yml

```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./champion_orders.db:/app/champion_orders.db
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    restart: always
  
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - streamlit
    restart: always
```

### Deploy

```bash
docker-compose up -d
```

---

## 6. Azure App Service

### Prerequisites
- Azure account
- Azure CLI installed

### Steps

```bash
# Create resource group
az group create --name champion-rg --location eastus

# Create App Service Plan
az appservice plan create --name champion-plan --resource-group champion-rg --sku B1

# Create Web App
az webapp create --resource-group champion-rg --plan champion-plan --name champion-cleaners

# Configure deployment
az webapp deployment source config-zip --resource-group champion-rg --name champion-cleaners --src app.zip

# View logs
az webapp log tail --resource-group champion-rg --name champion-cleaners
```

---

## 7. Google Cloud Run

### Steps

```bash
# Create Dockerfile (see above)

# Build and push image
gcloud builds submit --tag gcr.io/PROJECT_ID/champion-cleaners

# Deploy
gcloud run deploy champion-cleaners \
  --image gcr.io/PROJECT_ID/champion-cleaners \
  --platform managed \
  --region us-central1 \
  --port 8501
```

---

## Post-Deployment Checklist

- ✅ Test all pages and functionality
- ✅ Test FAQ search with multiple queries
- ✅ Test schedule form submission
- ✅ Test order tracking
- ✅ Verify database operations
- ✅ Check mobile responsiveness
- ✅ Test contact forms
- ✅ Verify email notifications (if configured)
- ✅ Monitor performance
- ✅ Setup backups

---

## Performance Optimization

### Before Deployment

1. **Enable Caching**
   ```python
   @st.cache_data
   def load_faq_data():
       return FAQ_DATA
   ```

2. **Database Optimization**
   - Add indexes to frequently queried columns
   - Regular backups

3. **Streamlit Configuration**
   ```toml
   [client]
   showErrorDetails = false
   
   [logger]
   level = "warning"
   ```

---

## Monitoring & Logs

### Streamlit Cloud
- Built-in metrics dashboard
- Real-time logs in cloud console

### AWS
```bash
# View EC2 logs
sudo journalctl -u streamlit -f

# Monitor system
htop
```

### Docker
```bash
# View logs
docker logs -f container_id

# Monitor resources
docker stats
```

---

## Security Best Practices

1. **Environment Variables**
   - Never commit secrets to Git
   - Use `.env` file (ignored by Git)
   - Set in deployment platform

2. **Database**
   - Regular backups
   - Encryption in transit
   - Secure access credentials

3. **HTTPS**
   - Enable SSL/TLS
   - Use Let's Encrypt (free)
   - Redirect HTTP to HTTPS

4. **Input Validation**
   - Validate all user inputs
   - Sanitize data before storage
   - Use parameterized queries

---

## Scaling Strategies

### For Small Traffic (< 1000 visits/day)
- Streamlit Cloud (Free)
- Heroku Free Tier

### For Medium Traffic (1000-10k visits/day)
- Heroku Paid
- Single AWS EC2 instance
- DigitalOcean Droplet

### For Large Traffic (10k+ visits/day)
- AWS Auto Scaling
- Load Balancer
- Managed Database (RDS)
- CDN (CloudFront)

---

## Disaster Recovery

1. **Regular Backups**
   ```bash
   # Backup database
   cp champion_orders.db champion_orders.db.backup
   ```

2. **Version Control**
   - All code in Git
   - Tagged releases
   - Rollback capability

3. **Monitoring**
   - Health checks
   - Uptime monitoring
   - Alert notifications

---

## Cost Estimation

| Platform | Monthly Cost | Notes |
|----------|-------------|-------|
| Streamlit Cloud | $0 | Free (with limitations) |
| Heroku | $5-50 | Starting at $5 |
| AWS EC2 | $0-50 | Free tier + usage |
| DigitalOcean | $5+ | Simple pricing |
| Azure | Variable | Pay as you go |

---

## Support & Troubleshooting

### Common Issues

**Issue:** Port already in use
```bash
# Kill process on port 8501
lsof -i :8501
kill -9 <PID>
```

**Issue:** Database locked
```bash
# Reset database
rm champion_orders.db
```

**Issue:** Memory issues
- Reduce cache size
- Implement pagination
- Use lazy loading

---

## Next Steps

1. Choose your deployment platform
2. Follow the specific guide above
3. Test thoroughly
4. Monitor performance
5. Gather user feedback
6. Iterate and improve

---

**Last Updated:** January 7, 2026
**For Support:** Contact the development team
