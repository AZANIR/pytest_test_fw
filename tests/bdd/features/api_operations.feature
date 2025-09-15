Feature: API Operations
  As an API client
  I want to perform CRUD operations
  So that I can manage data through the API

  Scenario Outline: Create different types of posts
    Given the API is available
    When I create a post with title "<title>" and body "<body>" for user <userId>
    Then the post should be created successfully
    And the response should contain the post details

    Examples:
      | title           | body                    | userId |
      | Test Post 1     | This is a test post     | 1      |
      | Another Post    | Another test content    | 2      |
      | Empty Body Post |                         | 1      |
      | Special Chars   | Post with émojis 🎉     | 3      |

  Scenario Outline: Retrieve posts with different filters
    Given the API has existing posts
    When I retrieve posts for user <userId>
    Then I should get <expectedCount> posts
    And all posts should belong to user <userId>

    Examples:
      | userId | expectedCount |
      | 1      | 10           |
      | 2      | 10           |
      | 5      | 10           |

  Scenario Outline: Update posts with various data
    Given a post exists with id <postId>
    When I update the post with title "<newTitle>" and body "<newBody>"
    Then the post should be updated successfully
    And the response should contain the updated title "<newTitle>"

    Examples:
      | postId | newTitle        | newBody              |
      | 1      | Updated Title 1 | Updated content 1    |
      | 2      | Updated Title 2 | Updated content 2    |
      | 3      | New Title       | Completely new text  |