#'6854847182:AAE8B_0q5f_PFsbduxMauxpRgJikNrgDw8A'
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi!')

def main() -> None:
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    application = Application.builder().token('6854847182:AAEQ6ll2nGkCEvozf7iQS437G1XwVDOuxNI').build()

    # Add a command handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()