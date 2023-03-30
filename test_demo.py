from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_DemoClass:
    # her testeten önce çağrılır
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    # her testen sonra çağırılır
    def teardown_method(self):
        self.driver.quit()

    # setup -> test_demoFunc -> teardown
    def test_demoFunc(self):
        #3A Act Arrange Assert
        text="Hello"
        assert text=="Hello"
    
    #setup -> test_demo2 -> teardown
    def test_demo2(self):
        assert True

    @pytest.mark.skip()
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        sleep(10)
        

