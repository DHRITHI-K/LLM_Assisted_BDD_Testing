def generate_bdd_scenarios(requirements_text):
    """
    Simulates LLM behavior by converting business requirements
    into BDD-style Gherkin scenarios.
    """

    scenarios = []

    # Positive / Happy Path
    scenarios.append("""
Scenario: Successful login with valid credentials
  Given the user is on the login page
  When the user enters valid username and password
  Then the user should be logged in successfully
""")

    # Negative Path
    scenarios.append("""
Scenario: Login fails with invalid credentials
  Given the user is on the login page
  When the user enters invalid username or password
  Then an error message should be displayed
""")

    return scenarios
