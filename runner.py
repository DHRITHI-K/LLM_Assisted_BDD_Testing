from input_reader import read_business_requirements
from llm.scenario_generator import generate_bdd_scenarios
from validator.scenario_validator import validate_scenarios

if __name__ == "__main__":
    requirements = read_business_requirements("requirements_input.txt")
    scenarios = generate_bdd_scenarios(requirements)

    validated_scenarios = validate_scenarios(scenarios)

    print("Validated BDD Scenarios:")
    for scenario in validated_scenarios:
        print(scenario)
