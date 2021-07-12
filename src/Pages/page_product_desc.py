from seleniumbase import BaseCase
from src.Locators import locators
import allure

class product_desc(BaseCase):
    @allure.step("Add Product to Cart")
    def click_add_to_cart(self):
        self.click(locators.product_page.add_to_cart)
        self.wait(6)

    @allure.step("Proceed to Checkout")
    def proceed_to_checkout(self):
        self.click(locators.checkout_page.proceed_to_checkout)

    @allure.step("View Cart")
    def check_cart(self):
        self.click(locators.product_page.view_cart)

