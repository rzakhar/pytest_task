from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMarketplace:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        # time.sleep(30)

        price = WebDriverWait(browser, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "p.price_color"))
        )

        assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) > 0, \
            "Cannot find 'Add to basket' button"
