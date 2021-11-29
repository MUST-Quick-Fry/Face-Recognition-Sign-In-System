import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def log_in():
    web.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/div/input').send_keys("admin")
    web.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div/input').send_keys("1234")
    sign_in_but = web.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/button')
    assert sign_in_but is not None
    sign_in_but.click()
    assert "http://127.0.0.1:8000/" in web.current_url
    ctr_panel = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/div')
    assert ctr_panel is not None
    ctr_panel.click()
    time.sleep(2)


def reissue():
    # web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/div').click()
    # time.sleep(2)
    retroa_but = web.find_element(By.XPATH, '//*[@id="main"]/section/aside/ul/div/li[2]/ul/div/li[2]')
    assert retroa_but is not None
    retroa_but.click()
    iframe = web.find_element(By.XPATH, '//*[@id="1003"]')
    assert iframe is not None
    web.switch_to.frame(iframe)
    before_reissue = web.find_element(By.XPATH, '//*[@id="container"]')
    before_reissue.screenshot("before_reissue.png")
    web.find_element(By.XPATH, '//*[@id="changelist-form"]/div[1]/button[1]').click()
    sel_sid = Select(web.find_element(By.XPATH, '//*[@id="id_sid"]'))
    num_sid = len(sel_sid.options)
    assert sel_sid is not None
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


if __name__ == '__main__':
    web = Chrome()
    web.get("http://127.0.0.1:8000/")
    log_in()
    sign_in_records('bef')
    reissue()
