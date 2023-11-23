# Created by Patryk at 22.11.2023

Feature: Possibility of adding items to the cart

  Background: User open browser, enter site URL, and login page appears
    Given User open browser, enter site URL, and login page appears
    When User writes a good login
    And User writes a good password
    Then User should be logged in


  Scenario: User selects a product - backpack to the cart
    When User click on add to cart button on backpack
    Then User should move to cart page
    Then Product should appear at cart page
    And Product should have correct name
    And Product should have correct description
    And Product should have correct price
    And Product quantity should be equal to one
    And Remove button should appear
    And Continue Shopping option should appear
    And Checkout option should appear


  Scenario: User selects a product - backpack to the cart, and then remove it
    When User click on add to cart button on backpack
    Then User should move to cart page
    Then Product should appear at cart page
    And Product should have correct name
    And Product should have correct description
    And Product should have correct price
    And Product quantity should be equal to one
    And Remove button should appear
    And Continue Shopping option should appear
    And Checkout option should appear
    Then User click remove button
    Then Product should disappear from cart page

  Scenario: User selects a product - backpack to the cart, and remove it at product panel
    When User click on add to cart button on backpack
    Then User click remove button at product panel
    Then User should move to cart page
    And Cart page should be empty

  Scenario:  User selects a product - backpack to the cart, and click continue shopping, then selects bike light to cart
    When User click on add to cart button on backpack
    Then User should move to cart page
    Then Product should appear at cart page
    And Product should have correct name
    And Product should have correct description
    And Product should have correct price
    And Product quantity should be equal to one
    And Remove button should appear
    And Continue Shopping option should appear
    And Checkout option should appear
    Then User click Continue Shopping option
    Then User click on add to cart button on bike light
    Then User should move to cart page
    Then Products should appear at cart page
    And Products should have correct description
    And Products should have correct name
    And Products should have correct price
    And Products quantity should be equal to one