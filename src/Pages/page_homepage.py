from seleniumbase import BaseCase
from src.Locators import locators
import allure

class homepage(BaseCase):
    @allure.step("Enter Product For Seacrh")
    def enter_product_for_serch(self):
        self.update_text(locators.Homepage.search_bar,"Samsung S21")
        self.click(locators.Homepage.search_submit_button)

    @allure.step("Open Amazon website")
    def open_amazon(self):
        self.open("https://www.amazon.in/")

    @allure.step("Select Price Range")
    def select_price_range(self):
        self.click(locators.Homepage.price_range)

    @allure.step("Verify Prime Tag on Product")
    def verify_prime_tag(self):
        self.assert_element(locators.Homepage.prime_tag)

    @allure.step("Get Product Original Price")
    def get_product_price(self):
        self.get_text(locators.Homepage.product_price)

    @allure.step("Select Product")
    def select_product(self):
        self.click(locators.Homepage.samsung_s21)
        self.switch_to_newest_window()
