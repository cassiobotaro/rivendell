# Download file using selenium

## Problem

Crawl a website and download some content using browser headless.


## Discuss

In firefox, we have to create a user profile and configure the directory where the files
will be stored. We should also tell firefox to download certain types of files without asking the user.

```python
# profile to download some mime types automatically
profile = FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.dir', os.getcwd())
# you can select multiple types of files by separating them with commas
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'text/plain,image/jpeg')
# start firefox and connect into it
driver = Firefox(options=options, firefox_profile=profile)
```

In chrome, we also set the directory where the files will be stored and don't prompt for download.

```python
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
```

Unfornately we have to hack to make it work on headless mode.

```python
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
```

Another thing is that only works on newer versions of google chrome.

## How to run

`python firefox_example.py`

or

`python chrome_example.py`
