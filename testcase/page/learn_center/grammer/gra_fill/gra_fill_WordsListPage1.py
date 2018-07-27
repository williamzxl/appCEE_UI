import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class GCChooseAnswerPage(AllCommonEle, ItemLists):
    '''
    语法单选题目作答页
    '''
    gra_page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    gra_list_num_id = (By.ID, "com.langlib.cee:id/fragment_gra_choice_questinx")
    gra_text_id = (By.ID, "com.langlib.cee:id/text_view")

    answer_a_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_a")
    answer_b_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_b")
    answer_c_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_c")
    answer_d_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_d")
    i_dont_know_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_e")

    gra_choose_sure_id = (By.ID, "com.langlib.cee:id/fragment_gra_choice_sure_tv")

    def get_gra_list_text(self):
        return self.getText(self.find_element(*self.gra_list_num_id))

    def get_gra_lists_nums(self):
        text = self.getText(self.find_element(*self.gra_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def choose_answer(self, answers=None):
        if answers.lower() == 'a':
            self.find_element(*self.answer_a_id).click()
        if answers.lower() == 'b':
            self.find_element(*self.answer_b_id).click()
        if answers.lower() == 'c':
            self.find_element(*self.answer_c_id).click()
        if answers.lower() == 'd':
            self.find_element(*self.answer_d_id).click()
        else:
            self.find_element(*self.i_dont_know_id).click()

    def click_gra_choose_sure(self):
        self.find_element(*self.gra_choose_sure_id).click()


if __name__ == "__main__":
    pass
