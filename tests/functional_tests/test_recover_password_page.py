import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import open_chrome_browser, close_chrome_browser

live_server_url = 'https://www.codental.com.br/password/new'

@pytest.mark.functional
def test_recover_password_page_open_ok():
    browser = open_chrome_browser('--headless')
    browser.get(live_server_url)
    body = browser.find_element(By.TAG_NAME, 'body')
    assert 'Recuperar senha' in body.text
    close_chrome_browser(browser)

@pytest.mark.functional
def test_enviar_button_without_email():
    browser = open_chrome_browser()
    browser.get(live_server_url)

    enviar_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="new_professional"]/div[2]/input'))
    )
    enviar_button.click()

    is_still_on_recover_password_page = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="new_professional"]/div[2]/input'))
    )

    assert is_still_on_recover_password_page is not None
    assert browser.current_url == live_server_url

    close_chrome_browser(browser)

@pytest.mark.functional
def test_enviar_button_with_not_valid_email():
    browser = open_chrome_browser()
    browser.get(live_server_url)

    email_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'professional_email'))
    )
    email_input.send_keys('not_valid_email')

    enviar_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="new_professional"]/div[2]/input'))
    )
    enviar_button.click()

    is_still_on_recover_password_page = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="new_professional"]/div[2]/input'))
    )

    assert is_still_on_recover_password_page is not None
    assert browser.current_url == live_server_url

    close_chrome_browser(browser)