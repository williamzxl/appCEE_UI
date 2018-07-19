import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class WTChooseAnswerPage(AllCommonEle, ItemLists):
    '''
    单词听译题目作答页
    '''
    page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    list_num_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_index_tv")
    audio_icon_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_play_imagebtn")

    answer_a_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_a")
    answer_b_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_b")
    answer_c_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_c")
    answer_d_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_d")
    i_dont_know_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_e")

    next_button_ele_id = "com.langlib.cee:id/fragment_word_trans_next_tv"
    next_button_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_next_tv")

    def get_trans_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_words_trans_lists_nums(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_trans_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def choose_answer(self, answers=None):
        if answers == 'a':
            self.find_element(*self.answer_a_id).click()
        if answers == 'b':
            self.find_element(*self.answer_b_id).click()
        if answers == 'c':
            self.find_element(*self.answer_c_id).click()
        if answers == 'd':
            self.find_element(*self.answer_d_id).click()
        else:
            self.find_element(*self.i_dont_know_id).click()


if __name__ == "__main__":
    pass
