#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://example.com/")
print(driver.page_source)
driver.quit()
