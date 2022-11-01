from telegram.ext import *
from requests import*
from telegram import *
import telegram
chat_list=['1339241817','1339241817']
#api_key="5748788062:AAHPP-5baIzIy7Q7zjccYgnwIJkAzjqRUeE"
def sample_responses(input_text,context,update):
    botl=telegram.Bot("5794179294:AAHjS2BLZt4k3dIN4D0XjxswdkQowhud7bo")
    user_message=str(input_text).lower()
    chat_id=update.effective_chat.id
    if chat_id  not in chat_list:
        chat_list.append(chat_id)
    print(chat_list)
    if user_message in("hi","hola","vanakkam","namaste","hy","hyy"):
         image = get("https://pbs.twimg.com/media/EJ8gLIcVAAI-WQw.jpg").content
         botl.send_chat_action(chat_id,action=telegram.chataction.ChatAction.TYPING)
         return context.bot.sendMediaGroup(chat_id, media=[InputMediaPhoto(image, caption="வணக்கம்டி மாப்ளே")])
    if user_message in("gokul"):
        return "he is very beautifulboy"
    if user_message in("bhavu"):
         
         return "She is a Angel👼🧡❤💚 "
    if user_message in("fuck","sex","boobs"):
         image = get("https://pbs.twimg.com/media/FZFchgwakAASIux.jpg").content
         botl.send_chat_action(chat_id,action=telegram.chataction.ChatAction.TYPING)
         return context.bot.sendMediaGroup(chat_id, media=[InputMediaPhoto(image, caption="வேண்டம் அண்ணா😞")])
    if user_message in("Theme song","our song","song","depression","boosts"):
        try :
             botl.send_message(chat_id,text="Wait Few Secs Im a Little Bot......😥")
             image = get("https://od.lk/d/NDBfNTAyMDg1Mzdf/GIGA%20CHAD%201.mp3").content
             botl.send_chat_action(chat_id,action=telegram.chataction.ChatAction.UPLOAD_AUDIO)
             return context.bot.sendMediaGroup(chat_id, media=[InputMediaAudio(image, caption="")])
        except:
          return("BOT UNDER MAINTAINANCE💻")
    """if user_message in("send"):
        for i in range(0,len(chat_list)):
            print(chat_list[i])
            botl.send_message(chat_list[i],text="MoVe Towards Your Goal Bro🐱‍🏍")
            image = get("https://od.lk/d/NDBfNTAyMDg1Mzdf/GIGA%20CHAD%201.mp3").content
            botl.send_chat_action(chat_list[i],action=telegram.chataction.ChatAction.UPLOAD_AUDIO)
            return context.bot.sendMediaGroup(chat_list[i], media=[InputMediaAudio(image, caption="")])"""
         
    return "nah Bro! cant understand exactly 😪What youre asking For Try Again!🧐"
    

if __name__ == "__main__":
    sample_responses =()
