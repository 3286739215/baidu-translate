import execjs
import requests
headers={
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://fanyi.baidu.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://fanyi.baidu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'BIDUPSID=46044067443B4D4E5ED38B036142D8B8; PSTM=1625450821; __yjs_duid=1_3f567388e8ee4d075a1ba374072a24911625466455298; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=107315_110085_127969_164869_176399_181536_184716_185240_185268_185636_186635_186840_189732_189755_190248_190797_191068_191253_191288_191783_192206_192389_192407_193283_193560_194085_194512_194605_195004_195188_195343_195631_195679_196045_196426_196487_196513_197287_197288_197471_197553_197577_197711_197782_197832_197956_198076_198089_198188_198261_198420_198513_198648_199177_199284_199305_199468_199565_199648_199678_199753_199755_199836_199865_199906_200055_200158_200273_200448_200554_200870_200933_200966_201103_201329_201546; APPGUIDE_10_0_2=1; BAIDUID=1A092EBD4CB938F746C3C0E9E48FD345:FG=1; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=nwCOJeC62wud0cTD2-XqSenl4eb0QuoTH6aoZPBlS2mOgWrgufMNEG0PDU8g0KAbJrxhogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJFJoC-MJDI3fP36qROE-tC--fT2aP_XKKOLVMTaBp7ketn4hUt20xcL54Oi0ltJJGRk_-D-WhvJMnc2QhrKQtkqXPcw2ROq-2rJ-J3s3PTpsIJM5Mo2QUCTBU5k0bTUaKviaKOEBMb1VCnDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6o-ea0qtjkjfKresJoq2RbhKROvhjRvef0gyxoObtRxtNr-MhcgWh54JC5MWjJaDxPUbNJBLU3k-eT9LMnx--t58h3_XhjJWhK7QttjQn0O5g3TKfJt3pTFDb7TyU45hf47ybKO0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRLDVCPMJDLWhKv65nt_KttSqxby26n02e79aJ5y-J7nhMoNBU6UyULZ2GoTX6bDte3i0K3_QpbZql5VM5OBjq4sjxOXBh5MyNcnKl0MLP-WehvMQl3DQMFNhMnMBMPeamOnaU_y3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRe5t2D6O0jGROaRcWt4o8Qtcy5t0_fb7xeUJajM4pbt-qJfoA5NAO_l-abMFVMfJXMtvzKjo30x5nBTKOaGKjs4oIQI5jDJvabfvOM4kkQN3TJtKO5bRi5lCMMtcaDn3oyTbVXp0n0G7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJuj_Kt2JI-2bnO1MtbOKPLX5x_XKPoHbT7-34oJ2Tr_et-rhRJTXUI8LNDH-bQbtI7nKI_EyPj6eJr1j-oDDh_0hnO7ttoyyHRGWU8-al7JSPoT5tjYXxL1Db3RL6vMtg3C3qc-Mnnoepvojtcc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SC0hJDJP; BDSFRCVID_BFESS=nwCOJeC62wud0cTD2-XqSenl4eb0QuoTH6aoZPBlS2mOgWrgufMNEG0PDU8g0KAbJrxhogKK5mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJFJoC-MJDI3fP36qROE-tC--fT2aP_XKKOLVMTaBp7ketn4hUt20xcL54Oi0ltJJGRk_-D-WhvJMnc2QhrKQtkqXPcw2ROq-2rJ-J3s3PTpsIJM5Mo2QUCTBU5k0bTUaKviaKOEBMb1VCnDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6o-ea0qtjkjfKresJoq2RbhKROvhjRvef0gyxoObtRxtNr-MhcgWh54JC5MWjJaDxPUbNJBLU3k-eT9LMnx--t58h3_XhjJWhK7QttjQn0O5g3TKfJt3pTFDb7TyU45hf47ybKO0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRLDVCPMJDLWhKv65nt_KttSqxby26n02e79aJ5y-J7nhMoNBU6UyULZ2GoTX6bDte3i0K3_QpbZql5VM5OBjq4sjxOXBh5MyNcnKl0MLP-WehvMQl3DQMFNhMnMBMPeamOnaU_y3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRe5t2D6O0jGROaRcWt4o8Qtcy5t0_fb7xeUJajM4pbt-qJfoA5NAO_l-abMFVMfJXMtvzKjo30x5nBTKOaGKjs4oIQI5jDJvabfvOM4kkQN3TJtKO5bRi5lCMMtcaDn3oyTbVXp0n0G7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJuj_Kt2JI-2bnO1MtbOKPLX5x_XKPoHbT7-34oJ2Tr_et-rhRJTXUI8LNDH-bQbtI7nKI_EyPj6eJr1j-oDDh_0hnO7ttoyyHRGWU8-al7JSPoT5tjYXxL1Db3RL6vMtg3C3qc-Mnnoepvojtcc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEK5r2SC0hJDJP; delPer=0; PSINO=7; H_PS_PSSID=35970_35104_31253_36005_34584_35948_35993_35318_26350_35882_35869_35877; BA_HECTOR=240k81848g050h21l41h2gqc90r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1644914734,1646813364,1646816789,1646817940; BDUSS=GNETHh5TENlMkZoQTBDOWttcDFxbkJBMnVNMllQdFFJVkZ6WUs2dTk1QW1BRkJpSVFBQUFBJCQAAAAAAQAAAAEAAABiAB8JztK63L22wswyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACZzKGImcyhiN; BDUSS_BFESS=GNETHh5TENlMkZoQTBDOWttcDFxbkJBMnVNMllQdFFJVkZ6WUs2dTk1QW1BRkJpSVFBQUFBJCQAAAAAAQAAAAEAAABiAB8JztK63L22wswyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACZzKGImcyhiN; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1646818092; ab_sr=1.0.1_ODQwYTVmYzlhZGJjM2JhZTIwYzBlOTAwMWQzM2JlNGZjMjc0MjQ2NDVjOGU1ODViY2EzZGQ1ZTkwOTI5NzJmMzUzYjlhNmU0OThlY2IxNTBhMmMxYTZjNmJjOGM5MGVjMmQ2NWQ1OTllMGJmZTliMDIwYjU2MzNiZjQ3ZWZjODgzYTdkMjgzOTY3YzhmOTYyMTc0NWYwOTJkNWM3OTYwNzM1ODhkYjYzZmNkMmUyOWEzODA3NWVmOGRkMzg4ZTE1'
}

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
        'token':'3e62499159366607f0667c0262d84827'
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