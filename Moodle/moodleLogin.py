import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

PATH="D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

driver.implicitly_wait(5)

data = driver.find_element_by_id("login").text

words = data.split()

username = input("enter username")
password = input("enter password")


driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(username)

driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(password)


driver.find_element_by_id("valuepkg3").clear()



if(words[7]==("add")):
	driver.find_element_by_id("valuepkg3").send_keys(int(words[8]) + int(words[10]))

elif(words[7]==("subtract")):
	driver.find_element_by_id("valuepkg3").send_keys(int(words[8]) - int(words[10]))

elif(words[8]==("first")):
	driver.find_element_by_id("valuepkg3").send_keys(int(words[10]))

else :
	driver.find_element_by_id("valuepkg3").send_keys(int(words[12]))

driver.find_element_by_id("loginbtn").click()

