import requests
import json

def get_all_short_conv_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysListening/{}/shortConv".format(list)
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
        'user-agent': "http/3.7.0",
        'cache-control': "no-cache",
        # 'postman-token': "70505db4-3560-4a2c-8ee1-f8eba4a83505"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    answer = response.text
    json_data = json.loads(answer)
    result = json_data.pop("data").pop('questGuide')
    word_answers = []
    for r in result:
        for answer in r.pop('subQuestGuide'):
            word_answers.append(answer.get('questAnswer'))
    print("Database_answers:", word_answers)
    return (word_answers)


def right_answer_short_conv(answer, num):
    get_answer = answer[:]
    right_answer = get_answer.pop(int(num)-1)
    return right_answer


def wrong_answer_short_conv(answer, num):
    get_answer = answer[:]
    test = get_answer.pop(int(num)-1)
    if ord(test) + 1 <= 68:
        wrong_answer = chr(ord(test) + 1)
    else:
        wrong_answer = chr(ord(test) - 1)
    return wrong_answer

#
# answer = get_all_sen_fill_answer(list=1501, taskID=1)
# print(right_answer_sen_fill(answer, 2))
# print(wrong_answer_sen_fill(answer, 2))
# print(tuple(answer))

