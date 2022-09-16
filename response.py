from datetime import datetime
import requests
api_key="5748788062:AAHPP-5baIzIy7Q7zjccYgnwIJkAzjqRUeE"
base_url = 'https://api.telegram.org/bot{}/'.format(api_key)

to_url='https://api.telegram.org/bot{}/sendPhoto'.format(api_key)
def sample_responses(input_text):
    user_message=str(input_text).lower()
    
    if user_message in("hi","hola","vanakkam","namaste"):
        return "Hi"
    if user_message in("how are you","epdi iruka","nalla irukiya"):
        return "Fine Bro,wat about you"
    if user_message in("name","un per enna","who are you","ne yaru"):
        return "IM A SIGMAVERSE_BOT"
    if user_message in("john"):
        payload={
     "chat_id": "5645358157",
     "photo" : "https://images.news18.com/ibnlive/uploads/2022/09/collage-maker-08-sep-2022-09.38-pm-16626533113x2.jpg?impolicy=website&width=510&height=356"}
        requests.post(to_url,data=payload)
        return "John is a Potta"
    if user_message in("women","whamen","pengal","girl"):
        return "hahahahahahahahahaha!Whamennnn!hahahh"
    if user_message in("time","mani enna","whats the time","whats the time now"):
        a=datetime.now()
        date_time=a.strftime("%d/%m/%y,%H:%M:%S")
        return str(date_time)
    if user_message in("yourpic","sendyourpic","show your face"):
        payload={
     "chat_id": "5645358157",
     "photo" : "https://melmagazine.com/wp-content/uploads/2021/01/Gigachad.jpg"}
        requests.post(to_url,data=payload)
        return"This is upates me"
    if user_message in("ruban"):
        payload={
     "chat_id": "5645358157",
     "photo" : "https://theancestory.com/wp-content/uploads/2022/02/pv-gaming-phone-number.jpg"}
        requests.post(to_url,data=payload)
        return"This is Ruban Free Fire legend"
    if user_message in("ruban100"):
       for i in range(100):
         payload={"chat_id": "5645358157","photo" : "https://theancestory.com/wp-content/uploads/2022/02/pv-gaming-phone-number.jpg"}
         requests.post(to_url,data=payload)
       return"This is Ruban Free Fire legend"

    return "nahi betta! cant understand"
