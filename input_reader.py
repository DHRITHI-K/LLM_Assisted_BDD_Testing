def read_business_requirements(file_path):
    with open(file_path, "r") as file:
        requirements = file.read()
    return requirements


if __name__ == "__main__":
    data = read_business_requirements("requirements_input.txt")
    print("Business Requirements Input:")
    print(data)
