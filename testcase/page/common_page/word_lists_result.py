from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_trans.word_translating_resultPage2 import WTAnswerResultPage


class Word_Lists_ResultPage(WTAnswerResultPage):
    '''
    单词听译结果展示页
    '''
    time_id = (By.ID, "com.langlib.cee:id/fragment_list_top_view_time")
    grade_id = (By.ID, "com.langlib.cee:id/fragment_list_top_view_grade")
    answer_lists_ids = (By.ID, "com.langlib.cee:id/fragment_word_dic_list_item_rl")
    error_answers_ids = (By.ID, "com.langlib.cee:id/fragment_word_dic_list_item_type")
    star_ids = (By.ID, "com.langlib.cee:id/fragment_word_profi_tv")
    start1_id = (By.ID, "com.langlib.cee:id/popwindow_word_profi_star1")
    start2_id = (By.ID, "com.langlib.cee:id/popwindow_word_profi_star2")
    start3_id = (By.ID, "com.langlib.cee:id/popwindow_word_profi_star3")
    learn_center_class = (By.CLASS_NAME, "android.widget.TextView")

    def get_time(self):
        return self.getText(self.find_element(*self.time_id))

    def get_grade(self):
        return self.getText(self.find_element(*self.grade_id))

    def get_starts_nums(self):
        starts_nums = self.find_elements(*self.star_ids)
        starts = []
        for num in starts_nums:
            starts.append(self.getText(num))
        return starts

    def list_all_starts(self):
        stars_nums = self.find_elements(*self.star_ids)
        return stars_nums

    def click_star(self, ele):
        ele.click()

    def choose_star(self, star=3):
        if star == 1:
            self.find_element(*self.start1_id).click()
        if star == 2:
            self.find_element(*self.start2_id).click()
        else:
            self.find_element(*self.start3_id).click()

    def click_learn_center(self):
        self.find_element(*self.learn_center_class).click()


if __name__ == "__main__":
    pass