import requests
from pprint import pprint
url = "http://192.168.1.154:55262/users/practices/groups"

querystring = {"grpType":"1"}

headers = {
    'host': "192.168.1.154:55262",
    'content-type': "application/json",
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'connection': "keep-alive",
    'appkey': "Cet_E94A599B77DA",
    'user-agent': "LBLearnCenter/1.0 (iPhone; iOS 11.0.3; Scale/3.00)",
    'accesstoken': "6ab38189-a25b-4c83-926d-027c578b4aef",
    'accept-language': "zh-Hans-CN;q=1",
    'appversion': "1.0",
    'cache-control': "no-cache",
    'postman-token': "432158f0-e795-9186-5fe7-8ef0774666d4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)