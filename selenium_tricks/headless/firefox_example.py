#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver


# set browser headless
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
# navigate to site and print source page
driver.get("http://example.com/")
print(driver.page_source)
driver.quit()
