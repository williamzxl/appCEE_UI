import requests

url = "http://192.168.1.154:55262/sysReading/934/senAnalysis"

querystring = {"taskID":"1"}

headers = {
    'platform': "Android",
    'appversion': "1.0",
    'appkey': "Cet_E94A599B77DA",
    'app': "cee",
    'appsecret': "8548C4F6-96F1-4E37-ADD6-89BEF5478B9B",
    'accesstoken': "b9e93792-d6f9-4e5d-bd80-f00bead144e1",
    'host': "192.168.1.154:55262",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.7.0",
    'cache-control': "no-cache",
    'postman-token': "9f46a9d2-8fbe-440b-4520-b6cba489d75d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)