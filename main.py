import execjs
import requests
headers={'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 'content-length': '106', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'BIDUPSID=EF5D2DCB95CD02713C504B965E680572; PSTM=1508391259; BAIDUID=FE94A1C6870007735C0EA30CA092352A:FG=1; BDUSS=HhpVTc3VjZrQ2ppRX5RcVFoQW9-WExTQ29zYWR-TUluOUQxRGVaWHZrWGlOWmRkRVFBQUFBJCQAAAAAAAAAAAEAAAAUxiG2ZnJlZc31vNG~pQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOKob13iqG9dW; locale=zh; __guid=37525047.783289347368707300.1568961749022.282; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; yjs_js_security_passport=67080cbdf7d8d4ad0eb8f1513b5feb52c128c29b_1569324592_js; monitor_count=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1568961749,1569324577,1569324592,1569324674; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1569324674; __yjsv5_shitong=1.0_7_9055159b9a5e975fcd2c2c48931b3bc7b406_300_1569324677995_117.32.216.70_70981334', 'origin': 'https://fanyi.baidu.com', 'referer': 'https://fanyi.baidu.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}


# proxies = {'http': 'http://27.13.39.70:4245', 'https': 'https://27.13.39.70:4245'}


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
        'token':'8d588b57816e1213f2bcfaf52bddbbe2',
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