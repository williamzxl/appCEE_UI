import re
from time import sleep
from selenium.webdriver.common.by import By
from testcase.page.learn_center.listening.word_dic.word_listening_resultPage3 import WLAnswerResultPage
from testcase.interface.sysListening.word_dict.answer import get_all_answer, right_answer, wrong_answer

account_text = (By.LINK_TEXT, u'账号密码登录')
account_id = (By.ID, "com.langlib.cee:id/account_login_account")
account_del_id = (By.ID, "com.langlib.cee:id/account_login_account_delete_btn")
pwd_id = (By.ID, "com.langlib.cee:id/account_login_password")
eye_id = (By.ID, "com.langlib.cee:id/account_login_password_checkbox")
tips_msg = r"用户名或密码错误"
tips_msg_id = (By.ID, "com.langlib.cee:id/account_login_prompt")
submit_id1 = (By.ID, "com.langlib.cee:id/account_login_btn")

danci564 = (By.ID, "com.langlib.cee:id/fragment_test_data_item_tv")
back_btn = (By.ID, "com.langlib.cee:id/title_iframe_back_btn")
# com.langlib.cee:id/title_iframe_back_btn
#com.langlib.cee:id/dialog_sure_button
back_sure_btn = (By.ID, "com.langlib.cee:id/dialog_sure_button")
back_text_btn = (By.ID, "com.langlib.cee:id/dialog_descripiton_tv")

click_next_button_id = (By.ID, "com.langlib.cee:id/fragment_word_dic_next_tv")

login_page = WLAnswerResultPage()
login_page.open(noReset=True)
sleep(20)
eles = login_page.find_elements(*danci564)
print(eles)
print(eles[0])
# for ele in eles:
#     print(ele)
for ele in eles[12:13]:
    regx = re.compile(r'(\d)+')
    text = login_page.getText(ele)
    result = regx.search(text)
    print(int(result.group()))
    answers = get_all_answer(list=int(result.group()))
    # answers = get_all_answer(list=1000)
    ele.click()

    curr, total = login_page.get_words_list_num()
    print(curr, total)
    for i in range(int(curr), int(total)+1):
        login_page.click_audio_button()
        login_page.save_screen_shot(page_name="Word", file_name="播放截图")
        current_right_answer = right_answer(answers, i)
        current_wrong_answer = wrong_answer(answers, i)
        print(current_right_answer, current_wrong_answer)
        try:
            login_page.hideKeyboard()
        except:
            login_page.save_screen_shot("No KEYBoard")
        login_page.fill_answer(current_right_answer)
        sleep(1)
        login_page.pressKeyCode("66")
        sleep(1)
        login_page.save_screen_shot("题目判定页")
        login_page.click_next_button()
    # login_page.send_keys(Keys.ENTER)
#     login_page.quit()
    # try:
    #     login_page.find_element(*back_btn).click()
    #     sleep(20)
    #     print("Back")
    # except SyntaxError:
    #     print("result page")
    # back_ele = login_page.find_element(*back_text_btn)
    # print(login_page.getText(back_ele))
    # try:
    #     print(login_page.page_source())
    #     login_page.find_element(*back_sure_btn).click()
    # except:
    #     print("hhh")