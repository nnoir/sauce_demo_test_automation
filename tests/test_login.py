import pytest
from pages.login_page import LoginPage
from db_utils import get_test_users

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        users = get_test_users()
        metafunc.parametrize("username,password", users)

def test_successful_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if "inventory" in driver.current_url:
        assert True
    else:
        error_message = login_page.invalid_login().lower()

        if "locked out" in error_message:
            print(f"User '{username}' is blocked - login impossible")
            assert True
        else:
            pytest.fail(f"❌ Login failed for user: '{username}'. Reason: '{error_message}'")

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_password")
    error = login_page.invalid_login()

    assert "Epic sadface: Username and password do not match any user in this service" in error


