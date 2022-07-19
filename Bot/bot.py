
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger, sendfile, Deletemessage
import os
import telepot
import urllib.request
from PIL import Image
import requests
from bs4 import BeautifulSoup
import random
import string
import requests
import time
import json
import math
import html5lib
dia='✅'

os.environ['TZ'] = 'America/Buenos_Aires'

gods=["21951A6626","21951A6637","21951A6627","21951A6614"]
members =[2141450636,809309749,2045746007,1257359605,2113380774,1134323688,2040610087]
bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='https://t.me/dheeraj2324'
		),
        InlineKeyboardButton(
			"Channel",
			url='https://t.me/aboutdheeraj'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    print(chat_id)
    userid= info['username']
    text = f'<b>Welcome</b> @{userid}<b>, to maths calculator bot and also private stuff!</b>\n<b>To know more use-</b> /help\n<code>This bot is provided for educational use!!</code>\n<code>ENTER IN YOUR OWN RISK!!</code>\n<code>YOU ARE RESPONSIBLE FOR YOUR OWN ACTION!.</code>'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return
def cmds(update, context):
    chat_id = update.message.chat_id
    text = "<b>Available cmds available:</b>\n<code>/ssc xxxxxxxxxxx</code>\n<code>/inter xxxxxxxxxxx</code>\n<code>/bd xxxxxxxxxxx</code>\n<code>/aadhar xxxxxxxxxxx</code>\n<code>/income xxxxxxxxxxx</code>\n<code>/caste xxxxxxxxxxx</code>\n<code>/pic xxxxxxxxxxx</code>\n<b>Do /lab for more info about labs!</b>\n<b>pvt Cmds are only shared with Gods!</b>\n<code>xxxxxxxxxxx -- replace with Roll no.</code>\n<b>ENTER IN YOUR OWN RISK!!!</b>"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Hey, welcome to this Bot! Sorry to say cmds of the bots have been taken to private!!</b>\n<code>Some cmds are listed here:</code> /cmds"
    Sendmessage(chat_id, text)

def ssc(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_SSC.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" :  "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def fssc(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_SSC.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def fpan(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_PAN_CARD.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!"
        Sendmessage(chat_id,text)
def addgod(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    
    text =  update.message.text.split(' ',1)
    print(info)
    logger.info(text)
    if chat_id in members:
        tempp=text[-1]
        global gods
        textt=tempp.upper()
        gods.append(textt)
        text = "Done!"
        Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def removegod(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    print(info)
    logger.info(text)
    if chat_id in members:
        tempp=text[-1]
        global gods
        textt=tempp.upper()
        if textt in gods:
            gods.remove(textt)
            text = "Done!"
            Sendmessage(chat_id,text)
        else:
            text="Never was a God"
            Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
##############################################################################################################################################
def inter(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    print(info)
    logger.info(text)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_INTER.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def finter(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    print(info)
    logger.info(text)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_INTER.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def pic(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods can't be seen!!"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def fpic(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods cann't be seen!!"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_PHOTO.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
#################################
####################################
def pic_range(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    try:
        ttt=int(textt[8:])
    except:
        ttt=int(textt[9:])
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                try:
                    ttt=int(textt[8:])
                    for i in range(ttt,ttt+11):
                        q=textt[8:]
                        w=textt[:8]
                        textt = w+str(i)
                        if textt in gods:
                            text = "Gods data not available"
                            Sendmessage(chat_id,text)
                        else:
                            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(textt,textt)
                            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                            payload = {
                                "chat_id" : chat_id,
                                "photo" : photos,
                                "caption" : "✅ Done!!---{}".format(textt)
                            }
                            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                            res=requests.post(to_url , data=payload)
                except:
                    ttt=int(textt[9:])
                    for i in range(0,10):
                        q=textt[9:]
                        w=textt[:9]
                        textt = w+str(i)
                        photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg".format(textt,textt)
                        base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                        payload = {
                            "chat_id" : chat_id,
                            "photo" : photos,
                            "caption" : "✅ Done!!---{}".format(textt)
                        }
                        to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                        res=requests.post(to_url , data=payload)
            except:
                text="Not Valid Roll no."
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
    
################################################################################################################################
def bd(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_BIRTHCERTIFICATE.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
################################################################################################################################################
def aadhar(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    global members
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Aadhar.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
	
def all_details(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    if chat_id in members:
        funcs = [pic, aadhar, ssc, inter, bd, eamcet, caste, income]
        for i in funcs:
            try: i(update, context)
            except: pass
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
	
def faadhar(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/IARE/STAFF/{}/DOC/{}_AADHAR_CARD.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
##########################################################################################################################################################
def eamcet(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    global members
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_EAMCET_RANK.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def caste(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Caste.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
def income(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    global members
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Income.jpg".format(textt,textt)
            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
            payload = {
                "chat_id" : chat_id,
                "photo" : photos,
                "caption" : "✅ Done!!---{}".format(textt)
            }
            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
            res=requests.post(to_url , data=payload)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
####################################
def bd_range(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    try:
        ttt=int(textt[8:])
    except:
        ttt=int(textt[9:])
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                try:
                    ttt=int(textt[8:])
                    for i in range(ttt,ttt+11):
                        q=textt[8:]
                        w=textt[:8]
                        textt = w+str(i)
                        if textt in gods:
                            text = "Gods data not available"
                            Sendmessage(chat_id,text)
                        else:
                            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_BIRTHCERTIFICATE.jpg".format(textt,textt)
                            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                            payload = {
                                "chat_id" : chat_id,
                                "photo" : photos,
                                "caption" : "✅ Done!!---{}".format(textt)
                            }
                            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                            res=requests.post(to_url , data=payload)
                except:
                    ttt=int(textt[9:])
                    for i in range(0,10):
                        q=textt[9:]
                        w=textt[:9]
                        textt = w+str(i)
                        photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_BIRTHCERTIFICATE.jpg".format(textt,textt)
                        base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                        payload = {
                            "chat_id" : chat_id,
                            "photo" : photos,
                            "caption" : "✅ Done!!---{}".format(textt)
                        }
                        to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                        res=requests.post(to_url , data=payload)
            except:
                text="Not Valid Roll no."
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
####################################
def aadhar_range(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',1)
    tempp=text[-1]
    logger.info(text)
    print(info)
    textt=tempp.upper()
    try:
        ttt=int(textt[8:])
    except:
        ttt=int(textt[9:])
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                try:
                    ttt=int(textt[8:])
                    for i in range(ttt,ttt+11):
                        q=textt[8:]
                        w=textt[:8]
                        textt = w+str(i)
                        if textt in gods:
                            text = "Gods data not available"
                            Sendmessage(chat_id,text)
                        else:
                            photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Aadhar.jpg".format(textt,textt)
                            base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                            payload = {
                                "chat_id" : chat_id,
                                "photo" : photos,
                                "caption" : "✅ Done!!---{}".format(textt)
                            }
                            to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                            res=requests.post(to_url , data=payload)
                except:
                    ttt=int(textt[9:])
                    for i in range(0,10):
                        q=textt[9:]
                        w=textt[:9]
                        textt = w+str(i)
                        photos = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Aadhar.jpg".format(textt,textt)
                        base_url = 'https://api.telegram.org/bot{}/'.format(bot_token)
                        payload = {
                            "chat_id" : chat_id,
                            "photo" : photos,
                            "caption" : "✅ Done!!---{}".format(textt)
                        }
                        to_url = 'https://api.telegram.org/bot{}/sendPhoto'.format(bot_token)
                        res=requests.post(to_url , data=payload)
            except:
                text="Not Valid Roll no."
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
   ##############################
def cfile(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    tempp=text[1]
    numb=text[2]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            file_id = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/LAB/SEM2/ACSC05/{}_week{}.pdf".format(textt,textt,numb)
            r=requests.get(file_id)
            qq=(list(str(r)))
            q=['<', 'R', 'e', 's', 'p', 'o', 'n', 's', 'e', ' ', '[', '2', '0', '0', ']', '>']
            if q==qq:
                sendfile(chat_id,file_id)
                text = "{}----[c-lab]----week{}".format(textt,numb)
                Sendmessage(chat_id,text)
            else:
                text = "Nasty burger didnt upload!"
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
###########################start karo yaha se##########################
def efile(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    tempp=text[1]
    numb=text[2]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            file_id = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/LAB/SEM2/AHSC04/{}_week{}.pdf".format(textt,textt,numb)
            r=requests.get(file_id)
            qq=(list(str(r)))
            q=['<', 'R', 'e', 's', 'p', 'o', 'n', 's', 'e', ' ', '[', '2', '0', '0', ']', '>']
            if q==qq:
                sendfile(chat_id,file_id)
                text = "{}----[English-lab]----week{}".format(textt,numb)
                Sendmessage(chat_id,text)
            else:
                text = "Nasty burger didnt upload!"
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
        
        
        ##################################################
def apfile(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    tempp=text[1]
    numb=text[2]
    logger.info(text)
    global members
    print(info)
    textt=tempp.upper()
    if chat_id in members:
        if textt in gods:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:		
            file_id = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/LAB/SEM2/AHSC05/{}_week{}.pdf".format(textt,textt,numb)
            r=requests.get(file_id)
            qq=(list(str(r)))
            q=['<', 'R', 'e', 's', 'p', 'o', 'n', 's', 'e', ' ', '[', '2', '0', '0', ']', '>']
            if q==qq:
                sendfile(chat_id,file_id)
                text = "{}----[AP-lab]----week{}".format(textt,numb)
                Sendmessage(chat_id,text)
            else:
                text = "Nasty burger didnt upload!"
                Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)
######################################################################################################################
def attendance(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    username=text[1]
    password=text[2]
    logger.info(text)
    print(info)
    Deletemessage(chat_id, update.message.message_id)
    text = "<code> {} </code> -- <b>Attendance</b>".format(username)
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            login_data={'username':username,'password':password}
            with requests.Session() as s:
              url = "https://samvidha.iare.ac.in/pages/login/checkUser.php"
              r= s.get(url)
              soup = BeautifulSoup(r.content, 'html5lib')
              q=s.post(url,data=login_data)
              url = "https://samvidha.iare.ac.in/home?action=stud_att_STD"
              r= s.get(url)
              aa=str(r.content[24973:28000])
              a=("English")
              t=aa.index(a)
              text="<b>English:</b> <code>{}%</code>".format(aa[t+238+1-2:t+238+1+7+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
              a="Probability and Statistics"
              t=aa.index(a)
              text="<b>P&S:</b> <code>{}%</code>".format(aa[t+205+43+9+1-2:t+205+43+9+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              a=("Applied Physics")
              t=aa.index(a)
              text="<b>AP:</b> <code>{}%</code>".format(aa[t+194+52-2+1:t+52+194+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
              a="Programming for Problem Solving using C"
              t=aa.index(a)
              text="<b>PPSC:</b> <code>{}%</code>".format(aa[t+218+52-2+1:t+218+52+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
              a="English Language and Communication Skills Laboratory"
              t=aa.index(a)
              text="<b>Eng lab:</b> <code>{}%</code>".format(aa[t+231+52+1-2:t+231+52+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
              a=("Physics Laboratory")
              t=aa.index(a)
              text="<b>AP lab:</b> <code>{}%</code>".format(aa[t+197+52+1-2:t+197+7+52+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
              a="Programming for Problem Solving using C Laboratory"
              t=aa.index(a)
              text="<b>C lab:</b> <code>{}%</code>".format(aa[t+229+52+1-2:t+229+7+52+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
              Sendmessage(chat_id,text)
            
#             file_id = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/LAB/SEM2/AHSC05/{}_week{}.pdf".format(textt,textt,numb)
#             r=requests.get(file_id)
#             qq=(list(str(r)))
#             q=['<', 'R', 'e', 's', 'p', 'o', 'n', 's', 'e', ' ', '[', '2', '0', '0', ']', '>']
#             if q==qq:
#                 sendfile(chat_id,file_id)
#                 text = "{}----[AP-lab]----week{}".format(textt,numb)
#             else:
#                 text = "Nasty burger didnt upload!"
#                 Sendmessage(chat_id,text)
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)        
        
        #boi  if didnt upload ka code likhe?kk u will? not sure how to write in tg format same as idle

#####################################################################################################################################################################


def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("pic", pic))
    dp.add_handler(CommandHandler("Pic", pic))
    dp.add_handler(CommandHandler("income", income))
    dp.add_handler(CommandHandler("Income", income))
    dp.add_handler(CommandHandler("caste", caste))
    dp.add_handler(CommandHandler("Caste", caste))
    dp.add_handler(CommandHandler("inter", inter))
    dp.add_handler(CommandHandler("aadhar", aadhar))
    dp.add_handler(CommandHandler("aadhars", aadhar_range))
    dp.add_handler(CommandHandler("all", all_details))
    dp.add_handler(CommandHandler("eamcet", eamcet))
    dp.add_handler(CommandHandler("bd", bd))
    dp.add_handler(CommandHandler("clab", cfile))
    dp.add_handler(CommandHandler("elab", efile))
    dp.add_handler(CommandHandler("Clab", cfile))
    dp.add_handler(CommandHandler("Elab", efile))
    dp.add_handler(CommandHandler("aplab", apfile))
    dp.add_handler(CommandHandler("Aplab", apfile))
    dp.add_handler(CommandHandler("APlab", apfile))
    dp.add_handler(CommandHandler("bds", bd_range))
    dp.add_handler(CommandHandler("addgod", addgod))
    dp.add_handler(CommandHandler("removegod", removegod))
    dp.add_handler(CommandHandler("Aadhar", aadhar))
    dp.add_handler(CommandHandler("cmds", cmds))
    dp.add_handler(CommandHandler("ssc", ssc))
    dp.add_handler(CommandHandler("fssc", fssc))
    dp.add_handler(CommandHandler("finter", finter))
    dp.add_handler(CommandHandler("fpan", fpan))
    dp.add_handler(CommandHandler("fpic", fpic))
    dp.add_handler(CommandHandler("pics", pic_range))
    dp.add_handler(CommandHandler("faadhar", faadhar))
    #dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("attendance", attendance))

    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
