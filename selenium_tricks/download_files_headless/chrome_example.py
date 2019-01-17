import os
import time

from selenium.webdriver import Chrome, ChromeOptions


def enable_download_in_headless_chrome(driver, download_dir):
    # hack founded in
    # https://stackoverflow.com/questions/45631715/downloading-with-chrome-headless-and-selenium
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )

    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_dir},
    }
    driver.execute("send_command", params)


# set browser headless
options = ChromeOptions()
options.headless = True
# profile to download files automatically
options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)

# start firefox and connect into it
driver = Chrome(options=options)
enable_download_in_headless_chrome(driver, os.getcwd())
url = "http://localhost:5000/files"
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
