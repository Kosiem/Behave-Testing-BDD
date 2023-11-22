from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import selenium.common.exceptions

@given(u'User enter site URL, and login page appears')
def step_initial_condition(context):

    context.login = context.driver.find_element(By.XPATH, "//input[@name='user-name']")
    context.password = context.driver.find_element(By.XPATH, "//input[@name='password']")
    context.button = context.driver.find_element(By.XPATH, "//input[@type='submit']")

@when(u'User writes a good login')
def step_write_good_login(context):

    context.login.send_keys("standard_user")


@when(u'User writes a good password')
def step_write_good_password(context):

    context.password.send_keys("secret_sauce")


@then(u'User should be logged in')
def step_log_in(context):

    context.button.click()
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"


@when(u'User writes a bad login')
def step_write_bad_login(context):

    context.login.send_keys("bad_user")


@when(u'User writes a bad password')
def step_write_bad_password(context):

    context.password.send_keys("bad_password")



@then(u'User shouldn\'t be logged in')
def step_dont_log_in(context):

    context.button.click()
    context.message = context.driver.find_element(By.XPATH, "//h3")
    assert context.message.text == "Epic sadface: Username and password do not match any user in this service"


@then(u'User closes the message')
def step_close_error_message(context):

    context.button = context.driver.find_element(By.XPATH, "//button[@class='error-button']")
    context.button.click()

    try:
        WebDriverWait(context.driver, 2).until(ec.presence_of_element_located((By.XPATH, "//button[@class='error-button']")))
    except selenium.common.exceptions.TimeoutException:
        assert True


def after_scenario(context):

    context.driver.close()
