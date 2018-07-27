import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
from testcase.page.learn_center.listening.short_conv.short_conv_step1_Page import SC_Step1_Page
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class SC_Step2_Page(SC_Step1_Page):
    '''
    短对话训练第二步做题步骤
    '''
    audio_icon_id = (By.ID, "com.langlib.cee:id/frame_audio_conv_imageview")
    current_time_id = (By.ID, "com.langlib.cee:id/frame_audio_conv_current_time")
    total_time_id = (By.ID, "com.langlib.cee:id/frame_audio_conv_total_time")

    answer_a_id = (By.ID, "com.langlib.cee:id/option_a_no")
    answer_b_id = (By.ID, "com.langlib.cee:id/option_b_no")
    answer_c_id = (By.ID, "com.langlib.cee:id/option_c_no")

    item_text_class = (By.CLASS_NAME, "android.widget.TextView")
    short_conv_done_id = (By.ID, "com.langlib.cee:id/fragment_short_conv_done_tv")
    short_conv_answer_next_id = (By.ID, "com.langlib.cee:id/fragment_short_conv_answer_next_tv")

    def click_audio_icon(self):
        self.find_element(*self.audio_icon_id).click()

    def get_current_time(self):
        return self.getText(self.find_element(*self.current_time_id))

    def get_total_time(self):
        return self.getText(self.find_element(*self.total_time_id))

    def check_audio_play(self, curr, total):
        return True if curr == total else False

    def choose_answer(self, answer):
        if answer.upper() == 'A':
            self.find_element(*self.answer_a_id).click()
        if answer.upper() == 'B':
            self.find_element(*self.answer_b_id).click()
        if answer.upper() == 'C':
            self.find_element(*self.answer_c_id).click()

    def click_short_conv_step2_sure(self):
        self.find_element(*self.short_conv_done_id).click()

    '''
    第二步结果页
    '''
    def click_play(self):
        self.find_elements(*self.item_text_class)[0].click()

    def click_conv_text(self):
        self.find_elements(*self.item_text_class)[1].click()

    def click_conv_answer(self):
        self.find_elements(*self.item_text_class)[2].click()

    def click_short_conv_step2_next(self):
        self.find_element(*self.short_conv_answer_next_id).click()

    # def click_words_list_button(self):
    #     self.find_element(*self.word_list_button_id).click()


if __name__ == "__main__":
    pass