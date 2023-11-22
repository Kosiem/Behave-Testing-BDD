from selenium import webdriver
from behave import fixture
def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    context.driver.get("https://www.saucedemo.com/")

    yield context.driver

