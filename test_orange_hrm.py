import pytest
from orangehrm import OrangeHrmLogin
from selenium import webdriver

driver = None


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


def test_correct_login(setup):
    orangehrm = OrangeHrmLogin(driver)
    user = 'Admin'
    passcode = 'admin123'

    orangehrm.enter_cred(user, passcode)
    orangehrm.click_login_btn()


def test_incorrect_login(setup):
    orangehrm = OrangeHrmLogin(driver)
    user = 'aks'
    passcode = '123'

    orangehrm.enter_cred(user, passcode)
    orangehrm.click_login_btn()

    error_msg = orangehrm.get_error_message()
    assert error_msg == 'Invalid credentials'
