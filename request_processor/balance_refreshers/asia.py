#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, atexit, sys
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

driver = webdriver.Firefox()
atexit.register(driver.quit)
driver.implicitly_wait(30)
base_url = "http://www.asiamiles.com/"

driver.get(base_url + "am/en/account")

driver.find_element_by_id("txtMbrID").click()
driver.find_element_by_id("txtMbrID").send_keys(sys.argv[1])

driver.find_element_by_id("txtMbrPIN").click()
driver.find_element_by_id("txtMbrPIN").send_keys(sys.argv[2])

driver.save_screenshot('/home/ubuntu/asia_screenshot.png')
driver.find_element_by_id("txtMbrPIN").send_keys(Keys.RETURN)

time.sleep(2)

#driver.get(base_url + "am/en/account")
miles = driver.find_element_by_css_selector("div.logined_element > div:nth-of-type(2) > span").text
print locale.atoi(miles)
driver.find_element_by_id("btn_login").click()
