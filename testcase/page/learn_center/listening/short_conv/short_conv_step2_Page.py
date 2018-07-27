from testcase.page.common_page.word_lists_result import Word_Lists_ResultPage
# from testcase.page.common_page.webview_common_ele import AllCommonEle, ItemLists
from testcase.page.common_page.all_result_page import All_ResultPage
from testcase.page.learn_center.listening.sen_fill.sen_fill_resultPage2 import SFAnswerResultPage


class SFAllAnswerPage(SFAnswerResultPage, Word_Lists_ResultPage, All_ResultPage):
    pass


if __name__ == "__main__":
    pass