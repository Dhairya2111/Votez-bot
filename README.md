# Telegram Voting Bot

A simple Telegram bot to conduct polls in channels and groups using inline buttons.

## Setup Instructions

1.  **Get API Credentials:**
    - Go to [my.telegram.org](https://my.telegram.org) and create an app to get `API_ID` and `API_HASH`.
    - Message [@BotFather](https://t.me/BotFather) to create a bot and get the `BOT_TOKEN`.

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure:**
    - Open `bot.py` and replace `API_ID`, `API_HASH`, and `BOT_TOKEN` with your actual values.

4.  **Run the Bot:**
    ```bash
    python bot.py
    ```

## How to use
- Add the bot to your group or channel as an admin.
- Send: `/create_poll Question | Option 1 | Option 2`
- Users can click buttons to vote. Clicking again removes the vote.