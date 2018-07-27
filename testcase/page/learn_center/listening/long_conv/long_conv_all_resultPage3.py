from time import sleep
from testcase.page.common_page.word_lists_result import Word_Lists_ResultPage
# from testcase.page.common_page.webview_common_ele import AllCommonEle, ItemLists
from testcase.page.common_page.all_result_page import All_ResultPage
from testcase.page.learn_center.listening.short_conv.short_conv_step2_Page import SC_Step2_Page


class SCAllAnswerPage(SC_Step2_Page, Word_Lists_ResultPage, All_ResultPage):
    pass
    # def click_one_list(self, driver, ele):
    #     ele.click()
    #     sleep(1)
    #     all_info = driver.page_source()
    #     print("ALL INFO:", all_info)
    #     mark_step = driver.get_step_desc()
    #     if mark_step.split(":") == "第一步":
    #         return 5
    #     if mark_step.split(":") == "第二步":
    #         return 6


if __name__ == "__main__":
    pass