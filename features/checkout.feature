# Created by Patryk at 22.11.2023
Feature: Checkout option for products

  Background: The user is logged in and is on the store page. User add to cart a backpack product
    Given User open browser, enter site URL, and login page appears
    When User writes a good login
    And User writes a good password
    Then User should be logged in
    When User click on add to cart button on backpack
    Then User should move to cart page
    Then Product should appear at cart page
    Then User clicks on checkout button

  Scenario: User fills checkout information form correctly
    When User writes first name
    And User writes last name
    And User writes postal code
    Then User clicks continue button
    Then User should see his product in checkout
    And Product should have correct price
    And Product should have correct description
    And Product should have correct name
    And Product quantity should be equal to one
    And User should see payment information
    And User should see shipping information
    And User should see total price
    Then User clicks finish button
    And User should see confirmation of order
    And User should see back home button


  Scenario: User fills checkout information, but without first name
    When User writes last name
    And User writes postal code
    Then User clicks continue button
    Then User should see error message

  Scenario: User fills checkout information, but without last name
    When User writes first name
    And User writes postal code
    Then User clicks continue button
    Then User should see error message

  Scenario: User fills checkout information, but without postal code
    When User writes first name
    And User writes last name
    Then User clicks continue button
    Then User should see error message


  Scenario: User fills checkout information, clicks continue, but then clicks cancel
    When User writes first name
    And User writes last name
    And User writes postal code
    Then User clicks continue button
    Then User should see his product in checkout
    And Product should have correct price
    And Product should have correct description
    And Product should have correct name
    And Product quantity should be equal to one
    Then User clicks cancel button
    And User should be at home page of shop



