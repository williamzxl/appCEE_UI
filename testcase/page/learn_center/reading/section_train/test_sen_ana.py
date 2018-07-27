from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.reading.sen_analysis.sen_ana_AllResultPage3 import SAAllAnswerPage
from testcase.interface.reading.sen_analysis.get_all_sen_analysis_answer import get_all_sen_analysis_answer, \
    right_answer_sen_ana, wrong_answer_sen_ana

item_class = (By.CLASS_NAME, "android.widget.TextView")

login_page = SAAllAnswerPage()
login_page.open(noReset=True)
items = login_page.find_elements(*item_class)
for item in items:
    if login_page.getText(item) == "阅读":
        item.click()
        for item in items:
            if login_page.getText(item) == "句子分析":
                item.click()
                eles = login_page.get_all_list_ele()
                for i in eles[32:]:
                    num = login_page.get_list_num(login_page, i)
                    result = login_page.click_one_list(login_page, i)
                    print("Result:",result, "Num:", num)
                    if result == 0:
                        all_answers, all_answers_choice = get_all_sen_analysis_answer(list=int(num))
                        curr_sen, total = login_page.get_sen_ana_lists_nums()
                        print("Cureent_SNE",curr_sen, "Total", total)
                        for curr_sen in range(curr_sen, total + 1):
                            curr_ques, total_ques = login_page.get_step_nums()
                            print("Current_ques:",curr_ques,"Total_ques",  total_ques)
                            for curr_ques in range(curr_ques, total_ques + 1):
                                right_answer, choice_EN = right_answer_sen_ana(all_answers, all_answers_choice,\
                                                                               sen_num=curr_sen,ques_num=curr_ques)
                                print("right_answer:", right_answer, "choice_EN:", choice_EN)
                                if str(choice_EN).isupper() and choice_EN is not None:
                                    login_page.sen_ana_choose_answer(right_answer)
                                    login_page.click_sen_ana_sure_button()
                                    login_page.click_sen_ana_next_question()
                                if right_answer and choice_EN is None:
                                    print("填写中文句子：", right_answer)
                                    login_page.fill_CN_answer(right_answer)
                                    login_page.click_sen_ana_sure_button()
                                    login_page.click_sen_ana_finish_button()
                                    # login_page.click_sen_ana_next_sen()
                                if right_answer == 0 and choice_EN is None:
                                    try:
                                        login_page.click_to_check_CN()
                                        login_page.click_sen_ana_sure_button()
                                        login_page.click_sen_ana_finish_button()
                                        login_page.click_sen_ana_next_sen()
                                    except:
                                        pass
                                # if int(curr_sen) == int(total_ques) and int(curr_ques) == int(total_ques):
                                #     login_page.click_word_icon()
                                #     login_page.click_words_list_finish()
                                #     login_page.click_back_btn()

                        # login_page.gra_fill_answer(login_page, answers=right_answer, nums=10)
                        # login_page.click_gra_fill_submit()
                        # login_page.click_sure_button()
                        # login_page.click_finish_button()
                        # login_page.click_finish_all()
                        # login_page.click_back_btn()
                    if result == 3:
                        login_page.click_back_btn()
                    if result == 4:
                        login_page.click_words_list_finish()
                        login_page.click_back_btn()
                    # if result == 7:
                    #     answers = get_all_gra_fill_answer(list=int(num))
                    #     # curr, total = login_page.get_gra_lists_nums()
                    #     # print(curr, total)
                    #     # login_page.click_gra_fill_next_step()
                    #     # print(answers)
                    #     login_page.gra_fill_answer(login_page, answers=answers, nums=10)
                    #     login_page.click_gra_fill_submit()
                    #     login_page.click_sure_button()
                    #     login_page.click_finish_button()
                    #     login_page.click_finish_all()
                    #     login_page.click_back_btn()





