from input_reader import read_business_requirements
from llm.scenario_generator import generate_bdd_scenarios

if __name__ == "__main__":
    requirements = read_business_requirements("requirements_input.txt")
    scenarios = generate_bdd_scenarios(requirements)

    print("Generated BDD Scenarios:")
    for scenario in scenarios:
        print(scenario)
