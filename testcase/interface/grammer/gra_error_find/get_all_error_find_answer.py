import requests
import json


def get_all_gra_fill_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysGrammar/{}/graFill".format(list)
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
    result = json_data.pop("data").get('questGuide')
    word_answers = []
    for k, v in result[0].items():
        if type(v) == type([1]):
            for i in v[1].pop('subQuestGuide'):
                word_answers.append(i.get('questAnswer'))
    return word_answers


def right_answer_gra_fill(answer, num):
    get_answer = answer[:]
    # right_answer = get_answer.pop(int(num)-1)
    right_answer = get_answer
    return right_answer

def wrong_answer_gra_fill(answer, num):
    get_answer = answer[:]
    # test = get_answer.pop(int(num)-1)
    wrong_answer = []
    for w in get_answer:
        wrong_answer.append(w[::-1])
    return wrong_answer

#
# def wrong_answer_gra_choice(answer, num):
#     get_answer = answer[:]
#     test = get_answer.pop(int(num)-1)
#     wrong_answer = []
#     for w in test:
#         if chr(ord(w.lower()) + 1).isalpha():
#             wrong_answer.append(chr(ord(w.lower()) + 1))
#         else:
#             wrong_answer.append(chr(ord(w.lower()) - 1))
#     return "".join(wrong_answer)

#
# answer = get_all_gra_fill_answer(list=1553, taskID=1)
# print(answer)
# print(right_answer_gra_fill(answer, 1))
# print(wrong_answer_gra_fill(answer, 1))
