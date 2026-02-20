
import requests
import os
from soundcloud_downloader import SoundCloudDownloader
from pytube import YouTube

API = "8466968653:AAGkjuBzhiGhZ8LFX895EZ2wjaxd77kHwyY"
BASE_URL = f"https://api.telegram.org/bot{API}/"

proxy = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}

os.makedirs("download")

last_update_id = 0
    
def sendMessage_welcome(chat_id , text , work , text2 , work2):
    url = BASE_URL + "sendMessage"
    result = requests.post(url , json={
        "chat_id": chat_id,
        "text": text,
        "reply_markup":{
            "inline_keyboard":[
                [
                    {"text": text , "callback_data": work},
                    {"text": text2 , "callback_data": work2}
                ]
            ]
        }
    } , proxies=proxy)
    print(result)

def sendMessage(chat_id , text):
    url = BASE_URL + "sendMessage"
    result = requests.post(url , json={
        "chat_id": chat_id,
        "text": text,
    } , proxies=proxy)
    print(result)


def downloadd(url , chat_id):
    try:
        downloader = SoundCloudDownloader(output_dir="downloads")
        result = downloader.download_track(url)
        print(result)
    except:
        sendMessage(chat_id , "خطا در دانلود فایل❌❌")

def create_button(chat_id , text , work):
    url = BASE_URL + "sendMessage"
    result = requests.post(url , json={
        "chat_id":chat_id,
        "reply_markup":{
            "inline_keyboard":[
                [
                    {"text": text , "callback_data": work}
                ]
            ]
        }
    })
    print(result)


def download_youtube(url , chat_idd):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download("downloads")
    except:
        sendMessage(chat_id , "خطا در دانلود🤖")

status = {}
while True:
    response = requests.get(
        BASE_URL + "getUpdates",
        params={"offset": last_update_id + 1, "timeout": 3},
        proxies=proxy
    )
    data = response.json()
    print("در حال برقراری ارتباط")
    
    for messages in data["result"]:
        
        if "callback_query" in messages:
            callback_query = messages["callback_query"]
            chat_id = callback_query["message"]["chat"]["id"]
            data_btn = callback_query["data"]

            if data_btn == "download":
                sendMessage(chat_id , "لطفا لینک خود را وارد کنید")
                status[chat_id] = "wait_for_url"

            if data_btn == "download_youtube":
                sendMessage(chat_id , "لطفا آدرس دقیق آهنگ رو بفرستید")
                status[chat_id] = "wait_for_url_youtube"
        
        last_update_id = messages.get("update_id")
        message = messages.get("message" , {})
        chat_id = message.get("chat" , {}).get("id")
        text = message.get("text")
        
        if text == "/start":
            sendMessage_welcome(chat_id , " به ربات soundcloud-downloader خوش امدید🤖🤖" , "download" , "دانلود ویدیو یوتیوب🤖🤖 و" , "download_youtube"),
        elif status.get(chat_id) == "wait_for_url":
                        
            matn = text
            sendMessage(chat_id , matn)
            downloadd(matn , chat_id)
            del(status)

        elif status.get(chat_id) == "wait_for_url_youtube":
                        
            matn = text
            sendMessage(chat_id , matn)
            download_youtube(matn)
            del(status)