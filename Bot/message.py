import logging
from telegram import Bot
import os
players="-1001782490306"
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

bot_token = os.environ.get('TG_BOT_TOKEN')
bot = Bot(bot_token)

def Sendmessage(chat_id, text,reply_markup=None):
    try:
        message = bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=None,parse_mode="HTML", reply_markup=reply_markup)
        msg_id = message.message_id
        return msg_id
    except Exception as e:
        logger.info(e)
        raise UserWarning
def SendMess(players, text,reply_markup=None):
    try:
        message = bot.send_message(chat_id=players, text=text, reply_to_message_id=None,parse_mode="HTML", reply_markup=reply_markup)
        msg_id = message.message_id
    except Exception as e:
        logger.info(e)
        raise UserWarning
def Editmessage(chat_id, text, msg_id, reply_markup=None):
    try:
        bot.edit_message_text(chat_id=chat_id, text=text, message_id=msg_id,parse_mode="HTML", reply_markup=reply_markup)
    except Exception as e:
        logger.info(e)
def sendfile(chat_id, file_id):
    try:
        bot.send_document(chat_id=chat_id, document = file_id)
    except Exception as e:
        logger.info(e)
def Deletemessage(chat_id,msg_id):
    try:
        bot.delete_message(chat_id=chat_id , message_id = msg_id)
    except Exception as e:
        logger.info(e)
