import time
import unittest

from ..Init import InitDriver
from syg_test.management.TestModule import TestModule

home_page_url = 'http://47.94.123.58:2333/admin/login'

browser = InitDriver.set_up_locally_chrome()
sleep_time = 2

class TryLogin(unittest.TestCase):
    global browser
    TestModule.test_login("13800001111", "3131321", browser, home_page_url)
    time.sleep(sleep_time)

    TestModule.test_get_pass("51013722@qq.com", browser)
    time.sleep(sleep_time)

    TestModule.test_login("13800001111", "12345678", browser)
    time.sleep(sleep_time)

    TestModule.test_dashboard()
    time.sleep(sleep_time)

    '''
    mng_user = browser.find_element_by_css_selector('.sidebar-menu li:first-child a')
    mng_user.click()
    
    time.sleep(4)
    
    search_customername = browser.find_element_by_css_selector('#customerName');
    search_phonenumber = browser.find_element_by_css_selector('#search-form .row > .form-group:nth-child(2) input[type="text"]');
    search_btn = browser.find_element_by_css_selector('#search')
    search_customername.send_keys('sko')
    search_btn.click()
    
    time.sleep(4)
    
    search_customername.clear();
    search_phonenumber.send_keys(180)
    search_btn.click()
    
    time.sleep(10)
   '''



if __name__ == '__main__':
    unittest.main()