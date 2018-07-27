# from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.grammer.gra_choice.gra_choice_AllResultPage3 import GCAllResultPage
from testcase.interface.grammer.gra_choice.get_all_gra_choice_answer import get_all_gra_choice_answer,\
    right_answer_gra_choice, wrong_answer_gra_choice


item_class = (By.CLASS_NAME, "android.widget.TextView")

login_page = GCAllResultPage()
login_page.open(noReset=True)
items = login_page.find_elements(*item_class)
for item in items:
    # print(login_page.getText(item))
    if login_page.getText(item) == "语法":
        item.click()
        for item in items:
            if login_page.getText(item) == "单项选择":
                item.click()
                eles = login_page.get_all_list_ele()
                for i in eles[6:]:
                    num = login_page.get_list_num(login_page, i)
                    result = login_page.click_one_list(login_page, i)
                    print(num, result)
                    if result == 0:
                        answers = get_all_gra_choice_answer(list=int(num))
                        curr, total = login_page.get_gra_lists_nums()
                        print(curr, total)
                        for j in range(int(curr), int(total) + 1):
                            if j == int(total):
                                login_page.save_screen_shot(page_name="Word_Trans", file_name="播放截图")
                                current_right_answer = right_answer_gra_choice(answers, j)
                                current_wrong_answer = wrong_answer_gra_choice(answers, j)
                                print(current_right_answer, current_wrong_answer)
                                login_page.choose_answer(current_right_answer)
                                login_page.save_screen_shot("题目判定页")
                                login_page.click_gra_choose_sure()
                                login_page.click_words_list_button()
                                login_page.click_words_list_finish()
                            # login_page.click_audio_button()
                            else:
                                login_page.save_screen_shot(page_name="Word", file_name="播放截图")
                                current_right_answer = right_answer_gra_choice(answers, j)
                                current_wrong_answer = wrong_answer_gra_choice(answers, j)
                                print(current_right_answer, current_wrong_answer)
                                login_page.choose_answer(current_right_answer)
                                login_page.save_screen_shot("题目判定页")
                                login_page.click_gra_choose_sure()
                                login_page.click_next_button()
                    # if result == 1:
                    #     login_page.click_next_button()
                    if result == 2:
                        login_page.click_words_list_finish()
                        login_page.click_back_btn()
                    if result == 3:
                        login_page.click_back_btn()


