import execjs
import requests
headers={'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 'content-length': '106', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'BIDUPSID=46044067443B4D4E5ED38B036142D8B8; PSTM=1625450821; __yjs_duid=1_3f567388e8ee4d075a1ba374072a24911625466455298; BDUSS=dQNGZES0huRGJEWnk4eEZnM243STZDNXlTV01LQzB3UjlDb2k0c1Bjd1VpZ3RoSVFBQUFBJCQAAAAAAAAAAAEAAADwtf3rztK63L22wswAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABT942AU~eNgbm; BDUSS_BFESS=dQNGZES0huRGJEWnk4eEZnM243STZDNXlTV01LQzB3UjlDb2k0c1Bjd1VpZ3RoSVFBQUFBJCQAAAAAAAAAAAEAAADwtf3rztK63L22wswAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABT942AU~eNgbm; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=107315_110085_127969_164869_176399_181536_184716_185240_185268_185636_186635_186840_189732_189755_190248_190797_191068_191253_191288_191783_192206_192389_192407_193283_193560_194085_194512_194605_195004_195188_195343_195631_195679_196045_196426_196487_196513_197287_197288_197471_197553_197577_197711_197782_197832_197956_198076_198089_198188_198261_198420_198513_198648_199177_199284_199305_199468_199565_199648_199678_199753_199755_199836_199865_199906_200055_200158_200273_200448_200554_200870_200933_200966_201103_201329_201546; BAIDUID=F5A4FF1C0128DD098507D75708687026:FG=1; APPGUIDE_10_0_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_YTliMjYyMDMzNTE0MjFhYWYzNWQzYWFmZThkYTEyYjFjNDhjY2JlYTNlNGRlOWJiYTMwYWEzMjlmMGRmOWMxZjViMDdkMjYwNmM5MmQ4MzYzM2UyODUyOGU4OWI4NGRjMTk4OWY5YTY3Yjc5MzQyMzZhNjI5ODRjMDM0YTRmMGI4YzNlYzM3NTk0YjZmZGVlOWEyZTQwZTk1MTJlNzUwZTVhNGM4N2UyNWUyYWRiNjMzYTcwMzlmZThhYmJmYTdh; H_PS_PSSID=35835_35104_31253_35777_34584_35490_35871_35316_26350_35883_35724_35877_22160; BDSFRCVID=KkIOJeC62GgmnYTDWnu75PYi4KXBLlJTH6aoysg4Iy-yjuCXUxKBEG0PoM8g0Ku-h9_4ogKK3mOTHR8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbFq_C_bJC_3H45Te5A-q4tehHRiaU79WDTm_D_X--TMhfoeDpPW-jLrWfry26ObtJCq-pPK5D8hsDj6QTJTXttnhNjPJj3k3mkjbpvDfn02OP5EQ-khWt4syP4e2xRnWNuOKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hI84j50KjjP8-Uvy-40XtR4jVIL8Kbu3MtncXU6qLT5XLP8eaRJB3NvXLCIaLUTEMboIDp3_yl0njxQy-U3m0DFe-h4ayIokEl5bMUonDhO02a7MJUPJKJnJXq6O5hvvhn6O3M7CeMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_Et5L8tnPH_Kv5b-0_JbQw5tI_-P6MyURAWMT-0bFHKb3EafTxsM3k5jth0hFtj-Rv3f7QWHn7_JjOM4OJMhTwqJr85ftR3q7i3fQxtNRy2CnjtpvhKJPwBTOobUPUDUc9LUvNfgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-mD6_M3e; BAIDUID_BFESS=F5A4FF1C0128DD098507D75708687026:FG=1; BDSFRCVID_BFESS=KkIOJeC62GgmnYTDWnu75PYi4KXBLlJTH6aoysg4Iy-yjuCXUxKBEG0PoM8g0Ku-h9_4ogKK3mOTHR8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbFq_C_bJC_3H45Te5A-q4tehHRiaU79WDTm_D_X--TMhfoeDpPW-jLrWfry26ObtJCq-pPK5D8hsDj6QTJTXttnhNjPJj3k3mkjbpvDfn02OP5EQ-khWt4syP4e2xRnWNuOKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hI84j50KjjP8-Uvy-40XtR4jVIL8Kbu3MtncXU6qLT5XLP8eaRJB3NvXLCIaLUTEMboIDp3_yl0njxQy-U3m0DFe-h4ayIokEl5bMUonDhO02a7MJUPJKJnJXq6O5hvvhn6O3M7CeMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_Et5L8tnPH_Kv5b-0_JbQw5tI_-P6MyURAWMT-0bFHKb3EafTxsM3k5jth0hFtj-Rv3f7QWHn7_JjOM4OJMhTwqJr85ftR3q7i3fQxtNRy2CnjtpvhKJPwBTOobUPUDUc9LUvNfgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLK-oj-D-mD6_M3e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1644385807,1644393647,1644483529,1644910453; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1644910453', 'origin': 'https://fanyi.baidu.com', 'referer': 'https://fanyi.baidu.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}


proxies = {'http': 'http://27.13.39.70:4245', 'https': 'https://27.13.39.70:4245'}


def get_ip():
    global proxies
    url = "http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    res = requests.get(url).json()
    data = res.get("data")
    pox = data[0].get("ip") + ":" + str(data[0].get("port"))
    proxies["http"] = "http://" + pox
    proxies["https"] = "https://" + pox
    print(proxies)

def signs(n):
    query = n
    with open('baidu_translate_js.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
    sign = ctx.call('e', query)
    return sign
def datas(sign,n,zh,en):
    data={
        'from':zh,
        'to': en,
        'query': n,
        'simple_means_flag':' 3',
        'sign': sign,
        'token':'2d990f2109c0837e3685f664a877e14c',
    }
    return data
def xinxi(url,data):
    try:
        r=requests .post(url=url,headers=headers,data=data,  timeout=10).json()
    except:
        get_ip()
        return xinxi(url,data)
    return r


if __name__=='__main__':
    url='https://fanyi.baidu.com/v2transapi'
    print("请输入需要的要求(1或者2)：")
    print("1.英译中      2.中译英")
    q=input()
    if q=='2':
        print("输入翻译内容：")
        n=input()
        zh='zh'
        en='en'
        sign=signs(n)
        data=datas(sign,n,zh,en)
        r=xinxi(url,data)
        print("翻译结果："+'\n'+r['trans_result']['data'][0]['dst'])
    else:
        print("输入翻译内容：")
        n = input()
        zh='en'
        en='zh'
        sign = signs(n)
        data = datas(sign, n,zh,en)
        r = xinxi(url, data)
        print("翻译结果：" + '\n' + r['trans_result']['data'][0]['dst'])