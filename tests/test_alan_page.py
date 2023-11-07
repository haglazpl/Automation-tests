import time

import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

TIME_TO_WAIT = 1
FILE_PATH = "Your file path" #example "C:\\Users\\Dominik\\test.pdf"


class TestPositiveCases:

    @pytest.mark.positive
    @pytest.mark.general
    def test_validate_top_bar_menu_and_footage(self, driver):
        print("Starting test_validate_top_bar_menu_and_footage")

        # CHECK CANDIDATE SECTION
        print("Checking candidates section")
        driver.find_element(By.XPATH,
                            "/html/body/div[@class='home-container']/div[@class='container "
                            "container-wide h-100 position-relative']//div[@class='row']/div["
                            "2]//h3/a[@href='/dla-kandydatow/']").click()
        BaseUtils.check_recruitment_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                      "@href='https://alan-systems.com/pl/dla-kandydatow-o-nas/']").click()
        BaseUtils.check_recruitment_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                      "@href='https://alan-systems.com/pl/dla-kandydatow-kariera/']").click()
        BaseUtils.check_recruitment_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                      "@href='https://alan-systems.com/pl/dla-kandydatow-kontakt/']").click()
        BaseUtils.check_recruitment_section(self, driver)
        print("Checking recruitment section - Completed")

        # CHECK BUSINESS SECTION
        print("Checking business section")
        driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                      "@href='https://alan-systems.com/pl/dla-biznesu/']").click()
        BaseUtils.check_business_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                      "@href='https://alan-systems.com/pl/dla-biznesu-o-nas/']").click()
        BaseUtils.check_business_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                      "@href='https://alan-systems.com/pl/dla-biznesu-oferta/']").click()
        BaseUtils.check_business_section(self, driver)

        driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                      "@href='https://alan-systems.com/pl/dla-biznesu-kontakt/']").click()
        BaseUtils.check_business_section(self, driver)
        print("Checking business section - Completed")


class TestNegativeCases:

    @pytest.mark.negative
    @pytest.mark.general
    def test_validate_required_fields_in_job_offer(self, driver, extras):
        print("Starting test_validate_required_fields_in_job_offer")
        action = ActionChains(driver)
        # Go to the candidate page
        driver.find_element(By.XPATH,
                            "/html/body/div[@class='home-container']/div[@class='container "
                            "container-wide h-100 position-relative']//div[@class='row']/div["
                            "2]//h3/a[@href='/dla-kandydatow/']").click()

        # Find and go to all job offers
        driver.find_element(By.XPATH,
                            "/html/body/header[@class='position-relative']/div[1]//a["
                            "@href='/dla-kandydatow-kariera/']").click()

        # Select test automation developer job offer
        test_automation_dev_job_offer = driver.find_element(By.XPATH,
                                                            '//a[contains(@href,'
                                                            '"https://alan-systems.com/pl/oferta-pracy/test'
                                                            '-automation-developer/")]')
        driver.execute_script("arguments[0].scrollIntoView();", test_automation_dev_job_offer)
        time.sleep(TIME_TO_WAIT)
        test_automation_dev_job_offer.click()

        # Scroll down job offer, fill the checkboxes and upload pdf
        select_first_checkbox = driver.find_element(By.XPATH, "//div[contains(@id, 'checkbox-1')]//div")
        select_second_checkbox = driver.find_element(By.XPATH, "//div[contains(@id, 'checkbox-2')]//div")
        apply_button = driver.find_element(By.XPATH,
                                           "/html/body//section/div[@class='container container-wide']/div["
                                           "@class='row']//form[@method='post']//button[@class='forminator-button "
                                           "forminator-button-submit']")
        driver.execute_script("arguments[0].scrollIntoView({'block':'center','inline':'center'});",
                              select_first_checkbox)
        time.sleep(TIME_TO_WAIT)

        action.double_click(select_first_checkbox)
        action.double_click(select_second_checkbox)
        driver.find_element(By.XPATH, "//div[@id='upload-1']/div/div/input[@name='upload-1']").send_keys(FILE_PATH)

        # Try to apply by clicking apply button
        apply_button.click()

        # Error message should appear now
        error_message_catch = len(driver.find_elements(By.XPATH, "//span[@class='forminator-error-message']")) > 0
        assert error_message_catch, "Can't find error message button"
        print(f'Is correct error message button displayed? {error_message_catch}')


class BaseUtils:
    # Utility class for helper methods

    def check_recruitment_section(self, driver):
        # Method for checking recruitment section nav bar(top bar menu) and footage(basic contact data)
        time.sleep(TIME_TO_WAIT)
        nav_top_bar = driver.find_element(By.XPATH, "/html/body/header[@class='position-relative']//nav")
        nav_top_bar_alan_logo = driver.find_element(By.XPATH, "/html/body//nav//a[@href='https://alan-systems.com/pl"
                                                              "/']/img[@alt='Alan System']")
        nav_top_bar_for_candidates = driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                                                   "@href='https://alan-systems.com/pl/dla-kandydatow"
                                                                   "/']")
        nav_top_bar_about_us = driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                                             "@href='https://alan-systems.com/pl/dla-kandydatow-o-nas"
                                                             "/']")
        nav_top_bar_career = driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                                           "@href='https://alan-systems.com/pl/dla-kandydatow-kariera"
                                                           "/']")
        nav_top_bar_contact = driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                                            "@href='https://alan-systems.com/pl/dla-kandydatow"
                                                            "-kontakt/']")
        nav_top_bar_go_to_business_section = driver.find_element(By.XPATH, "//ul[@id='menu-menu-kariera']//a["
                                                                           "@href='https://alan-systems.com/pl/dla"
                                                                           "-biznesu/']")
        contact_window = driver.find_element(By.XPATH, "/html/body//div[@class='container']//h3[.='KONTAKT']")

        assert nav_top_bar.is_displayed(), "Nav bar should be visible but it's not"
        assert nav_top_bar_alan_logo.is_displayed(), "Nav bar Alan logo should be visible but it's not"
        assert nav_top_bar_for_candidates.is_displayed(), "Nav bar candidates button should be visible but it's not"
        assert nav_top_bar_about_us.is_displayed(), "Nav bar about us button should be visible but it's not"
        assert nav_top_bar_career.is_displayed(), "Nav bar career button should be visible but it's not"
        assert nav_top_bar_contact.is_displayed(), "Nav bar contact button should be visible but it's not"
        assert nav_top_bar_go_to_business_section.is_displayed(), "Nav bar business section button should be visible " \
                                                                  "but it's not"
        assert contact_window.is_displayed(), "Contact info should be visible but it's not"

    def check_business_section(self, driver):
        # Method for checking business section nav bar(top bar menu) and footage(basic contact data)
        time.sleep(TIME_TO_WAIT)
        nav_top_bar = driver.find_element(By.XPATH, "/html/body/header[@class='position-relative']//nav")
        nav_top_bar_alan_logo = driver.find_element(By.XPATH, "/html/body//nav//a[@href='https://alan-systems.com/pl"
                                                              "/']/img[@alt='Alan System']")
        nav_top_bar_for_business = driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                                                 "@href='https://alan-systems.com/pl/dla-biznesu/']")
        nav_top_bar_about_us = driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                                             "@href='https://alan-systems.com/pl/dla-biznesu-o-nas/']")
        nav_top_bar_offer = driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                                          "@href='https://alan-systems.com/pl/dla-biznesu-oferta/']")
        nav_top_bar_contact = driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                                            "@href='https://alan-systems.com/pl/dla-biznesu-kontakt/']")
        nav_top_bar_go_to_recruitment_section = driver.find_element(By.XPATH, "//ul[@id='menu-menu-biznes']//a["
                                                                              "@href='https://alan-systems.com/pl/dla"
                                                                              "-kandydatow/']")
        contact_window = driver.find_element(By.XPATH, "/html/body//div[@class='container']//h3[.='KONTAKT']")

        assert nav_top_bar.is_displayed(), "Nav bar should be visible but it's not"
        assert nav_top_bar_alan_logo.is_displayed(), "Nav bar Alan logo should be visible but it's not"
        assert nav_top_bar_for_business.is_displayed(), "Nav bar for business button should be visible but it's not"
        assert nav_top_bar_about_us.is_displayed(), "Nav bar about us button should be visible but it's not"
        assert nav_top_bar_offer.is_displayed(), "Nav bar offer button should be visible but it's not"
        assert nav_top_bar_contact.is_displayed(), "Nav bar contact button should be visible but it's not"
        assert nav_top_bar_go_to_recruitment_section.is_displayed(), "Nav bar recruitment section button should be " \
                                                                     "visible but it's not"
        assert contact_window.is_displayed(), "Contact info should be visible but it's not"
