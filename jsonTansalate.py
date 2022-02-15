# -*- coding: utf-8 -*-
# @Time    : 2021-10-18 15:05
# @Author  : 王代明
# @Email   : 1416962790@qq.com
# @File    : fiand.py
# @Software: PyCharm
import json
import random
import re
import time
import pyperclip

from main import *

# listt = ['de', 'spa', 'fra', 'jp', 'kor', 'vie', 'th','zh']

# listt=['en']
listt = ['ben']
# with open("zh-cn", 'r', encoding='utf-8') as fp:
#     list1 = fp.readlines()
#     fp.close()

lastResult = ""
sourceLanguage = "en"
# print("输入翻译内容：")
text='{ "VirtualGame": "Virtual game", "ProductList": "Product List", "ItsOverPleaseWaitForTheNextTime": "It'+str("'s")+' over. Please wait for the next time", "DigInSuccessfully": "Dig in successfully", "iSee": "I see", "PleaseChooseYourWallet": "please choose your wallet", "NoWalletAddressFoundPleaseMaintain": "No wallet address found, please maintain", "loadMore": "pull down to load more", "MoreService": "More service", "in": "In", "out": "Out", "uploading": "uploading", "changeLanguage": "change language", "detail": "detail", "EnterQuantity": "Enter Quantity", "Details": "Details", "Cancel": "Cancel", "Home": "Home", "FindPassword": "Find Password", "Single": "Single", "Double": "Double", "SmallSingle": "Small Single", "SmallDouble": "Small Double", "BigSingle": "Big Single", "BigDouble": "BigDouble", "r1": "tips： A handling fee of 1U will be charged for withdrawals below 500 A 0.3% commission will be charged for withdrawals over 500 (including 500)", "r2": "tips: As exchanges may charge transfer fees. Make sure the merchant receives the full payment. After payment. The system will automatically check the payment status.", "r3": "After confirmation, the funds will be transferred to the opposite account" }'
for name in listt:
    print(text)
    params_json = json.loads(text)

    # jsonObject=json.dumps(params_json,sort_keys=True)
    # print(type(params_json))
    items = params_json.items()
    for key, value in items:
        value=value.replace("》》》","\"")
        print(value)
        url = 'https://fanyi.baidu.com/v2transapi'
        zh = sourceLanguage
        en = name
        sign = signs(value)
        data = datas(sign, value, zh, en)
        r = xinxi(url, data)
        try:
            print("翻译结果：  " + r['trans_result']['data'][0]['dst'])
        except:
            r = xinxi(url, data)
        result = r['trans_result']['data'][0]['dst']
        value = re.sub("(.*?: ')(.*?)('.*?)", lambda m: m.group(1) + str(result) + m.group(3), value)
        if en == sourceLanguage:
            result = value
        params_json[key] = result
    # fpp.write(result)
    print(params_json)

# stra="Nicknames: 'Nicknames',"
# text = re.sub("(.*?: ')(.*?)('.*?)", lambda m:m.group(1)+str(12345678)+m.group(3),stra)
# # # test=str.replace("Nicknames",'123')
# print(text)
#
# url='http://www.55188.com/thread-8306254-2-3.html'
# pattern='-(\d+)-(\d+)-(\d+)'
# i=5678
# newUrl=re.sub(pattern,lambda m:'-'+m.group(1)+'-'+str(i)+'-'+m.group(3),url)
# print(newUrl)
