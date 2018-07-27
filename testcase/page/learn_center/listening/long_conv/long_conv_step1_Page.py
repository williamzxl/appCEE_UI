import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class SC_Step1_Page(AllCommonEle, ItemLists):
    '''
    短对话第一步选择关键词
    '''
    page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    list_num_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_index_tv")

    step_desc = (By.ID, "com.langlib.cee:id/fragment_short_conv_step_des")
    question_id = (By.ID, "com.langlib.cee:id/conversation_question")
    answer_a = (By.ID, "com.langlib.cee:id/option_a")
    answer_b = (By.ID, "com.langlib.cee:id/option_b")
    answer_c = (By.ID, "com.langlib.cee:id/option_c")

    short_conv_sure_id = (By.ID, "com.langlib.cee:id/fragment_short_conv_sure_tv")
    short_conv_next_id = (By.ID, "com.langlib.cee:id/fragment_short_conv_next_tv")

    def get_step_desc(self):
        return self.getText(self.find_element(*self.step_desc))

    def get_short_conv_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_short_conv_lists_nums(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def mark_words(self):
        self.find_element(*self.question_id).click()
        self.find_element(*self.answer_a).click()
        self.find_element(*self.answer_b).click()
        self.find_element(*self.answer_c).click()

    def click_short_conv_step1_sure(self):
        self.find_element(*self.short_conv_sure_id).click()

    def click_short_conv_step1_next(self):
        self.find_element(*self.short_conv_next_id).click()


if __name__ == "__main__":
    pass
