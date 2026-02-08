# Discord Unmute Bot

A simple Discord bot to handle unmuting members. It supports both the modern Discord **Timeout** feature and the legacy **Muted role** method.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration**:
    - Create a bot application in the [Discord Developer Portal](https://discord.com/developers/applications).
    - Enable `Server Members Intent` and `Message Content Intent` under the **Bot** tab.
    - Copy your Bot Token into the `.env` file.

3.  **Run the Bot**:
    ```bash
    python main.py
    ```

## Usage

- `/unmute @user [reason]`

**Note**: The bot must have a higher role than the user it is trying to unmute and must have the `Manage Roles` and `Moderate Members` permissions.