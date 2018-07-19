import requests
import json

def get_all_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysListening/{}/wordDic".format(list)
    # url = "http://192.168.1.154:55262/sysListening/1000/wordDic"
    querystring = {"taskID": "{}".format(taskID)}
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
        'postman-token': "70505db4-3560-4a2c-8ee1-f8eba4a83505"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    answer = response.text
    json_data = json.loads(answer)
    result = json_data.pop("data").pop('questGuide')
    word_answers = []
    for a in result:
        word_answers.append(a.pop('wordEN'))
    print("Database_answers:",word_answers )
    return word_answers


def right_answer(answer, num):
    get_answer = answer[:]
    right_answer = get_answer.pop(num-1)
    return right_answer


def wrong_answer(answer, num):
    get_answer = answer[:]
    test = get_answer.pop(num-1)
    wrong_answer = []
    for i in test:
        if chr(ord(i) + 1).isalpha():
            wrong_answer.append(chr(ord(i) + 1))
        else:
            wrong_answer.append(chr(ord(i) -1))
    wrong_answer = "".join(wrong_answer)
    return wrong_answer


# answer = get_all_answer(list=1001, taskID=1)
# print(right_answer(answer, 1))
# print(wrong_answer(answer, 1))
# print(tuple(answer))
#
