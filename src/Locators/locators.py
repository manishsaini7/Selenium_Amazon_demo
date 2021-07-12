class Homepage(object):
    search_bar = "//input[@id='twotabsearchtextbox']"
    search_submit_button = "//input[@id='nav-search-submit-button']"
    samsung_s21 = "//div[4]//div[1]//span[1]//div[1]//div[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[1]//h2[1]//a[1]//span[1]"
    prime_tag = "//div[4]//div[1]//span[1]//div[1]//div[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]//span[1]//i[1]"
    price_range = "//span[contains(text(),'Over ₹20,000')]"
    product_price = "//div[4]//div[1]//span[1]//div[1]//div[1]//div[1]//div[2]//div[2]//div[1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//a[1]//span[1]//span[2]//span[2]"

class product_page(object):
    add_to_cart = "//input[@id='add-to-cart-button']"
    view_cart = "//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']"

class login_page(object):
    continue_button = "//input[@id='continue']"
    sign_in_submit = "//input[@id='signInSubmit']"

class checkout_page(object):
    qty_button = "//span[@id='a-autoid-0']//span[@class='a-button-inner']"
    select_qty = "//a[normalize-space()='2']"
    cart_price = "//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold']"
    proceed_to_checkout = "//input[@name='proceedToRetailCheckout']"
