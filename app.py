import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
import requests
from flask import Flask
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

TOKEN = 'YOUR_BOT_TOKEN'

@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'
    
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I can upload URLs to Render or Koyeb instances.')

def upload(update, context):
    url = context.args[0]
    chat_id = update.effective_chat.id

    # Upload URL to Render or Koyeb instance
    render_url = f'https://your-render-instance.com/upload?url={url}'
    koyeb_url = f'https://your-koyeb-instance.com/upload?url={url}'

    # Send uploaded file to Telegram chat
    context.bot.send_document(chat_id, render_url or koyeb_url)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('upload', upload))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    app.run()
