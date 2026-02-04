import logging
import os
from pyrogram import Client, filters, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Bot Configuration
API_ID = 1234567  # Replace with your API ID
API_HASH = "your_api_hash"  # Replace with your API HASH
BOT_TOKEN = "your_bot_token"  # Replace with your Bot Token

app = Client("poll_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Database to store poll results (In-memory for this example)
# Structure: {message_id: {option_index: [user_ids]}}
polls_db = {}

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Hello! I am a Poll Bot.\n\n"
        "You can create custom polls in groups and channels.\n"
        "Use /create_poll to start."
    )

@app.on_message(filters.command("create_poll") & (filters.group | filters.channel | filters.private))
async def create_poll_command(client, message):
    text = message.text.split(None, 1)
    if len(text) < 2:
        return await message.reply_text("Usage: `/create_poll Question | Option 1 | Option 2 | Option 3`")

    parts = [p.strip() for p in text[1].split("|")]
    if len(parts) < 3:
        return await message.reply_text("Please provide a question and at least 2 options.")

    question = parts[0]
    options = parts[1:]

    buttons = []
    for idx, opt in enumerate(options):
        buttons.append([InlineKeyboardButton(f"{opt} (0)", callback_data=f"vote_{idx}")])

    poll_msg = await message.reply_text(
        f"📊 **POLL**\n\n**{question}**\n\nTotal Votes: 0",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # Initialize poll data
    polls_db[poll_msg.id] = {
        "question": question,
        "options": options,
        "votes": {str(i): [] for i in range(len(options))}
    }

@app.on_callback_query(filters.regex(r"^vote_"))
async def handle_vote(client, callback_query):
    poll_id = callback_query.message.id
    user_id = callback_query.from_user.id
    option_idx = callback_query.data.split("_")[1]

    if poll_id not in polls_db:
        return await callback_query.answer("Poll expired or data lost.", show_alert=True)

    poll = polls_db[poll_id]
    
    # Check if user already voted for this specific option
    if user_id in poll["votes"][option_idx]:
        # Remove vote (Toggle feature)
        poll["votes"][option_idx].remove(user_id)
        await callback_query.answer("Vote removed!")
    else:
        # Remove from other options first (Single choice poll)
        for opt in poll["votes"]:
            if user_id in poll["votes"][opt]:
                poll["votes"][opt].remove(user_id)
        
        poll["votes"][option_idx].append(user_id)
        await callback_query.answer("Vote recorded!")

    # Update UI
    total_votes = sum(len(v) for v in poll["votes"].values())
    new_buttons = []
    for i, opt_text in enumerate(poll["options"]):
        count = len(poll["votes"][str(i)])
        new_buttons.append([InlineKeyboardButton(f"{opt_text} ({count})", callback_data=f"vote_{i}")])

    await callback_query.edit_message_text(
        f"📊 **POLL**\n\n**{poll['question']}**\n\nTotal Votes: {total_votes}",
        reply_markup=InlineKeyboardMarkup(new_buttons)
    )

if __name__ == "__main__":
    print("Bot is running...")
    app.run()