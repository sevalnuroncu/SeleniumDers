from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
#  seleniumun çalışması için bir webdriver lazım. Chrome kullanacağımız için chromedriver lazım driver
# seleniuma bir tarayıcı yüklüyomuşuz gibi düşünebiliriiz. 


driver=webdriver.Chrome(ChromeDriverManager().install())#seleniuma web driver tanıtma
driver.maximize_window()
driver.get("https://www.google.com/?hl=tr")#üzerinde çalıştığım tarayıcı hangi url'e gitsin
input=driver.find_element(By.NAME,"q")#html sayfasında namei q olan input tagını bana getir 
input.send_keys("kodlama.io")#input içine kodlama io yaz
searchButton=driver.find_element(By.NAME,"btnK")#bulacağım element driverin içinde olduğuiçin driver. diye yazdık
# googlda ara buttonunun ismi btnk'dır
sleep(2)
searchButton.click()
sleep(4)
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde şu anda {len(listOfCourses)} adet kurs var")




# sleep(10)
while(True):
    continue
 