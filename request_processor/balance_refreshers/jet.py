#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, atexit, sys

driver = webdriver.Firefox()
atexit.register(driver.quit)
driver.implicitly_wait(30)
base_url = "http://www.jetairways.com/"

driver.get(base_url + "/EN/US/Home.aspx")
driver.find_element_by_id("hplnkLoginTab").click()
time.sleep(2)
driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").click()
driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").click()
driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").clear()
driver.find_element_by_id("ctl00_ctl00_body_Login_txtJPNumber").send_keys(sys.argv[1])
driver.find_element_by_id("ctl00_ctl00_body_Login_txtPassword").clear()
driver.find_element_by_id("ctl00_ctl00_body_Login_txtPassword").send_keys(sys.argv[2])
driver.find_element_by_id("ctl00_ctl00_body_Login_btnSubmit").click()
time.sleep(2)
miles = driver.find_element_by_xpath("//td[text()='JPMiles Available:']/../td[2]").text
print miles
driver.find_element_by_link_text("JetPrivilege Logout").click()
