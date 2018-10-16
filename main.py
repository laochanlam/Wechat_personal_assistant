#!usr/bin/python
# -*- coding: utf-8 -*-

import itchat
from itchat.content import *
from googletrans import Translator

translator = Translator()

@itchat.msg_register([TEXT, PICTURE])
def _(msg):
    # result = translator.translate("Result from google translator", dest="zh-CN")
    # print(result.text)
    result = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # print(result[3:8])
    # print(msg.text)
    # translate_detect_object = translator.detect(msg.text)
    # if (translate_detect_object.lang.find("zh-CN") != -1) or (translate_detect_object.lang.find("zh-tw") != -1):
    #     print("find chinese")
    #     translated_object = translator.translate(
    #     msg.text, src="zh-tw", dest="en")
    # else:
    #     print("no find chinese")
    #     translated_object = translator.translate(
    #     msg.text, dest="zh-tw")
    #     # print(translate_detect_object.lang)
    # print(translated_object.text)
    if result[3:8] == "KARRY":
    # equals to print(msg['FromUserName'])
        translate_detect_object = translator.detect(msg.text)
        if (translate_detect_object.lang.find("zh-CN") != -1) or (translate_detect_object.lang.find("zh-tw") != -1):
            print("find chinese")
            translated_object = translator.translate(
            msg.text, src="zh-tw", dest="en")
        else:
            print("no find chinese")
            translated_object = translator.translate(
            msg.text, dest="zh-tw")
            # print(translate_detect_object.lang)
        print(translated_object.text)
        return translated_object.text
        # return u"豬仔[愛心]"

itchat.auto_login()
itchat.run()
