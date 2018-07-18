import unittest
from utils.log import logger
from utils.file_reader import ExcelReader
from testcase.page.login_page.login_method import *


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.tips_msg = "用户名或密码错误"
        self.login_page = start_app(noReset=False)
        logger.info("setUp Start to open app")

    def test_login_success(self):
        u'''输入正确用户名和密码登录成功'''
        uname = "18519893004"
        pwd = '111111'
        screen_shot_name = "Login_success_page"
        self.login_success_page = login(self.login_page, uname, pwd, screen_shot_name)
        self.page_source = self.login_success_page.page_source()
        self.assertGreaterEqual(len(self.page_source), 1)

    def test_login_error_uname(self):
        u'''输入错误用户名和正确密码'''
        uname = "185198"
        pwd = '111111'
        screen_shot_name = "Login_with_error_uname"
        self.login_error_name_page = login(self.login_page, uname, pwd, screen_shot_name)
        tips_msg = self.login_error_name_page.get_tips_msg()
        self.assertEqual(self.tips_msg, tips_msg)

    def test_login_error_pwd(self):
        u'''输入正确用户名和错误密码'''
        uname = "18519893004"
        pwd = '11232434'
        screen_shot_name = "Login_with_error_pwd"
        self.login_error_pwd_page = login(self.login_page, uname, pwd, screen_shot_name)
        tips_msg = self.login_error_pwd_page.get_tips_msg()
        self.assertEqual(self.tips_msg, tips_msg)

    def test_login_error_uname_pwd(self):
        u'''输入错误用户名和错误密码'''
        uname = "185198"
        pwd = '111sdfsdg'
        screen_shot_name = "Login_with_error_uname_pwd"
        self.login_error_name_pwd_page = login(self.login_page, uname, pwd, screen_shot_name)
        tips_msg = self.login_error_name_pwd_page.get_tips_msg()
        self.assertEqual(self.tips_msg, tips_msg)

    def tearDown(self):
        self.login_page.quit()
        logger.info("Close the app")


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    # unittest.TextTestRunner().run(suite)
    unittest.main()