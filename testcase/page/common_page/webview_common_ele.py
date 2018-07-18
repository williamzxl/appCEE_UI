from selenium.webdriver.common.by import By
from testcase.common.basePage import BasePage
# from testcase.page.login_page.loginPage import LoginPage
# from selenium.webdriver.common.keys import Keys


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
        self.find_element(*self.back_btn_id)

    def get_dialog_tips_text(self):
        return self.getText(self.find_element(*self.dialog_tips_text_id))

    def click_sure_button(self):
        if self.dialog_tips_text_id in self.page_source():
            return self.find_element(*self.dialog_sure_button)

    def click_cancel_button(self):
        if self.dialog_tips_text_id in self.page_source():
            return self.find_element(*self.dialog_cancel_button)


if __name__ == "__main__":
    pass
