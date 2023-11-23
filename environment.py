from selenium import webdriver
from behave import fixture
@fixture()
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    context.driver.get("https://www.saucedemo.com/")
    return context.driver

@fixture()
def after_scenario(context, scenario):
    context.driver.close()