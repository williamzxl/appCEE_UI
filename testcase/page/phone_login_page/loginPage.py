from testcase.common.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    '''
    账号密码登录页面元素
    '''
    account_text = (By.LINK_TEXT, u'账号密码登录')
    account_id = (By.ID, "com.langlib.cee:id/account_login_account")
    account_del_id = (By.ID, "com.langlib.cee:id/account_login_account_delete_btn")
    pwd_id = (By.ID, "com.langlib.cee:id/account_login_password")
    eye_id = (By.ID, "com.langlib.cee:id/account_login_password_checkbox")
    tips_msg = r"用户名或密码错误"
    tips_msg_id = (By.ID, "com.langlib.cee:id/account_login_prompt")
    submit_id1 = (By.ID, "com.langlib.cee:id/account_login_btn")

    '''
    短信验证码登录界面
    '''
    sms_text = (By.LINK_TEXT, u'短信验证码登录')
    phone_id = (By.ID, "com.langlib.cee:id/account_login_message_account")
    phone_del_id = (By.ID, "com.langlib.cee:id/account_login_message_account_delete_btn")
    msgCode_id = (By.ID, "com.langlib.cee:id/account_login_message_validate_code")
    getCode_id = (By.ID, "com.langlib.cee:id/account_login_get_validate_code")
    submit_id2 = (By.ID, "com.langlib.cee:id/account_login_message_btn")

    def open(self, noReset=None):
        self.get(noReset)

    '''
    账号密码登录页面操作
    '''
    def click_account_text(self):
        self.find_element(*self.account_text).click()

    # def click_acocunt(self):
    #     self.find_element(*self.account_id).click()

    def input_account(self, username):
        self.find_element(*self.account_id).send_keys(username)

    def click_del_acount(self):
        self.find_element(*self.account_del_id).click()

    def input_password(self, password):
        self.find_element(*self.pwd_id).send_keys(password)

    def click_ac_lgbtn(self):
        self.find_element(*self.submit_id1).click()
    #
    #ele = login_page.find_element(*tips_msg_id)
    #print(ele.text)
    def get_tips_msg(self):
        return self.get_text(self.find_element(*self.tips_msg_id))

    '''
    短信验证码登录页面操作
    '''
    def click_sms_text(self):
        self.find_element(*self.sms_text).click()

    def input_phone(self):
        self.find_element(*self.phone_id)

    def click_del_phone(self):
        self.find_element(*self.phone_del_id).click()

    def click_get_code(self):
        self.find_element(*self.getCode_id).click()

    def click_ph_lgbtn(self):
        self.find_element(*self.submit_id2).click()


if __name__ == "__main__":
    test = LoginPage()
    test.open()