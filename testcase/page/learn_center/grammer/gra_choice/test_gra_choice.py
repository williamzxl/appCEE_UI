from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_trans.word_translating_all_resultPage3 import WTAllAnswerPage
from testcase.interface.sysListening.word_trans.word_trans_all_answer import get_all_trans_answer,\
    right_answer_trans, wrong_answer_trans


item_class = (By.CLASS_NAME, "android.widget.TextView")

login_page = WTAllAnswerPage()
login_page.open(noReset=True)
items = login_page.find_elements(*item_class)
for item in items:
    # print(login_page.getText(item))
    if login_page.getText(item) == "单词听译":
        item.click()
        eles = login_page.get_all_list_ele()
        for i in eles[13:15]:
            num = login_page.get_list_num(login_page, i)
            result = login_page.click_one_list(login_page, i)
            print(num, result)
            if result == 0:
                answers = get_all_trans_answer(list=int(num))
                curr, total = login_page.get_words_trans_lists_nums()
                print(curr, total)
                for j in range(int(curr), int(total) + 1):
                    if j == int(total):
                        login_page.save_screen_shot(page_name="Word_Trans", file_name="播放截图")
                        current_right_answer = right_answer_trans(answers, j)
                        current_wrong_answer = wrong_answer_trans(answers, j)
                        print(current_right_answer, current_wrong_answer)
                        try:
                            login_page.hideKeyboard()
                        except:
                            login_page.save_screen_shot("No KEYBoard")
                        login_page.choose_answer(current_right_answer)
                        login_page.save_screen_shot("题目判定页")
                        login_page.click_finish_button()
                        login_page.click_back_btn()
                    # login_page.click_audio_button()
                    else:
                        login_page.save_screen_shot(page_name="Word", file_name="播放截图")
                        current_right_answer = right_answer_trans(answers, j)
                        current_wrong_answer = wrong_answer_trans(answers, j)
                        print(current_right_answer, current_wrong_answer)
                        try:
                            login_page.hideKeyboard()
                        except:
                            login_page.save_screen_shot("No KEYBoard")
                        login_page.choose_answer(current_right_answer)
                        login_page.save_screen_shot("题目判定页")
                        login_page.click_next_button()
            # if result == 1:
            #     login_page.click_next_button()
            if result == 2:
                login_page.click_finish_button()
                login_page.click_back_btn()
            if result == 3:
                print(login_page.get_grade())
                print(login_page.get_time())
                all_stars = login_page.list_all_starts()
                print(len(all_stars))
                print(login_page.getSize())
                # for star in all_stars:
                #     login_page.click_star(star)
                #     login_page.choose_star(2)
                login_page.swipeUp(1080, 1629, 369, 5)
                # login_page.flickUp(1080, 1629, 369)
                sleep(30)
                login_page.click_back_btn()


