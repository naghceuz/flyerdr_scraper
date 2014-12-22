# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Delta(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.delta.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delta(self):
        driver = self.driver
        driver.get(self.base_url + "/custlogin/loginNow.action")
        time.sleep(1)
        driver.find_element_by_id("lblUser_Nm").click()
        driver.find_element_by_id("usernm").click()
        driver.find_element_by_id("usernm").clear()
        driver.find_element_by_id("usernm").send_keys("9015704332")
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("allanflyerdr")
        driver.find_element_by_id("submit1").click()
        time.sleep(1)
        driver.get(self.base_url + "/acctactvty/manageacctactvty.action")
        miles = driver.find_element_by_css_selector("div.textContainer4 > div.current_holder > h4.subText").text
        driver.find_element_by_css_selector("#header_logout > span.ui-button-text").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
