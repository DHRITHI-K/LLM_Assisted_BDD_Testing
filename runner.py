from input_reader import read_business_requirements
from llm.scenario_generator import generate_bdd_scenarios
from validator.scenario_validator import validate_scenarios
from approval.manual_approval import approve_scenarios

def select_happy_path_scenarios(scenarios):
    """
    Selects only happy-path scenarios for automation.
    """
    happy_paths = []
    for scenario in scenarios:
        if "successful" in scenario.lower():
            happy_paths.append(scenario)
    return happy_paths


if __name__ == "__main__":
    requirements = read_business_requirements("requirements_input.txt")
    scenarios = generate_bdd_scenarios(requirements)

    validated_scenarios = validate_scenarios(scenarios)
    approved_scenarios = approve_scenarios(validated_scenarios)

    happy_path_scenarios = select_happy_path_scenarios(approved_scenarios)

    print("\nHappy Path Scenarios Selected for Automation:")
    for scenario in happy_path_scenarios:
        print(scenario)
