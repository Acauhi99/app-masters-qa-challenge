from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

ROOT_DIR = Path(__file__).parent.parent
CHROME_DRIVER_NAME = 'chromedriver'
CHROME_DRIVER_PATH = ROOT_DIR / 'bin' / CHROME_DRIVER_NAME

def open_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_experimental_option("detach", True)
    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    try:
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        return browser
    except WebDriverException as e:
        print(f"Ocorreu um erro ao abrir o navegador: {e}")

def close_chrome_browser(browser):
    browser.quit()

if __name__ == '__main__':
    browser = open_chrome_browser('--headless')
    browser.get('https://www.google.com')

