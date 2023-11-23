# Created by Patryk at 22.11.2023

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

  Scenario: User writes bad login, good password and is not logged in
    When User writes a bad login
    And User writes a good password
    Then User shouldn't be logged in
    Then User closes the message

  Scenario: User writes good login, bad password and is not logged in
    When User writes a good login
    And User writes a bad password
    Then User shouldn't be logged in
    Then User closes the message

