import requests
import json


def get_all_gra_choice_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysGrammar/{}/mulChoice".format(list)
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
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    answer = response.text
    json_data = json.loads(answer)
    result = json_data.pop("data").pop('questGuide')
    word_answers = []
    for a in result:
        word_answers.append(a.pop('questAnswer'))
    print("Database_answers:", word_answers)
    return word_answers


def right_answer_gra_choice(answer, num):
    get_answer = answer[:]
    right_answer = get_answer.pop(int(num)-1)
    return right_answer


def wrong_answer_gra_choice(answer, num):
    get_answer = answer[:]
    test = get_answer.pop(int(num)-1)
    wrong_answer = []
    if (ord(test) + 1) <= 68:
        wrong_answer.append(chr(ord(test) + 1))
    else:
        wrong_answer.append(chr(ord(test) -1))
    return "".join(wrong_answer)

#
# answer = get_all_gra_choice_answer(list=1533, taskID=1)
# print(right_answer_gra_choice(answer, 6))
# print(wrong_answer_gra_choice(answer, 6))
