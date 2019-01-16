from selenium.webdriver import Firefox, FirefoxProfile
import os
import time

# profile to download some mime types automatically
profile = FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'application/octet-stream')
# start firefox and connect into it
driver = Firefox(firefox_profile=profile)
url = 'http://the-internet.herokuapp.com/download'
# navigate to the site
driver.get(url)
filename = 'some-file.txt'
# get "a" element and click
driver.find_element_by_css_selector(f'a[href $= "{filename}"]').click()
# wait download to finish
time.sleep(3)
# close firefox
driver.quit()
