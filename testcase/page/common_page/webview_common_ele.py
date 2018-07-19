import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.common.basePage import BasePage
from testcase.page.login_page.loginPage import LoginPage
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


class ItemLists(LoginPage):
    '''
    题目列表页面
    '''
    lists_ids = (By.ID, "com.langlib.cee:id/fragment_test_data_item_tv")
    next_button_ele_id = "com.langlib.cee:id/fragment_word_dic_next_tv"
    next_button_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_next_tv")
    finish_button_ele_id = "com.langlib.cee:id/fragment_word_dic_done_tv"
    finish_button_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_done_tv")
    learn_center_ele_class = "android.widget.TextView"
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    def get_all_list_ele(self):
        eles = self.find_elements(*self.lists_ids)
        return eles

    def get_list_num(self, driver, ele):
        regx = re.compile(r'(\d)+')
        text = driver.getText(ele)
        result = regx.search(text)
        return int(result.group())

    def click_one_list(self, driver, ele):
        ele.click()
        sleep(1)
        all_info = driver.page_source()
        print("ALL INFO:", all_info)
        # if self.next_button_ele_id in all_info:
        #     print("This is one word listening result page")
        #     return 1
        # if "{}".format(str(self.next_button_id).strip("(|)").split(',')[1]) in all_info:
        #     print("{}".format(str(self.next_button_id).strip("(|)").split(',')[1]))
        #     print("This is one word listening result page")
        #     return 1
        if self.finish_button_ele_id in all_info:
            print("This is the last result page")
            return 2
        # if "{}".format(str(self.finish_button_id).strip("(|)").split(',')[1]) in all_info:
        #     print("This is the last result page")
        #     return 2
        # if "{}".format(str(self.learn_center_class).strip("(|)").split(',')[1]) in all_info:
        #     print(str(self.learn_center_class).strip("(|)").split(',')[1])
        # # if self.getText(self.find_element(*self.learn_center_class)) in all_info:
        #     print("This is all word listening result page")
        #     return 3
        # if self.learn_center_ele_class in all_info:
        #     print("This is all word listening result page")
        #     return 3
        if '学习中心' in all_info:
            print("This is all word listening result page")
            return 3
        else:
            return 0


class AllCommonEle(BasePage):
    '''
    返回按钮相关操作
    '''
    back_btn_id = (By.ID, "com.langlib.cee:id/title_iframe_back_btn")
    dialog_tips_text_id = "com.langlib.cee:id/dialog_descripiton_tv"
    dialog_tips_text_id_ele = (By.ID, dialog_tips_text_id)
    dialog_sure_button = (By.ID, "com.langlib.cee:id/dialog_sure_button")
    dialog_cancel_button = (By.ID, "com.langlib.cee:id/dialog_cancel_button")

    def click_back_btn(self):
        self.find_element(*self.back_btn_id).click()

    def get_dialog_tips_text(self):
        return self.getText(self.find_element(*self.dialog_tips_text_id))

    def click_sure_button(self):
        if self.dialog_tips_text_id in self.page_source():
            return self.find_element(*self.dialog_sure_button).click()

    def click_cancel_button(self):
        if self.dialog_tips_text_id in self.page_source():
            return self.find_element(*self.dialog_cancel_button).click()


if __name__ == "__main__":
    pass
