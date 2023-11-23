import selenium.common.exceptions as exc
from behave import when, then
from selenium.webdriver.common.by import By


@when(u'User click on add to cart button on backpack')
def step_add_to_cart_backpack(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()


@then(u'User should move to cart page')
def step_move_to_cart_page(context):
    context.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()


@then(u'Product should appear at cart page')
def step_check_product_appearing(context):
    try:
        context.driver.find_element(By.XPATH, "//div[@class='cart_list']")
    except exc.NoSuchElementException:
        assert False


@then(u'Product should have correct name')
def step_product_correct_name(context):
    assert context.driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == "Sauce Labs Backpack"


@then(u'Product should have correct description')
def step_product_correct_desc(context):
    assert context.driver.find_element(By.XPATH,
                                       "//div[@class='inventory_item_desc']").text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."


@then(u'Product should have correct price')
def step_product_correct_price(context):
    assert context.driver.find_element(By.XPATH, "//div[@class='inventory_item_price']").text == "$29.99"


@then(u'Product quantity should be equal to one')
def step_product_correct_qt(context):
    assert context.driver.find_element(By.XPATH, "//div[@class='cart_quantity']").text == "1"


@then(u'Remove button should appear')
def step_remove_appear(context):
    assert context.driver.find_element(By.XPATH, "//button[@name='remove-sauce-labs-backpack']").is_displayed()


@then(u'Continue Shopping option should appear')
def step_ct_shopping_appear(context):
    assert context.driver.find_element(By.XPATH, "//button[@name='continue-shopping']").is_displayed()


@then(u'Checkout option should appear')
def step_checkout_appear(context):
    assert context.driver.find_element(By.XPATH, "//button[@name='checkout']").is_displayed()


@then(u'User click remove button')
def step_click_remove(context):
    context.driver.find_element(By.XPATH, "//button[@name='remove-sauce-labs-backpack']").click()


@then(u'Product should disappear from cart page')
def step_product_disappear(context):
    try:
        context.driver.find_element(By.XPATH, "//div[@class='cart_item_label']")
    except exc.NoSuchElementException:
        assert True


@then(u'User click remove button at product panel')
def step_remove_at_product_panel(context):
    context.driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()


@then(u'Cart page should be empty')
def step_cart_page_empty(context):
    context.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    try:
        context.driver.find_elements(By.XPATH, "//div[@class='cart_item_label']")
    except exc.NoSuchElementException:
        assert True


@then(u'User click Continue Shopping option')
def step_continue_shopping(context):
    context.driver.find_element(By.XPATH, "//button[@name='continue-shopping']").click()


@then(u'User click on add to cart button on bike light')
def step_bike_light_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()


@then(u'Products should appear at cart page')
def step_products_appear(context):
    try:
        context.products = context.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        assert len(context.products) == 2
    except exc.NoSuchElementException:
        assert False


@then(u'Products should have correct description')
def step_products_correct_desc(context):
    context.desc = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_desc']")

    assert context.desc[
               0].text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    assert context.desc[
               1].text == "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included."


@then(u'Products should have correct name')
def step_products_correct_names(context):
    context.names = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    assert context.names[0].text == "Sauce Labs Backpack"
    assert context.names[1].text == "Sauce Labs Bike Light"


@then(u'Products should have correct price')
def step_products_correct_prices(context):
    context.prices = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")

    assert context.prices[0].text == "$29.99"
    assert context.prices[1].text == "$9.99"


@then(u'Products quantity should be equal to one')
def step_products_correct_qts(context):
    context.quantity = context.driver.find_elements(By.XPATH, "//div[@class='cart_quantity']")

    assert context.quantity[0].text == "1"
    assert context.quantity[1].text == "1"
