import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import open_chrome_browser, close_chrome_browser

live_server_url = 'https://www.codental.com.br/login'

@pytest.mark.functional
def test_login_page_open_ok():
    browser = open_chrome_browser()
    browser.get(live_server_url)
    body = browser.find_element(By.TAG_NAME, 'body')
    assert 'Entre com sua conta' in body.text
    close_chrome_browser(browser)

@pytest.mark.functional
def test_entrar_button_without_email():
    browser = open_chrome_browser()
    browser.get(live_server_url)

    entrar_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="new_professional"]/div[4]/input'))
    )
    entrar_button.click()

    is_still_on_login_page = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="new_professional"]/div[4]/input'))
    )

    assert is_still_on_login_page is not None
    assert browser.current_url == live_server_url

    close_chrome_browser(browser)

@pytest.mark.functional
def test_forgot_password_link():
    browser = open_chrome_browser()
    browser.get(live_server_url)

    forgot_password_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Esqueceu sua senha?'))
    )

    forgot_password_link.click()
    
    WebDriverWait(browser, 10).until(
        EC.url_to_be('https://www.codental.com.br/password/new')
    )

    assert browser.current_url == 'https://www.codental.com.br/password/new', f"Expected URL to be 'https://www.codental.com.br/password/new' but got '{browser.current_url}'"
    
    close_chrome_browser(browser)