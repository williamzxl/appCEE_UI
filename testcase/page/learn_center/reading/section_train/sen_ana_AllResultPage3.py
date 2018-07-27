from appium.webdriver.webdriver import By
from testcase.page.common_page.word_lists_result import Word_Lists_ResultPage
from testcase.page.common_page.all_result_page import All_ResultPage
from testcase.page.learn_center.reading.sen_analysis.sen_ana_SingleResultPage2 import SAAnswerResultPage


class SAAllAnswerPage(Word_Lists_ResultPage, SAAnswerResultPage, All_ResultPage):
    sen_index_classes = (By.CLASS_NAME, 'com.langlib.cee:id/recy_item')

    def click_sen_index_num(self):
        self.find_element(*self.sen_index_classes).click()


if __name__ == "__main__":
    pass