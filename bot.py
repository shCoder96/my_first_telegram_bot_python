import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level = logging.INFO,
					filename = 'bot.log')

def start_bot(bot, update):
	usrName = update.message.chat.username
	if usrName == None:
		usrName = update.message.chat.first_name
	mytxt = '''Hi {} i`m test bot'''.format(usrName)
	update.message.reply_text(mytxt)

def chat(bot, update):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
	upd = Updater(settings.TELEGRAM_API_KEY)  						# input API key


	upd.dispatcher.add_handler(CommandHandler('start', start_bot))
	upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))


	upd.start_polling()
	upd.idle()

if __name__ == "__main__":
	logging.info('bot started')
	main()