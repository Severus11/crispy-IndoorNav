import cv2
import logging
import urllib.request
import final_npGrid as fnp

from telegram.ext import Updater, MessageHandler, Filters
 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


def download_image(url,name):
    fullname = str(name)+".jpeg"
    urllib.request.urlretrieve(url,fullname)


def some_func(bot, update):
    pass
    if not update.effective_message.photo:
        update.effective_message.reply_text(text = "I don't prefer to talk but only find shortest paths to your destinations")
        update.effective_message.reply_text(text = "Send the map of your organization")
    else:
        chat_id = update.message.chat_id
        msg = update.effective_message
        file_id = msg.photo[-1].file_id
        photo = bot.get_file(file_id)
        download_image(photo["file_path"],'wassup')
        #text = pytesseract.image_to_string(cv2.imread("wassup.jpeg"), lang = "eng")
        update.effective_message.reply_text(text = 'Let me see through this')
        
        #fnp.imgop('wassup.jpeg')
        #fnp.main()
        
        
        bot.send_photo(chat_id=chat_id, photo=open('/home/severus7/Documents/python/astar/hero.png', 'rb'))
        update.effective_message.reply_text(text = 'Here is the shortest path to your destination. Happy traversing !!')

def solution_send(bot, update):
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=open('hero.jpg', 'rb'))


        
def main():
    updater = Updater('ENTER YOUR KEY HERE')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, some_func))
    #final_npGrid()
    dp.add_handler(MessageHandler(Filters.all, solution_send))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
