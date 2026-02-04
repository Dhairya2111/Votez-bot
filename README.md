# Discord Bot with Commands

A feature-rich Discord bot built with `discord.py`.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create a bot application on the [Discord Developer Portal](https://discord.com/developers/applications).
3. Copy your Bot Token into the `.env` file.
4. Ensure 'Message Content Intent' is enabled in the Developer Portal.
5. Run the bot: `python bot.py`

## Commands
- `!ping`: Check latency.
- `!echo <text>`: Repeat text.
- `!userinfo <@user>`: Get user details.
- `!clear <number>`: Bulk delete messages.
- `!help`: Show this list.