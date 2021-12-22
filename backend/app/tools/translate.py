import http.client
import hashlib
import urllib
import random
import json, time


def baidufanyi(text,fromLang = 'auto', toLang = 'zh'):
    appid = '20211201001016121'  # 填写你的appid
    secretKey = '1GMFZqNIiVW5u2WHcGjH'  # 填写你的密钥

    salt = random.randint(32768, 65536)
    myurl = '/api/trans/vip/translate'
    result = ""
    if len(text.strip()) > 0:
        q = text
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        print(myurl)
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)['trans_result'][0]['dst']
            print(result_all)

        # except Exception as e:
        # print (e)
        except Exception as e:
            print(result_all)
            time.sleep(10)
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            print(result_all)
            result = json.loads(result_all)['trans_result'][0]['dst']

        finally:
            if httpClient:
                httpClient.close()
    time.sleep(3)
    print(result)
    return result


def translate(document,fromlang = "auto", tolang = 'zh'):
    # 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
    # coding=utf-8
    paras = document.paragraphs
    for para in paras:
        txt = ""
        if len(para.runs)<1:
            continue
        for run in para.runs:
            txt += run.text
            run.text = ""

        txt=baidufanyi(txt,fromlang, tolang)
        para.runs[0].text = txt



