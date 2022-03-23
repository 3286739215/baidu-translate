# -*- coding: utf-8 -*-
# @Time    : 2021-10-18 15:05
# @Author  : 王代明
# @Email   : 1416962790@qq.com
# @File    : fiand.py
# @Software: PyCharm
import random
import re
import time
import pyperclip

from main import *
# listt = ['de', 'spa', 'fra', 'jp', 'kor', 'vie', 'th','zh']

# listt=['en']
listt = ['zh','cht', 'en', 'jp', 'vie', 'kor', 'th', 'de','fra','spa','tr']
# with open("source", 'r', encoding='utf-8') as fp:
#     list1 = fp.readlines()
#     fp.close()

lastResult=""
sourceLanguage="zh"
print("输入翻译内容：")
text=input()
for name in listt:
    print(name)
    # new_text = ""
    # try:
    #     new_text = re.search(".*?: '(.*?)'", text).group(1)
    # except:
    #     pass
    # if not new_text == "":
        # time.sleep(random.randint(2, 3))
    url = 'https://fanyi.baidu.com/v2transapi'
    zh = sourceLanguage
    en = name
    sign = signs(text)
    data = datas(sign, text, zh, en)
    r = xinxi(url, data)
    print("翻译结果：  " + r['trans_result']['data'][0]['dst'])
    result = r['trans_result']['data'][0]['dst']
    text = re.sub("(.*?: ')(.*?)('.*?)", lambda m:m.group(1)+str(result)+m.group(3),text)
    if en==sourceLanguage:
        result=text
    lastResult+="\""+result+"--\"+\n"
    # fpp.write(result)

lastResult = lastResult[:-5]
lastResult+="\""
pyperclip.copy(lastResult)
print(lastResult)

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