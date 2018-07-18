from testcase.page.login_page.loginPage import LoginPage
from time import sleep
from utils.log import logger


def start_app(noReset=None):
    login_page = LoginPage()
    login_page.open(noReset)
    sleep(20)
    logger.info("Start_app success")
    return login_page


def login(login_page, uname, pwd, screen_shot_name=None):
    login_page.input_account(uname)
    login_page.input_password(pwd)
    login_page.click_ac_lgbtn()
    logger.info("Login")
    sleep(20)
    login_page.save_screen_shot(page_name="LoginPage", file_name=screen_shot_name)
    return login_page

#
# def login_success(uname, pwd):
#     login_page = login(uname, pwd, "Login_success_page")
#     sleep(30)
#     page_source = login_page.page_source()
#     # login_page.quit()
#     return page_source
#
#
# def login_fail_error_uname(error_uname, pwd):
#     login_page = login(error_uname, pwd, screen_shot_name="Login_with_error_uname")
#     sleep(20)
#     tips_msg = login_page.get_tips_msg()
#     # login_page.quit()
#     return tips_msg
#
#
# def login_fail_error_pwd(uname, error_pwd):
#     login_page = login(uname, error_pwd,  screen_shot_name="Login_with_error_pwd")
#     sleep(20)
#     tips_msg = login_page.get_tips_msg()
#     # login_page.quit()
#     return tips_msg
#
#
# def login_fail_error_uname_error_pwd(error_uname, error_pwd):
#     login_page = login(error_uname,error_pwd,  screen_shot_name="Login_with_error_uname_error_pwd")
#     sleep(20)
#     tips_msg = login_page.get_tips_msg()
#     # login_page.quit()
#     return tips_msg
#
# def run_test():
#     tips_msg = "用户名或密码错误"
#     success = login_success(18519893004,111111)
#     print(success)
#     error_uname = login_fail_error_uname(18519893, 111111)
#     if error_uname == tips_msg:
#         print("Test error name PASS")
#     error_pwd = login_fail_error_pwd(18519893004, 8999393)
#     if error_pwd == tips_msg:
#         print("Test error pwd PASS")
#     error_uname_error_pwd = login_fail_error_uname_error_pwd(123, 123)
#     if error_uname_error_pwd == tips_msg:
#         print("Test error uname error pwd PASS")
#     else:
#         print("Check")


# run_test()