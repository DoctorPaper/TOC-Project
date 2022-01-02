import os
import random
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import requests
from lxml import etree

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def get_menu(index):
    response = requests.get("https://twcoupon.com/bmenu-50%E5%B5%90-menu%E8%8F%9C%E5%96%AE%E5%83%B9%E6%A0%BC.html")
    content = response.content.decode()
    html = etree.HTML(content)
    menu = html.xpath(f"//div[@class='store_menu']//div[@class='wrapper']//ul[{index}]//text()")
    string = ""
    for item in menu[2:]:
        string += item

    return string

def get_random_recommend():
    response = requests.get("https://twcoupon.com/bmenu-50%E5%B5%90-menu%E8%8F%9C%E5%96%AE%E5%83%B9%E6%A0%BC.html")
    content = response.content.decode()
    html = etree.HTML(content)
    menu = html.xpath(f"//div[@class='store_menu']//div[@class='wrapper']//ul[{random.randint(1,4)}]//text()")
    items = menu[3::4]
    return "本日推薦: " + items[random.randint(0,len(items)-1)]


def get_reply():
    rand_reply = [
        "請不要亂打字==",
        "輸入【使用教學】 查看指令",
        "腦癱嗎 字打好",
        "再亂打字我要生氣囉",
        "不想喝飲料請不要煩我謝謝",
        "哀額講那什麼洨話啊",
        "好像有人在亂講欸 還是怎麼樣的",
        "吼優 你到底有沒有要喝飲料啦"
    ]

    return rand_reply[random.randint(0,len(rand_reply)-1)]
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
