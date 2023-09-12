Feature: Login Functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      | email                         | password    |
      | amotoorisampleone@gmail.com   | secondone   |
      | amotoorisampletwo@gmail.com   | secondtwo   |
      | amotoorisamplethree@gmail.com | secondthree |


  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password say "12345" into the fields
    And I click on Login button
    Then I should get a proper warning message
