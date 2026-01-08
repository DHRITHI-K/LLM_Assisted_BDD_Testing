from input_reader import read_business_requirements
from llm.scenario_generator import generate_bdd_scenarios
from validator.scenario_validator import validate_scenarios
from approval.manual_approval import approve_scenarios

if __name__ == "__main__":
    requirements = read_business_requirements("requirements_input.txt")
    scenarios = generate_bdd_scenarios(requirements)

    validated_scenarios = validate_scenarios(scenarios)
    approved_scenarios = approve_scenarios(validated_scenarios)

    print("\nApproved Scenarios:")
    for scenario in approved_scenarios:
        print(scenario)
