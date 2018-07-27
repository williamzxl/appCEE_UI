from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.sen_fill.senfill_all_resultPage3 import SFAllAnswerPage
from testcase.interface.sysListening.sen_fill.sen_fill_all_answer import get_all_sen_fill_answer,\
    right_answer_sen_fill, wrong_answer_sen_fill


item_class = (By.CLASS_NAME, "android.widget.TextView")

login_page = SFAllAnswerPage()
login_page.open(noReset=True)
items = login_page.find_elements(*item_class)
for item in items:
    # print(login_page.getText(item))
    if login_page.getText(item) == "句子填充":
        item.click()
        eles = login_page.get_all_list_ele()
        for i in eles[7:8]:
            num = login_page.get_list_num(login_page, i)
            result = login_page.click_one_list(login_page, i)
            print(num, result)
            if result == 0:
                answers = get_all_sen_fill_answer(list=int(num))
                curr, total = login_page.get_senfill_lists_nums()
                print(curr, total)
                for j in range(int(curr), int(total) + 1):
                    if j == int(total):
                        login_page.save_screen_shot(page_name="Word_Trans", file_name="播放截图")
                        current_right_answer = right_answer_sen_fill(answers, j)
                        current_wrong_answer = wrong_answer_sen_fill(answers, j)
                        print(current_right_answer, current_wrong_answer)
                        try:
                            login_page.hideKeyboard()
                        except:
                            login_page.save_screen_shot("No KEYBoard")
                        login_page.senfill_fill_answer(current_right_answer)
                        login_page.save_screen_shot("题目判定页")
                        login_page.senfill_fill_answer()
                        login_page.click_words_list_button()
                        login_page.click_words_list_finish()
                        login_page.click_back_btn()
                    # login_page.click_audio_button()
                    else:
                        login_page.save_screen_shot(page_name="Word", file_name="播放截图")
                        current_right_answer = right_answer_sen_fill(answers, j)
                        current_wrong_answer = wrong_answer_sen_fill(answers, j)
                        print(current_right_answer, current_wrong_answer)
                        try:
                            login_page.hideKeyboard()
                        except:
                            login_page.save_screen_shot("No KEYBoard")
                        login_page.senfill_fill_answer(current_right_answer)
                        login_page.save_screen_shot("题目判定页")
                        login_page.click_next_button()
            # if result == 1:
            #     login_page.click_next_button()
            if result == 2:
                # login_page.click
                login_page.click_back_btn()
            if result == 3:
                print(login_page.get_grade())
                print(login_page.get_time())
                '''
                点击结果页的题目序号并返回
                '''
                eles = login_page.get_item_lists_index()
                for ele in eles:
                    login_page.click_result_num_index(ele)
                    login_page.click_back_all_result_page()
                '''
                点击结果页的生词表并返回
               '''
                login_page.click_word_icon()
                login_page.click_back_all_result_page()
                login_page.click_back_btn()
            if result == 4:
                login_page.click_words_list_button()
                login_page.save_screen_shot("结果展示页")
                login_page.click_back_btn()

