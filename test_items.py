from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_page_contains_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    cart_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert cart_button.is_displayed()
    time.sleep(30)
