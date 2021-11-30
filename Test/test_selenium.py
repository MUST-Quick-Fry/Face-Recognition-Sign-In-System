import time
from urllib.parse import urljoin
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def log_in():
    web.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/div/input').send_keys("admin")
    web.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div/input').send_keys("joininthegrouplvwnb")
    sign_in_but = web.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/button')
    assert sign_in_but is not None
    sign_in_but.click()
    assert "http://127.0.0.1:8000/" in web.current_url
    ctr_panel = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/div')
    assert ctr_panel is not None
    ctr_panel.click()
    time.sleep(2)


def go_to_iframe(id_num):
    iframe = web.find_element(By.XPATH, f'//*[@id="{id_num}"]')
    assert iframe is not None
    web.switch_to.frame(iframe)


def reissue():
    # web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/div').click()
    # time.sleep(2)
    retroa_but = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/ul/div/li[2]')
    assert retroa_but is not None
    retroa_but.click()
    go_to_iframe('1003')
    before_reissue = web.find_element(By.XPATH, '//*[@id="container"]')
    before_reissue.screenshot("before_reissue.png")
    web.find_element(By.XPATH, '//*[@id="changelist-form"]/div[1]/button[1]').click()
    sel_sid = Select(web.find_element(By.XPATH, '//*[@id="id_sid"]'))
    assert sel_sid is not None
    num_sid = len(sel_sid.options)
    sel_cid = Select(web.find_element(By.XPATH, '//*[@id="id_cid"]'))
    num_cid = len(sel_cid.options)
    assert sel_cid is not None
    '''test the function of add sign in'''
    for i in range(1, num_sid):
        for j in range(1, num_cid):
            if i == 1 and j == 2:
                continue
            elif i != 1 and j == num_cid - 1:
                break
            sel_sid = Select(web.find_element(By.XPATH, '//*[@id="id_sid"]'))
            sel_sid.select_by_index(i)
            sel_cid = Select(web.find_element(By.XPATH, '//*[@id="id_cid"]'))
            sel_cid.select_by_index(j)
            time.sleep(2)
            save_but = web.find_element(By.XPATH, '//*[@id="signin_form"]/div/div/button[2]')
            assert save_but is not None
            save_but.click()
            time.sleep(2)

    back_but = web.find_element(By.XPATH, '//*[@id="signin_form"]/div/div/button[1]')
    assert back_but is not None
    back_but.click()
    after_reissue = web.find_element(By.XPATH, '//*[@id="container"]')
    after_reissue.screenshot("after_reissue.png")
    web.switch_to.parent_frame()
    sign_in_records('aft')


def print_redord(sel, when):
    for i in range(len(sel.options)):
        sel.select_by_index(i)
        time.sleep(2)
        c1_bef_reissue = web.find_element(By.XPATH, '/html/body')
        c1_bef_reissue.screenshot(f"c{i + 1}_{when}.png")


def sign_in_records(when):
    sign_record_but = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/ul/div/li[1]')
    assert sign_record_but is not None
    sign_record_but.click()
    iframe = web.find_element(By.XPATH, '//*[@id="1002"]')
    assert iframe is not None
    web.switch_to.frame(iframe)
    dropdown = web.find_element(By.XPATH, '//*[@id="dropdown"]')
    sel = Select(dropdown)
    assert sel is not None
    print_redord(sel, when)
    web.switch_to.parent_frame()


def change_pwd():
    admin_btn = web.find_element(By.XPATH, '//*[@id="main"]/section/section/header/div/div[2]/div/button')
    assert admin_btn is not None
    admin_btn.click()
    source_body = web.find_element(By.XPATH, '/html/body')
    time.sleep(2)
    source_body.screenshot('admin_button.png')
    change_pwd_url = 'admin/password_change'
    web.get(urljoin(web.current_url, change_pwd_url))
    web.get_screenshot_as_file("change_pwd_page.png")
    # change_pwd_btn.click()
    old_pwd = web.find_element(By.XPATH, '//*[@id="password_form"]/div[1]/div/div/input')
    assert old_pwd is not None
    old_pwd.send_keys('1234')
    new_pwd = web.find_element(By.XPATH, '//*[@id="password_form"]/div[2]/div/div[1]/input')
    assert new_pwd is not None
    new_pwd.send_keys('joininthegrouplvwnb')
    confirm_pwd = web.find_element(By.XPATH, '//*[@id="password_form"]/div[3]/div/div/input')
    assert confirm_pwd is not None
    confirm_pwd.send_keys('joininthegrouplvwnb')
    web.save_screenshot('changing_pwd.png')
    click_btn = web.find_element(By.XPATH, '//*[@id="password_form"]/div[4]/div/button')
    assert click_btn is not None
    click_btn.click()
    time.sleep(2)
    web.get_screenshot_as_file("change_pwd_suc.png")


def sorted_by_students():
    retroa_but = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/ul/div/li[2]')
    assert retroa_but is not None
    retroa_but.click()
    go_to_iframe('1003')
    sign_in_list = web.find_element(By.XPATH, '//*[@id="changelist-form"]')
    assert sign_in_list is not None
    sign_in_list.screenshot('before_sorted.png')
    student_btn = web.find_element(By.XPATH, '//*[@id="result_list"]/thead/tr/th[3]/div[1]')
    assert student_btn is not None
    student_btn.click()
    web.implicitly_wait(2)
    sign_in_list = web.find_element(By.XPATH, '//*[@id="changelist-form"]')
    sign_in_list.screenshot('ascend_order.png')
    student_btn = web.find_element(By.XPATH, '//*[@id="result_list"]/thead/tr/th[3]/div[2]')
    student_btn.click()
    web.implicitly_wait(2)
    sign_in_list = web.find_element(By.XPATH, '//*[@id="changelist-form"]')
    sign_in_list.screenshot('descend_order.png')


def search_id_name(obj, style):
    retroa_but = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/ul/div/li[2]')
    assert retroa_but is not None
    retroa_but.click()
    go_to_iframe('1003')
    input_bar = web.find_element(By.XPATH, '//*[@id="changelist-search"]/div/div/input')
    assert input_bar is not None
    input_bar.send_keys(obj)
    search_btn = web.find_element(By.XPATH, '//*[@id="changelist-search"]/div/button')
    assert search_btn is not None
    sign_in_list = web.find_element(By.XPATH, '//*[@id="changelist-form"]')
    assert sign_in_list is not None
    sign_in_list.screenshot('before_search.png')
    search_btn.click()
    web.implicitly_wait(2)
    sign_in_list = web.find_element(By.XPATH, '//*[@id="changelist-form"]')
    assert sign_in_list is not None
    sign_in_list.screenshot(f'search_by_{style}.png')
    web.switch_to.parent_frame()


def add_obj(id_num, *args):
    num = int(id_num) - 1002
    obj_li = web.find_element(By.XPATH, f'//*[@id="home"]/div[1]/div/div/div[2]/div/div[{num}]')
    assert obj_li is not None
    obj_li.click()
    go_to_iframe(id_num)
    add_btn = web.find_element(By.XPATH, '//*[@id="changelist-form"]/div[1]/button[1]')
    assert add_btn is not None
    add_btn.click()
    web.get_screenshot_as_file(f'before_new_{dic[id_num]}_add.png')
    if id_num == '1006':
        name_input = web.find_element(By.XPATH, '//*[@id="id_name"]')
        assert name_input is not None
        name_input.send_keys(args[0])
        account_input = web.find_element(By.XPATH, '//*[@id="id_account"]')
        assert account_input is not None
        account_input.send_keys(args[0])
        pwd_input = web.find_element(By.XPATH, '//*[@id="id_pwd"]')
        assert pwd_input is not None
        pwd_input.send_keys(args[1])
        web.get_screenshot_as_file('teacher_add_pic.png')
        save_btn = web.find_element(By.XPATH, '//*[@id="teacher_form"]/div/div/button[4]')
        assert save_btn is not None
        save_btn.click()
        web.implicitly_wait(10)
        web.get_screenshot_as_file('teacher_add_suc.png')
    elif id_num == '1008':
        sel_tid = Select(web.find_element(By.XPATH, '//*[@id="id_tid"]'))
        assert sel_tid is not None
        sel_tid.select_by_index(1)
        name_input = web.find_element(By.XPATH, '//*[@id="id_name"]')
        assert name_input is not None
        name_input.send_keys(args[0])
        sel_weekday = Select(web.find_element(By.XPATH, '//*[@id="id_weekday"]'))
        assert sel_weekday is not None
        sel_weekday.select_by_index(int(args[1]))
        sta_t = web.find_element(By.XPATH, '//*[@id="id_start_time"]')
        assert sta_t is not None
        sta_t.send_keys(args[2])
        fin_t = web.find_element(By.XPATH, '//*[@id="id_finish_time"]')
        assert fin_t is not None
        fin_t.send_keys(args[3])
        save_btn = web.find_element(By.XPATH, '//*[@id="course_form"]/div/div/button[4]')
        assert save_btn is not None
        web.get_screenshot_as_file('course_add_pic.png')
        save_btn.click()
        web.implicitly_wait(10)
        web.get_screenshot_as_file('course_add_suc.png')


if __name__ == '__main__':
    web = Chrome()
    web.get("http://127.0.0.1:8000/")
    log_in()
    # sign_in_records('bef')
    # reissue()
    # change_pwd()
    # sorted_by_students()
    # search_id_name('hpl', 'name')
    # web.refresh()
    # time.sleep(2)
    # search_id_name('xxx', 'id')
    dic = {'1006': 'teacher', '1007': 'student', '1008': 'course_list'}
    # add_obj('1006', 'wyy', '123456')
    add_obj('1008', 'CN102', '2', '14:30:00', '16:20:00')
