from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import allure


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    with allure.step("test_button_exist"):
        assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


def test_button_exist_2(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    with allure.step("test_button_exist2"):
        assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()


def test_me():
    with allure.step("test_me"):
        assert 1 == 1
