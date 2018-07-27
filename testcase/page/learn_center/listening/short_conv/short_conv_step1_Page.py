import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class SFFillAnswerPage(AllCommonEle, ItemLists):
    '''
    句子填充题目作答页
    '''
    page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    list_num_id = (By.ID, "com.langlib.cee:id/fragment_sen_fill_index_tv")
    audio_icon_id = (By.ID, "com.langlib.cee:id/fragment_sen_fill_detail_play_imagebtn")

    sen_id = (By.ID, "com.langlib.cee:id/text_view")
    answer_edit_classes = (By.CLASS_NAME, "android.widget.EditText")

    def get_senfill_list_text(self):
        return self.getText(self.find_element(*self.list_num_id))

    def get_senfill_lists_nums(self):
        text = self.getText(self.find_element(*self.list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = result[0]
        total_num = result[1]
        return current_num, total_num

    def click_senfill_audio_button(self):
        self.find_element(*self.audio_icon_id).click()
        sleep(0.5)

    def senfill_fill_answer(self, answers=None):
        answer_edit_ele = self.find_elements(*self.answer_edit_classes)
        for edit,answer in zip(answer_edit_ele, answers):
            edit.send_keys(answer)
        self.pressKeyCode("66")



if __name__ == "__main__":
    pass
