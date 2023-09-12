# Created by illya at 9/12/2023
Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I am on the Home Page
    When I enter valid product "HP" into a search box field
    And I click on the Search button
    Then Valid product should get displayed in search results
