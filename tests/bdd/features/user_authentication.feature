Feature: User Authentication
  As a user
  I want to authenticate with the system
  So that I can access protected resources

  Background:
    Given the authentication service is available

  Scenario: Successful login with valid credentials
    Given a user with username "testuser" and password "testpass"
    When the user attempts to login
    Then the login should be successful
    And the user should receive an authentication token

  Scenario: Failed login with invalid credentials
    Given a user with username "testuser" and password "wrongpass"
    When the user attempts to login
    Then the login should fail
    And the user should receive an error message "Invalid credentials"

  Scenario: Login with empty credentials
    Given a user with empty credentials
    When the user attempts to login
    Then the login should fail
    And the user should receive an error message "Username and password are required"