
# import modules and global library
import requests
import yt_dlp
import json
import os

# TOKEN and BASE_URL

TOKEN = "955000265:DNX5vcMQjYLh2cNW1zX2QkeBTaGUEft1anE"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}/"

last_update_id = 0

# my proxies to get the best conection from youtube

proxye = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}
proxy = {
    'quiet': True,
    'format': 'best',
    'proxy': "socks5h://127.0.0.1:9150"
}   

# function for sending message

def sendMessage(text , chat_id):
    url = BASE_URL + "sendMessage"
    result = requests.post(url , json={
        "chat_id": chat_id,
        "text": text
    })
    print(result)
    return result

# funciton send message with inline keyboard

def sendMessage_with_inline_keyboard(text , chat_id , text_keyboard , callback_data):
    
    url = BASE_URL + "sendMessage"
    result = requests.post(url , json={
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {"text": text_keyboard , "callback_data": callback_data}
                ]
            ]
        }
    })
    print(result)
    return result



status = {}
while True:
        
    response = requests.get(
            BASE_URL + "getUpdates",
            params={"offset": last_update_id + 1, "timeout": 5},
        )
    
    data = response.json()
    for messages in data["result"]:
        
        if "callback_query" in messages:
            callback_query = messages["callback_query"]
            data_callback = callback_query["data"]
            username = callback_query["from"]["first_name"]
            chat_id = callback_query["message"]["chat"]["id"]

            if data_callback == "download_video_yes":
                sendMessage("لطفا لینک خود را وارد کنید" , chat_id)
                status[chat_id] = "wait_for_url_yes"
        
            if data_callback == "send_file":
                sendMessage("لطفا لینک خود را وارد کنید " , chat_id)
                status[chat_id] = "send_file"
            
            
        message = messages.get("message" , {})
        chat_id = message.get("chat" , {}).get("id")
        text = message.get("text")
        last_update_id = messages["update_id"]
            
        if text == "/start":
           url_send2 = BASE_URL + "sendMessage"
           result = requests.post(url_send2 , json={
                "chat_id": chat_id,
                "text": "سلام  به ربات یوتیوب دانلودر خوش آمدید",
                "reply_markup": {
                "inline_keyboard": [
                        [
                            {"text": "دانلود اتوماتیک" , "callback_data": "download_video_yes"},
                            {"text": "فرستادن فایل" , "callback_data": "send_file"}
                        ]
                    ]   
                }
            })
           print(result)
           
        elif status.get(chat_id) == "wait_for_url_yes":
            url = text
            status[chat_id] = None
            
            try:
                with yt_dlp.YoutubeDL(proxy) as i:
                    
                    sendMessage("در حال دانلود لطفا کمی صبر کنید ..." , chat_id)
                    info = i.extract_info(url , download=False)
                    download_link = info["url"]
                    print(download_link)
                    
                with requests.get(download_link , proxies=proxye , stream=True) as file:
                    sendMessage("در حال انتقال به سیستم ...." , chat_id)
                    with open("video.mp4" , "wb") as filename:
                        for i in file.iter_content(chunk_size=10000):
                            filename.write(i)
                    sendMessage("فایل با موفقیت دانلود شد🥳🥳🎉🎉" , chat_id)
                    
            except Exception as e:
                print(f"{e} :به ارور برخوردم")
        
        elif status.get(chat_id) == "send_file":
            try:
                url = text
                sendMessage("لینک در حال پزدازش است لطفا کمی صبر کنید" , chat_id)
                with yt_dlp.YoutubeDL(proxy) as i:
                    info = i.extract_info(url , download=False)
                    download_link = info["url"]
                    print(download_link)
                    
                with requests.get(download_link , proxies=proxye , stream=True) as file:
                    url_send = BASE_URL + "sendDocument"
                    files = {"document": ("video.mp4" , file.raw)}
                    result_send = requests.post(url_send , data={"chat_id": chat_id} , files=files)
            except Exception as e:
                print(f"{e} :به ارور برخوردم")