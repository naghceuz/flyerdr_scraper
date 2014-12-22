# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class JetAirways(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.jetairways.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_jet_airways(self):
        driver = self.driver
        driver.get(self.base_url + "/EN/US/Home.aspx")
        driver.find_element_by_id("hplnkLoginTab").click()
        time.sleep(2)
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").click()
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").click()
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").clear()
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").send_keys("184223270")
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtPassword").clear()
        driver.find_element_by_id("ctl00_ctl00_body_Login_txtPassword").send_keys("owen1992")
        driver.find_element_by_id("ctl00_ctl00_body_Login_btnSubmit").click()
        time.sleep(2)
        miles = driver.find_element_by_xpath("//td[text()='JPMiles Available:']/../td[2]").text
        driver.find_element_by_link_text("JetPrivilege Logout").click()
    
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
