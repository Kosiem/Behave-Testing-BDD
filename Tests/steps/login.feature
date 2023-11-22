# Created by Patryk at 21.11.2023
Feature: Log in

  Background: User is on login page
    Given User open browser, enter site URL, and login page appears

  Scenario: The user accesses the website, a login form appears and is filled correctly by the user
    When User writes a good login
    And User writes a good password
    Then User should be logged in


  Scenario:  The user accesses the website, a login form appears and is filled incorrectly by the user
    When User writes a bad login
    And User writes a bad password
    Then User shouldn't be logged in
    And User closes the message

  Scenario: The user accesses the website, a login form appears and user enters good login, but wrong password
    When User writes a good login
    And User writes a bad password
    Then User shouldn't be logged in
    And User closes the message

  Scenario: The user accesses the website, a login form appears and user enters bad login, but good password
    When User writes a bad login
    And User writes a bad password
    Then User shouldn't be logged in
    And User closes the message