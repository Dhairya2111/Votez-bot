# Telegram Bot on Render

This is a production-ready Telegram bot template designed to be deployed on Render.com using Webhooks.

## Deployment Steps on Render:

1. Create a new **Web Service** on Render.
2. Connect your GitHub repository.
3. Use the following settings:
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
4. Add **Environment Variables**:
   - `BOT_TOKEN`: Your token from @BotFather.
   - `WEBHOOK_URL`: The URL Render gives you (e.g., `https://your-app-name.onrender.com`).

## How it works:
- The bot uses Flask to listen for incoming updates from Telegram.
- Webhooks are more efficient than polling for cloud platforms like Render because they don't keep the CPU busy constantly.