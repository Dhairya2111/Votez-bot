import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Dictionary to store poll data
# Structure: {poll_id: {'question': str, 'options': {opt_id: {'text': str, 'votes': set(user_ids)}}}}
polls = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the Voting Bot!\n\n"
        "Use /create_poll <Question> | <Option1> | <Option2> to start a poll.\n"
        "Example: /create_poll Who is the best? | Messi | Ronaldo"
    )

async def create_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /create_poll Question | Opt1 | Opt2")
        return

    input_text = " ".join(context.args)
    parts = [p.strip() for p in input_text.split('|')]
    
    if len(parts) < 3:
        await update.message.reply_text("❌ Please provide a question and at least 2 options separated by '|'")
        return

    question = parts[0]
    options = parts[1:]
    poll_id = str(update.message.message_id)
    
    polls[poll_id] = {
        'question': question,
        'options': {str(i): {'text': opt, 'votes': set()} for i, opt in enumerate(options)}
    }

    keyboard = []
    for i, opt in enumerate(options):
        keyboard.append([InlineKeyboardButton(f"{opt} (0)", callback_data=f"vote_{poll_id}_{i}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"📊 *POLL:* {question}", reply_markup=reply_markup, parse_mode='Markdown')

async def handle_vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    
    # Data format: vote_pollid_optionindex
    _, poll_id, opt_index = query.data.split('_')

    if poll_id not in polls:
        await query.answer("This poll is no longer active.", show_alert=True)
        return

    poll = polls[poll_id]
    
    # Remove user from any other option in the same poll (prevent double voting)
    for idx in poll['options']:
        if user_id in poll['options'][idx]['votes']:
            poll['options'][idx]['votes'].remove(user_id)

    # Add vote
    poll['options'][opt_index]['votes'].add(user_id)
    
    # Update Keyboard
    keyboard = []
    for idx, data in poll['options'].items():
        count = len(data['votes'])
        keyboard.append([InlineKeyboardButton(f"{data['text']} ({count})", callback_data=f"vote_{poll_id}_{idx}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await query.edit_message_reply_markup(reply_markup=reply_markup)
        await query.answer("Vote recorded!")
    except Exception as e:
        await query.answer("Vote updated!")

if __name__ == '__main__':
    # Replace 'YOUR_TOKEN_HERE' with your actual Bot Token from @BotFather
    TOKEN = "YOUR_TOKEN_HERE"
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("create_poll", create_poll))
    application.add_handler(CallbackQueryHandler(handle_vote, pattern="^vote_"))
    
    print("Bot is running...")
    application.run_polling()