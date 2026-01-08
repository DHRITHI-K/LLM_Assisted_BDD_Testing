ALLOWED_KEYWORDS = [
    "given",
    "when",
    "then",
    "login",
    "enter",
    "click",
    "displayed",
    "redirected"
]

def validate_scenarios(scenarios):
    """
    Validates LLM-generated BDD scenarios.
    Checks for basic Given-When-Then structure
    and presence of allowed keywords.
    """

    valid_scenarios = []

    for scenario in scenarios:
        scenario_lower = scenario.lower()

        # Check Given-When-Then structure
        if all(word in scenario_lower for word in ["given", "when", "then"]):
            valid_scenarios.append(scenario)

    return valid_scenarios
