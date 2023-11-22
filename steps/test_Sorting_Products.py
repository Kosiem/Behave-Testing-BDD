from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

@given(u'User is on login page')
def step_user_on_login_pagel(context):

    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    context.driver.delete_all_cookies()

@then(u'User write correct login')
def step_user_correct_login(context):

    context.driver.find_element(By.XPATH, "//input[@name='user-name']") .send_keys("standard_user")


@then(u'User write correct password')
def step_user_correct_password(context):

    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("secret_sauce")


@then(u'User click login button')
def step_user_log_in(context):

    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'User should be on shop page')
def step_user_on_shop_page(context):

    WebDriverWait(context.driver, 5).until(ec.url_to_be("https://www.saucedemo.com/inventory.html"))
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"


@when(u'User chooses option to sort products alphabetically')
def step_choose_a_to_z(context):

    WebDriverWait(context.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//select")))
    context.sort = Select(context.driver.find_element(By.XPATH, "//select"))
    context.sort.select_by_value("az")

@then(u'Products should be sorted alphabetically')
def step_alphabetically_sort(context):


    context.items = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    context.before_sort = []
    for item in context.items:
        context.before_sort.append(item.text)
    print(context.before_sort)
    context.after_sort = sorted(context.before_sort)
    print(context.after_sort)
    assert context.before_sort == context.after_sort



@when(u'User chooses option to sort products in reverse order to alphabetical')
def step_choose_z_to_a(context):

    WebDriverWait(context.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//select")))
    context.sort = Select(context.driver.find_element(By.XPATH, "//select"))
    context.sort.select_by_value("za")


@then(u'Products should be sorted in reverse order to alphabetical')
def step_reverse_alphabetical_order(context):

    context.items = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    context.before_sort = []
    for item in context.items:
        context.before_sort.append(item.text)
    print(context.before_sort)
    context.after_sort = sorted(context.before_sort, reverse=True)
    print(context.after_sort)
    assert context.before_sort == context.after_sort


@when(u'User chooses option to sort products in price ascending order')
def step_choose_price_ascending(context):

    WebDriverWait(context.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//select")))
    context.sort = Select(context.driver.find_element(By.XPATH, "//select"))
    context.sort.select_by_value("lohi")


@then(u'Products should be sorted in price ascending order')
def step_price_ascending_order(context):

    context.items = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
    context.before_sort = []
    for item in context.items:
        context.before_sort.append(float(item.text.replace("$", "")))
    print(context.before_sort)
    context.after_sort = sorted(context.before_sort)
    print(context.after_sort)
    assert context.before_sort == context.after_sort


@when(u'User choose option to sort products in price descending order')
def step_impl(context):

    WebDriverWait(context.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//select")))
    context.sort = Select(context.driver.find_element(By.XPATH, "//select"))
    context.sort.select_by_value("hilo")


@then(u'Products should be sorted in price descending order')
def step_impl(context):


    context.items = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
    context.before_sort = []
    for item in context.items:
        context.before_sort.append(float(item.text.replace("$", "")))
    print(context.before_sort)
    context.after_sort = sorted(context.before_sort, reverse=True)
    print(context.after_sort)
    assert context.before_sort == context.after_sort

def after_scenario(context):

    context.driver.close()