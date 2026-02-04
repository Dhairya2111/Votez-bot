# Telegram Voting Bot

A simple bot to collect votes in channels and groups (FCs).

## Setup Instructions

1.  **Get a Token**: Message [@BotFather](https://t.me/botfather) on Telegram to create a bot and get your API Token.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure**: Open `bot.py` and replace `YOUR_TOKEN_HERE` with your actual bot token.
4.  **Run the Bot**:
    ```bash
    python bot.py
    ```

## How to use

1. Add the bot to your Channel or Group as an Admin.
2. Use the command: `/create_poll Question | Option 1 | Option 2`.
3. Users can click buttons to vote. The bot prevents double voting by switching the user's choice if they click a different option.