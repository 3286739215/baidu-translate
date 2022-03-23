import random
import re
import time
import json
from main import *

listt = ['zh','cht','th','spa']
# listt = ['zh']
sourceLanguage = "en"
with open("source", 'r', encoding='utf-8') as fp:
    list1 = fp.read()
    fp.close()

for name in listt:
    print(sourceLanguage, ">>>>>>>", name)

    with open(name+'.js', 'a+', encoding='utf-8') as fpp:
        print(sourceLanguage,">>>>>>>>>>>>",name)
        params_json = json.loads(str(list1))
        items = params_json.items()
        for key, value in items:
            value = value.replace("》》》", "\"")
            print(value)
            url = 'https://fanyi.baidu.com/v2transapi'
            zh = sourceLanguage
            en = name
            sign = signs(value)
            data = datas(sign, value, zh, en)
            # r = xinxi(url, data)
            r = xinxi(url, data)
            try:
                print("翻译结果：  " + r['trans_result']['data'][0]['dst'])
            except:
                r = xinxi(url, data)
                print (r)
            result = r['trans_result']['data'][0]['dst']
            value = re.sub("(.*?: ')(.*?)('.*?)", lambda m: m.group(1) + str(result) + m.group(3), value)
            if en == sourceLanguage:
                result = value
            params_json[key] = result
            print(params_json)
        fpp.write(str(params_json))
        fpp.close()

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
