import re
# from time import sleep
# from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import AllCommonEle
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_trans.word_translating_ChooseAnswerPage import WTChooseAnswerPage


class WTAnswerResultPage(WTChooseAnswerPage, AllCommonEle):
    '''
    单词听译题目判定页
    '''
    answer_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_word")
    audio_icon_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_word_phsymbol")
    next_button_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_next_tv")
    finish_button_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_done_tv")

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_finish_button(self):
        self.find_element(*self.finish_button_id).click()


if __name__ == "__main__":
    pass