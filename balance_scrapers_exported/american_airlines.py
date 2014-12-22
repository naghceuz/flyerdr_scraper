# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AmericanAirlines(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.aa.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_american_airlines(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(1)
        driver.get(self.base_url + "login/loginAccess.do")
#        time.sleep(1)
        driver.find_element_by_id("aa-loginForm.loginId").click()
        driver.find_element_by_id("aa-loginForm.loginId").send_keys("45T0XH8")
#        time.sleep(1)
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").send_keys("96844849")
#        time.sleep(1)
#        driver.find_element_by_id("pwd").submit()
        driver.find_element_by_name("_button_login").click()
        driver.find_element_by_id("pwd").click() # Wait until login page comes back up...
        driver.get(self.base_url + "homePage.do")
        currentbalance = driver.find_element_by_xpath("//div[@id='home-page-widgets']/div/div/div/p[4]").text
        driver.find_element_by_link_text(u"Logout »").click()
    
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
