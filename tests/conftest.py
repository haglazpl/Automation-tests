import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Setup driver and settings before each test
    print("Creating chrome driver")
    my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    my_driver.set_window_size(1936, 1056)
    my_driver.get("https://alan-systems.com/en/")
    check_if_page_is_in_polish_lang(my_driver)
    my_driver.implicitly_wait(2)
    yield my_driver

    # Setup driver and settings after each test
    print("Closing chrome driver")
    my_driver.quit()


def check_if_page_is_in_polish_lang(driver):
    # Check if page is in Polish language, if not change it to PL.
    try:
        e = driver.find_element(By.LINK_TEXT, "PL")
        if e:
            e.click()
    except NoSuchElementException:
        print("Website language page is correctly set to Polish by default")
