Feature: Add article
  As a user
  I want to be able to add article

  Scenario: Add article
    Given I have the following articles in my database:
      | id  | name        | is_available |
      | 1   | Drill       | no           |
      | 2   | Drill Press | no           |
    When I add following article:
      | id  | name        | is_available |
      | 3   | Grinder     | yes          |
    Then I see those listed articles:
      | id  | name        | is_available |
      | 1   | Drill       | no           |
      | 2   | Drill Press | no           |
      | 3   | Grinder     | yes          |