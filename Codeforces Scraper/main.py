import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
import shutil, os
import time
import os
from selenium.webdriver.chrome.options import Options

PATH="D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

print("Enter the contest number")
x=input()

for code in range(ord('A'), ord('Z') + 1):
        a=chr(code)
        b="https://codeforces.com/problemset/problem/" + str(x) + "/" + a
        print(b)
        driver.implicitly_wait(5)
        driver.get(b)
        time.sleep(1)

       

        if (driver.title[14] == a):
                 path = "C:/Users/HP/OneDrive/Documents/Selenium Dev Club/Codeforces Scraper/" + str(x) + "/" + a
        
                 os.makedirs(path)

                 el = driver.find_element_by_class_name('problem-statement')
                 el.screenshot('problem.png')
                 problem_path = path + "/problem.png" 
                 shutil.move("C:/Users/HP/OneDrive/Documents/Selenium Dev Club/Codeforces Scraper/problem.png", problem_path)

                 inputs = driver.find_elements_by_class_name("input")

                 a=1

                 for input in inputs:
                        txt_path = path + "/input" + str(a) + ".txt"
                
                        f = open(txt_path, "w+")
                        i = driver.find_elements_by_class_name("input")
                
                        f.write(i[a-1].text)
                        lines = f.readlines()
                        f.close()
                

                        txt_path1 = path + "/output" + str(a) + ".txt"
                
                        f = open(txt_path1, "w+")
                        i = driver.find_elements_by_class_name("output")
                
                        f.write(i[a-1].text)
                        f.close()

                
                        a=a+1

driver.quit()                
                
        

      
        

       
                
                
        

        

