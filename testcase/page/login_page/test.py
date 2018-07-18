from testcase.page.login_page.loginPage import LoginPage
from testcase.common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

account_text = (By.LINK_TEXT, u'账号密码登录')
account_id = (By.ID, "com.langlib.cee:id/account_login_account")
account_del_id = (By.ID, "com.langlib.cee:id/account_login_account_delete_btn")
pwd_id = (By.ID, "com.langlib.cee:id/account_login_password")
eye_id = (By.ID, "com.langlib.cee:id/account_login_password_checkbox")
tips_msg = r"用户名或密码错误"
tips_msg_id = (By.ID, "com.langlib.cee:id/account_login_prompt")
submit_id1 = (By.ID, "com.langlib.cee:id/account_login_btn")

login_page = LoginPage()
login_page.open()
sleep(20)
login_page.find_element(*account_id).send_keys(123)
login_page.find_element(*pwd_id).send_keys(123)
login_page.find_element(*submit_id1).click()

ele = login_page.find_element(*tips_msg_id)
print(ele.text)