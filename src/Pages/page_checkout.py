from seleniumbase import BaseCase
from src.Locators import locators
import allure

class checkout_page(BaseCase):
    @allure.step("Chgange Quantity to 2")
    def change_quantity(self):
        self.click(locators.checkout_page.qty_button)
        self.click(locators.checkout_page.select_qty)

    @allure.step("Get Product Price in Cart")
    def get_product_price_cart(self):
        self.get_text(locators.checkout_page.cart_price)

    @allure.step("Verify Prices in Cart and Product Description")
    def verify_prices(self,cart_price , original_price):
        assert(cart_price == original_price),"Prices are not equal"

    @allure.step("Proceed To Checkout")
    def proceed_to_checkout(self):
        self.click(locators.checkout_page.proceed_to_checkout)