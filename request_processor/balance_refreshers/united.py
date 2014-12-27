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
base_url = "http://www.united.com/"

driver.get(base_url + "web/en-US/apps/account/account.aspx")

driver.find_element_by_id("ctl00_ContentInfo_SignIn_onepass_txtField").click()
driver.find_element_by_id("ctl00_ContentInfo_SignIn_onepass_txtField").send_keys(sys.argv[1])

driver.find_element_by_id("ctl00_ContentInfo_SignIn_password_txtPassword").click()
driver.find_element_by_id("ctl00_ContentInfo_SignIn_password_txtPassword").send_keys(sys.argv[2])

driver.find_element_by_id("ctl00_ContentInfo_SignInSecure").click()

time.sleep(2)

driver.get(base_url + "web/en-US/apps/account/account.aspx?SI=1")
miles = driver.find_element_by_xpath("//span[@id='ctl00_ContentInfo_AccountSummary_lblMileageBalanceNew']").text
print locale.atoi(miles)
driver.find_element_by_link_text(u"Sign Out").click()
