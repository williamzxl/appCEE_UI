import re
from selenium.webdriver.common.by import By
from testcase.page.common_page.webview_common_ele import ItemLists, AllCommonEle
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class SAChooseAnswerPage(AllCommonEle, ItemLists):
    '''
    句子分析题目作答页
    '''
    page_title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
    total_list_num_id = (By.ID, "com.langlib.cee:id/fragment_sen_analysis_child_tip")
    sen_text_id = (By.ID, 'com.langlib.cee:id/fragment_sen_analysis_child_questtext')
    item_list_des_id = (By.ID, "com.langlib.cee:id/quest_analysis_step")

    answer_radio_button_classes = (By.CLASS_NAME, 'android.widget.RadioButton')
    mask_answer_id = (By.ID, "com.langlib.cee:id/sen_analysis_mask_answer")
    fill_CN_answer_classes = (By.CLASS_NAME, 'android.widget.EditText')
    answer_sure_id = (By.ID, "com.langlib.cee:id/senavaly_quest_sure")

    gra_tips_id = (By.ID, "com.langlib.cee:id/quest_analysis_group_gra_tip")
    sen_ana_next_button_id = (By.ID, 'com.langlib.cee:id/senavaly_quest_next_quest')
    sen_ana_done_button_id = (By.ID, 'com.langlib.cee:id/senavaly_quest_done')

    def get_sen_ana_list_text(self):
        return self.getText(self.find_element(*self.total_list_num_id))

    def get_sen_text_text(self):
        return self.getText(self.find_element(*self.sen_text_id))

    def get_sen_ana_lists_nums(self):
        text = self.getText(self.find_element(*self.total_list_num_id))
        text_regx = re.compile(r'.*\((\d+)\/(\d+)')
        result = text_regx.search(text).groups()
        current_num = int(result[0])
        total_num = int(result[1])
        return current_num, total_num

    def get_step_text(self):
        return self.getText(self.find_element(*self.item_list_des_id))

    def get_step_nums(self):
        text = self.getText(self.find_element(*self.item_list_des_id))
        text_regx = re.compile(r'\((\d+)\/(\d+)\)')
        result = text_regx.search(text).groups()
        current_step = int(result[0])
        total_step = int(result[1])
        return current_step, total_step

    def sen_ana_choose_answer(self, answer=None, right=True):
        answers_ele = self.find_elements(*self.answer_radio_button_classes)
        all_answer_CN = []
        for a in answers_ele:
            all_answer_CN.append(self.getText(a))
            if right:
                if self.getText(a) == answer:
                    a.click()
            else:
                if self.getText(a) != answer:
                    a.click()
        if answer not in all_answer_CN:
            print("正确答案不存在")
            self.save_screen_shot("正确答案不存在",file_name="句子分析不存在正确答案")
            for a in answers_ele:
                if self.getText(a) != answer:
                    a.click()


    def click_to_check_CN(self):
        self.find_element(*self.mask_answer_id).click()

    def fill_CN_answer(self, answer):
        ele = self.find_element(*self.fill_CN_answer_classes)
        ele.send_keys(answer)

    def click_sen_ana_sure_button(self):
        self.find_element(*self.answer_sure_id).click()

    def click_sen_ana_next_question(self):
        self.find_element(*self.sen_ana_next_button_id).click()

    def click_sen_ana_finish_button(self):
        self.find_element(*self.sen_ana_done_button_id).click()


if __name__ == "__main__":
    pass
