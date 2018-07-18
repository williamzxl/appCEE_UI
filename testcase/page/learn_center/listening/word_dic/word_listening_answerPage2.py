import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import AllCommonEle
from testcase.page.learn_center.listening.word_dic.word_listening_listsPage1 import WLLists
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class WLFillAnswerPage(AllCommonEle, WLLists):
    '''
    单词听写题目作答页
    '''
    page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    list_num_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_index_tv")
    audio_icon_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_detail_play_audio_btn")
    input_btn_class = (By.CLASS_NAME, "android.widget.EditText")
    # back_btn_id = (By.ID, "com.langlib.cee:id/title_iframe_back_btn")
    # dialog_tips_text_id = "com.langlib.cee:id/dialog_descripiton_tv"
    # dialog_tips_text_id_ele = (By.ID, "com.langlib.cee:id/dialog_descripiton_tv")
    # dialog_sure_button = (By.ID, "com.langlib.cee:id/dialog_sure_button")
    # dialog_cancel_button = (By.ID, "com.langlib.cee:id/dialog_cancel_button")

    # def click_back_btn(self):
    #     self.find_element(*self.back_btn_id)
    #
    # def get_dialog_tips_text(self):
    #     return self.getText(self.find_element(*self.dialog_tips_text_id))
    #
    # def click_sure_button(self):
    #     if self.dialog_tips_text_id in self.page_source():
    #         return self.find_element(*self.dialog_sure_button)
    #
    # def click_cancel_button(self):
    #     if self.dialog_tips_text_id in self.page_source():
    #         return self.find_element(*self.dialog_cancel_button)

    def get_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_words_list_num(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def fill_answer(self, answer=None):
        self.find_element(*self.input_btn_class).send_keys(answer)
        # self.send_keys(Keys.ENTER)


if __name__ == "__main__":
    pass
