import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_TOKEN with your Telegram Bot token
updater = Updater(token='6026369739:AAHINpteBdu8Wv35KgoyrSKA--jjbQfCNNU', use_context=True)
dispatcher = updater.dispatcher

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Movie Series Bot!")

# Define the search command handler
def search(update, context):
    # Get the search query from user input
    query = ' '.join(context.args)
    if query:
        # Search for channels with the given query
        results = context.bot.get_chat_members_count(chat_id=query)
        if results:
            # If there are channels with the given query, send their links to user
            message = "Here are the channels I found:\n\n"
            for result in results:
                message += f"{result.link}\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No channels found with this name.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a search query.")

# Add the handlers to the dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))

# Start the bot
updater.start_polling()
