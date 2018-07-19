# from time import sleep
from testcase.page.learn_center.listening.word_dic.word_listening_all_resultPage4 import WLAllAnswerPage
from testcase.interface.sysListening.word_dict.answer import get_all_answer,right_answer, wrong_answer

login_page = WLAllAnswerPage()
login_page.open(noReset=True)
eles = login_page.get_all_list_ele()
for i in eles[7:]:
    num = login_page.get_list_num(login_page, i)
    result = login_page.click_one_list(login_page, i)
    print(num, result)
    if result == 0:
        answers = get_all_answer(list=int(num))
        curr, total = login_page.get_words_list_num()
        print(curr, total)
        for j in range(int(curr), int(total) + 1):
            if j == int(total):
                login_page.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = right_answer(answers, j)
                current_wrong_answer = wrong_answer(answers, j)
                print(current_right_answer, current_wrong_answer)
                try:
                    login_page.hideKeyboard()
                except:
                    login_page.save_screen_shot("No KEYBoard")
                login_page.fill_answer(current_right_answer + "test")
                login_page.save_screen_shot("题目判定页")
                login_page.click_finish_button()
                login_page.click_back_btn()
            # login_page.click_audio_button()
            else:
                login_page.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = right_answer(answers, j)
                current_wrong_answer = wrong_answer(answers, j)
                print(current_right_answer, current_wrong_answer)
                try:
                    login_page.hideKeyboard()
                except:
                    login_page.save_screen_shot("No KEYBoard")
                login_page.fill_answer(current_right_answer + "test")
                login_page.save_screen_shot("题目判定页")
                login_page.click_next_button()
    # if result == 1:
    #     login_page.click_next_button()
    if result == 2:
        login_page.click_finish_button()
        login_page.click_back_btn()
    if result == 3:
        login_page.click_back_btn()


