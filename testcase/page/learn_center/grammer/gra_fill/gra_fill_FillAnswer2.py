import re
# from time import sleep
# from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import AllCommonEle
from selenium.webdriver.common.by import By
from testcase.page.learn_center.grammer.gra_choice.gra_choice_ChooseAnswerPage1 import GCChooseAnswerPage


class GCAnswerResultPage(GCChooseAnswerPage, AllCommonEle):
    '''
    语法单选题目判定页
    '''
    answer_type_ele_id = "com.langlib.cee:id/gra_choice_drag_answer_type"
    answer_type_id = (By.ID, "com.langlib.cee:id/gra_choice_drag_answer_type")
    next_button_id = (By.ID, "com.langlib.cee:id/fragment_gra_choice_next_tv")
    words_list_button_id = (By.ID, "com.langlib.cee:id/fragment_gra_choice_word_tv")

    def get_answer_type(self,driver):
        if self.answer_type_ele_id in driver.page_source():
            return self.getText(self.find_element(*self.answer_type_id))

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_words_list_button(self):
        self.find_element(*self.words_list_button_id).click()


if __name__ == "__main__":
    pass