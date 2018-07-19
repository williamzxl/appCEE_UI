import re
from testcase.page.login_page.loginPage import LoginPage
from selenium.webdriver.common.by import By
from testcase.interface.sysListening.answer import get_all_answer, right_answer, wrong_answer
# from selenium.webdriver.common.keys import Keys


class WLLists(LoginPage):
    '''
    单词听写列表
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
        all_info = driver.page_source()
        print("ALL INFO:", all_info)
        if self.next_button_ele_id in all_info:
            print("This is one word listening result page")
            return 1
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
        if "学习中心" in all_info:
            print("This is all word listening result page")
            return 3
        else:
            return 0


if __name__ == "__main__":
    login_page = WLLists()
    login_page.open(noReset=True)
    eles = login_page.get_all_list_ele()
    for i in eles:
        num = login_page.get_list_num(login_page, i)
        print(get_all_answer(list=num))
        if login_page.click_one_list(login_page, i) != 0:
            pass
