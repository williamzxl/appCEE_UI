import requests
import json
from itertools import chain


def get_all_sen_analysis_answer(list, taskID=1):
    url = "http://192.168.1.154:55262/sysReading/{}/senAnalysis".format(list)
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
    all_answers = []
    all_answers_choice= []
    for q in result:
        all_questAnswer = q.get('subQuestGuide')
        all_answers.append([a.get('questAnswer') for a in all_questAnswer])
        all_answers_choice.append([a.get('questChoices') for a in all_questAnswer])
    return all_answers, all_answers_choice

def right_answer_sen_ana(answers, answers_choice, sen_num=None, ques_num=None):
    choice_EN = answers[sen_num-1][ques_num - 1]
    print("Choice_EN:", choice_EN)
    answers_choice = list(chain(*answers_choice))
    if choice_EN:
        if choice_EN.isupper():
            for cn in list(chain(*answers_choice)):
                if choice_EN == cn.get('choiceTag'):
                    choice_CN = cn.get('choiceCN')
                    if choice_CN:
                        return choice_CN, choice_EN
        else:
            return choice_EN, None
    else:
        return 0, None

def wrong_answer_sen_ana(answers, answers_choice, sen_num=None, ques_num=None):
    choice_EN = answers[sen_num - 1][ques_num - 1]
    print("Choice_EN:", choice_EN)
    answers_choice = list(chain(*answers_choice))
    if choice_EN:
        if choice_EN.isupper():
            print(list(chain(*answers_choice)))
            for cn in list(chain(*answers_choice)):
                if choice_EN == cn.get('choiceTag'):
                    choice_CN = cn.get('choiceCN')
                    if choice_CN:
                        return choice_CN
        else:
            return choice_EN + "Test"
    else:
        return 0


answers, answers_choice = get_all_sen_analysis_answer(list=958, taskID=1)
right = right_answer_sen_ana(answers, answers_choice, 3, 1)
# wrong  = wrong_answer_sen_ana(answers, answers_choice, 5, 2)
print(right)
# print(wrong)
