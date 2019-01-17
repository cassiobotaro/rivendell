import os
import time

from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions

# set browser headless
options = FirefoxOptions()
options.headless = True
# profile to download some mime types automatically
profile = FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.dir', os.getcwd())
# you can select multiple types of files by separating them with commas
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'text/plain,image/jpeg')
# start firefox and connect into it
driver = Firefox(options=options, firefox_profile=profile)
url = 'http://localhost:5000/files'
# warning: doing driver.get directly in the files downloads URL
# causes a strange crash
# navigate to the site
driver.get(url)
# get "a" element and click
driver.find_element_by_css_selector('a[href $= "some_text.txt"]').click()
# download image also
driver.find_element_by_css_selector('a[href $= "lena.jpg"]').click()
# wait downloads to finish
time.sleep(3)
# close firefox
driver.quit()
