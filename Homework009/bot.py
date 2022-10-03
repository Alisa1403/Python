from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext


bot = Bot(token='5602457808:AAEAFUxm4qvRVdcerGcXB7d0l1C0Xy3E6ps')
updater = Updater(token='5602457808:AAEAFUxm4qvRVdcerGcXB7d0l1C0Xy3E6ps')
dispatcher = updater.dispatcher

def letter(update: Updater, context: CallbackContext):
    text = update.message.text
    if 'абв' in text.lower():
        msg = text.split()
        update.message.reply_text(' '.join(list(filter(lambda x: 'абв' not in x.lower(), msg))))
    else:
        context.bot.send_message(update.effective_chat.id, 'В тексте нет слов с "абв')


letter_handler = CommandHandler('letter', letter)
dispatcher.add_handler(letter_handler)

updater.start_polling()
updater.idle()

