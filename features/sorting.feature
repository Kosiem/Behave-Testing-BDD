# Created by Patryk at 22.11.2023

@use_setup_browser @sorting
Feature: Sorting products on the site

  Background: The user is logged in and is on the store page
    Then User write correct login
    And User write correct password
    And User click login button
    Then User should be on shop page

  Scenario: Alphabetical sorting of products
    When User chooses option to sort products alphabetically
    Then Products should be sorted alphabetically

  Scenario: Reverse to alphabetical sorting of products
    When User chooses option to sort products in reverse order to alphabetical
    Then Products should be sorted in reverse order to alphabetical

  Scenario: Price ascending sorting of products
    When User chooses option to sort products in price ascending order
    Then Products should be sorted in price ascending order

  Scenario: Price descending sorting of products
    When User choose option to sort products in price descending order
    Then Products should be sorted in price descending order