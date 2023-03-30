from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:

    def test_invalid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        #en fazla 5 sn olacak şekilde user-name id'li elementin görünmesini bekle
        WebDriverWait(driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
        usernameInput=driver.find_element(By.ID,"user-name")
        WebDriverWait(driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
    
    def test_valid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        WebDriverWait(driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
        usernameInput=driver.find_element(By.ID,"user-name")
        WebDriverWait(driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        passwordInput=driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(500)
        


testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()
