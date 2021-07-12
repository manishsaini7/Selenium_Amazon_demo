from src.Locators import locators
from src.Pages.page_homepage import homepage
from src.Pages.page_product_desc import product_desc
from src.Pages.page_checkout import checkout_page
import pytest

class test_amazon(homepage,product_desc,checkout_page):
    @pytest.mark.test_amazon01
    def test_amazon_01(self):
        self.open_amazon()
        self.enter_product_for_serch()
        self.select_price_range()
        self.verify_prime_tag()
        product_original_price = self.get_product_price()
        self.select_product()
        self.click_add_to_cart()
        self.check_cart()
        product_cart_price = self.get_product_price_cart()
        self.change_quantity()
        self.verify_prices(product_cart_price,product_original_price)