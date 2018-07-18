from selenium.webdriver.common.by import By
# from testcase.page.login_page.loginPage import LoginPage
from testcase.page.learn_center.listening.word_dic.word_listening_answerPage2 import WLFillAnswerPage


class WLAnswerResultPage(WLFillAnswerPage):
    '''
    单词听写题目判定页
    '''
    answer_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_word")
    audio_icon_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_word_phsymbol")
    word_CN_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_word_translate")
    next_button_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_next_tv")
    finish_button_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_done_tv")

    def click_next_button(self):
        self.find_element(*self.next_button_id).click()

    def click_finish_button(self):
        self.find_element(*self.finish_button_id).click()


if __name__ == "__main__":
    pass