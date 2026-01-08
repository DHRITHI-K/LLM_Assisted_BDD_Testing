from behave import given, when, then

@given('the user is on the login page')
def step_open_login_page(context):
    print("Opening login page")

@when('the user enters valid credentials')
def step_enter_credentials(context):
    print("Entering valid username and password")

@then('the user should be logged in successfully')
def step_verify_login(context):
    print("Login successful - dashboard displayed")
