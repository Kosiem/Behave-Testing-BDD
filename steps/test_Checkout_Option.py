import selenium.common.exceptions as exc
from behave import when, then
from selenium.webdriver.common.by import By


@when(u'User writes first name')
def step_user_writes_first_name(context):
    context.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Patryk")


@when(u'User writes last name')
def step_user_writes_last_name(context):
    context.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Behave")


@when(u'User writes postal code')
def step_user_writes_postal_code(context):
    context.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("00-000")


@then(u'User clicks continue button')
def step_click_continue(context):
    context.driver.find_element(By.XPATH, "//input[@id='continue']").click()


@then(u'User should see his product in checkout')
def step_user_see_product(context):
    try:
        context.driver.find_element(By.XPATH, "//div[@class='cart_item']")
        assert True
    except exc.NoSuchElementException:
        assert False


@then(u'User should see payment information')
def step_see_payment(context):
    context.payment = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label'][1]")
    assert context.payment.text == "Payment Information"
    context.pay_value = context.driver.find_element(By.XPATH, "//div[@class='summary_value_label'][1]")
    assert context.pay_value.text == "SauceCard #31337"


@then(u'User should see shipping information')
def step_see_shipping(context):
    context.shipping = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label'][2]")
    assert context.shipping.text == "Shipping Information"
    context.ship_value = context.driver.find_element(By.XPATH, "//div[@class='summary_value_label'][2]")
    assert context.ship_value.text == "Free Pony Express Delivery!"


@then(u'User should see total price')
def step_see_total_price(context):
    context.total_price = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label'][3]")
    assert context.total_price.text == "Price Total"
    context.item_total = context.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
    assert context.item_total.text == "Item total: $29.99"
    context.tax = context.driver.find_element(By.XPATH, "//div[@class='summary_tax_label']")
    assert context.tax.text == "Tax: $2.40"


@then(u'User clicks finish button')
def step_click_finish(context):
    context.driver.find_element(By.XPATH, "//button[@id='finish']").click()


@then(u'User should see confirmation of order')
def step_confirmation(context):
    context.header = context.driver.find_element(By.XPATH, "//h2[@class='complete-header']")
    assert context.header.text == "Thank you for your order!"
    context.body = context.driver.find_element(By.XPATH, "//div[@class='complete-text']")
    assert context.body.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    context.sign = context.driver.find_element(By.XPATH, "//img[@class='pony_express']")
    assert context.sign.get_attribute("alt") == "Pony Express"


@then(u'User should see back home button')
def step_back_home(context):
    try:
        context.driver.find_element(By.XPATH, "//button[@name='back-to-products']")
        assert True
    except exc.NoSuchElementException:
        assert False


@then(u'User should see error message')
def step_error_message(context):
    context.error_msg = ["Error: Postal Code is required", "Error: Last Name is required",
                         "Error: First Name is required"]

    context.msg = context.driver.find_element(By.XPATH, "//h3[@data-test='error']")

    for error in context.error_msg:
        if context.msg == error:
            assert True


@then(u'User clicks cancel button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@id='cancel']").click()


@then(u'User should be at home page of shop')
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"


@then("User clicks on checkout button")
def step_click_checkout(context):
    context.driver.find_element(By.XPATH, "//button[@name='checkout']").click()
