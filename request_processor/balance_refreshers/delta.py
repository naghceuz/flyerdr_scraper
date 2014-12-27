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
base_url = "https://www.delta.com/"

driver.get(base_url + "/custlogin/loginNow.action")
time.sleep(1)
driver.find_element_by_id("lblUser_Nm").click()
driver.find_element_by_id("usernm").click()
driver.find_element_by_id("usernm").clear()
driver.find_element_by_id("usernm").send_keys("9015704332")
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("allanflyerdr")
driver.find_element_by_id("submit1").click()
time.sleep(1)
driver.get(base_url + "/acctactvty/manageacctactvty.action")
miles = driver.find_element_by_css_selector("div.textContainer4 > div.current_holder > h4.subText").text
print miles
driver.find_element_by_css_selector("#header_logout > span.ui-button-text").click()
