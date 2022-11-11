Feature:verify books are added and deleted using library api

  Scenario: verify add book function
    Given the Book details that needs to be added to library
    When we execute add book API
    Then the book should be added