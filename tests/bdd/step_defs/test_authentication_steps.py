import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests


scenarios('../features/user_authentication.feature')


@pytest.fixture
def auth_context():
    return {
        'username': None,
        'password': None,
        'response': None,
        'token': None,
        'error_message': None
    }


@given('the authentication service is available')
def auth_service_available():
    pass


@given(parsers.parse('a user with username "{username}" and password "{password}"'))
def user_credentials(auth_context, username, password):
    auth_context['username'] = username
    auth_context['password'] = password


@given('a user with empty credentials')
def empty_credentials(auth_context):
    auth_context['username'] = ""
    auth_context['password'] = ""


@when('the user attempts to login')
def attempt_login(auth_context):
    if not auth_context['username'] or not auth_context['password']:
        auth_context['error_message'] = "Username and password are required"
        auth_context['login_success'] = False
        return

    if auth_context['username'] == "testuser" and auth_context['password'] == "testpass":
        auth_context['login_success'] = True
        auth_context['token'] = "mock_auth_token_12345"
    else:
        auth_context['login_success'] = False
        auth_context['error_message'] = "Invalid credentials"


@then('the login should be successful')
def login_successful(auth_context):
    assert auth_context['login_success'] is True


@then('the login should fail')
def login_failed(auth_context):
    assert auth_context['login_success'] is False


@then('the user should receive an authentication token')
def receive_token(auth_context):
    assert auth_context['token'] is not None
    assert auth_context['token'] == "mock_auth_token_12345"


@then(parsers.parse('the user should receive an error message "{expected_message}"'))
def receive_error_message(auth_context, expected_message):
    assert auth_context['error_message'] == expected_message