def approve_scenarios(scenarios):
    """
    Allows a human tester to approve or reject
    validated BDD scenarios before execution.
    """

    approved_scenarios = []

    for index, scenario in enumerate(scenarios, start=1):
        print(f"\nScenario {index}:")
        print(scenario)

        choice = input("Approve this scenario? (y/n): ").strip().lower()
        if choice == "y":
            approved_scenarios.append(scenario)

    return approved_scenarios
