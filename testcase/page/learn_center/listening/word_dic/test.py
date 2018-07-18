from testcase.page.learn_center.listening.word_dic.word_listening_all_resultPage4 import WLAllAnswerPage
from testcase.interface.sysListening.answer import get_all_answer

login_page = WLAllAnswerPage()
login_page.open(noReset=True)
eles = login_page.get_all_list_ele()
for i in eles:
    num = login_page.get_list_num(login_page, i)
    result = login_page.click_one_list(login_page, i)
    print(num , result)