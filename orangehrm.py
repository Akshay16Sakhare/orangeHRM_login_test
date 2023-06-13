import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHrmLogin:
    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.username = (By.NAME, 'username')
        self.password = (By.NAME, 'password')
        self.login_btn = (By.XPATH, "//button[@type='submit']")
        self.error_msg = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def enter_cred(self, user, passcode):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(passcode)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text


class OrangeHrmLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.username = (By.XPATH, "//input[@placeholder='Username']")
        self.password = (By.XPATH, "//input[@placeholder='Password']")
        self.login_btn = (By.XPATH, "//button[@type='submit']")
        self.error_msg = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def enter_cred(self, user, passcode):
        login_user = self.wait.until(EC.visibility_of_element_located(self.username))
        login_user.send_keys(user)

        login_passcode = self.wait.until(EC.visibility_of_element_located(self.password))
        login_passcode.send_keys(passcode)

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text
