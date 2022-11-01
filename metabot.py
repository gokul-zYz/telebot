from telegram.ext import *

import response as R
print("SIGMA WAKES UP...5..")
api=("5794179294:AAHjS2BLZt4k3dIN4D0XjxswdkQowhud7bo")
updater = Updater(token="5794179294:AAHjS2BLZt4k3dIN4D0XjxswdkQowhud7bo")
def start_command(update,context: CallbackContext):
    update.message.reply_text("Im Wake Up! bro")
def help_command(update,context: CallbackContext):
    update.message.reply_text("Need Help!? huh whamenn!")
def handle_message(update,context: CallbackContext):
    text=str(update.message.text).lower()
    response=R.sample_responses(text,context,update)
    update.message.reply_text(response)
def error(update,context):
    print(f"Update{update}caused error: {context.error}")
def main():
    updater=Updater(api,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
    
main()