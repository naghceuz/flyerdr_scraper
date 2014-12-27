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
base_url = "https://www.aa.com/"
    
driver.get(base_url)
time.sleep(1)
driver.get(base_url + "login/loginAccess.do")

driver.find_element_by_id("aa-loginForm.loginId").click()
driver.find_element_by_id("aa-loginForm.loginId").send_keys(sys.argv[1])

driver.find_element_by_id("pwd").click()
driver.find_element_by_id("pwd").send_keys(sys.argv[2])

driver.find_element_by_name("_button_login").click()
driver.find_element_by_id("pwd").click() # Wait until login page comes back up...
driver.get(base_url + "homePage.do")
miles = driver.find_element_by_xpath("//div[@id='home-page-widgets']/div/div/div/p[4]").text
print miles
driver.find_element_by_link_text(u"Logout »").click()

