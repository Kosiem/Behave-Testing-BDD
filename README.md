# Behave-Testing-BDD
Tests with use of Behave tool in Python and Gherkin feature file.

<h2>Tested features</h2>
- <b>Login page</b> <br>
- <b>Product sorting</b><br>
- <b>Adding to cart</b><br>
- <b>Checkout</b><br>

Each feature has different scenarios written to test the various functionalities on the site.<br>

<b>Example:</b>

```gherkin

Feature: Login functionality

  Background: User open browser, enter site URL, and login page appears
    Given  User open browser, enter site URL, and login page appears

  Scenario: User writes good login, good password and is logged in
    When User writes a good login
    And User writes a good password
    Then User should be logged in

  Scenario: User writes bad login, bad password and is not logged in
    When User writes a bad login
    And User writes a bad password
    Then User shouldn't be logged in
    Then User closes the message


```
<h2>Tests - Steps, were written using Behave</h2><br>

<b>Example:</b>

```python
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
```

<h2>Environment</h2><br>

There are two functions in the environment.py file, executing before the start of each scenarios - attaching the browser, maximizing the window, clearing cookies and connecting to the specified URL<br>

```python
from selenium import webdriver
from behave import fixture
@fixture()
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    context.driver.get("https://www.saucedemo.com/")
    return context.driver
```

And shutting down the browser. <br>

```python
@fixture()
def after_scenario(context, scenario):
    context.driver.close()

```
