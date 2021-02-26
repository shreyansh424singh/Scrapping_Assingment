import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil
import os

PATH="D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://codeforces.com/problemset")

a= input("Enter min difficulty")
b= input("Enter max difficulty")
c= int(input("number of problems you need"))
d=0

driver.find_element_by_name("minDifficulty").send_keys(a)
driver.find_element_by_name("maxDifficulty").send_keys(b)
path = "C:/Users/HP/OneDrive/Documents/Selenium Dev Club/Bonus Task 2/Difficulty level" + str(a) +" to " + str(b) 
os.makedirs(path)

driver.find_element_by_class_name("_FilterByTagsFrame_button").click()

el = driver.find_element_by_class_name("datatable").text
ele = el.splitlines()
l=len(ele)

for i in range(2, l, 4):
    if (d==c):
        break
    d=d+1
    
    num= str(ele[i])

    b1=""
    a1=""

    c1=1
    for k in num:
        if(c1<5):
            b1=b1+k
       
        else:
            a1+=k
        c1=c1+1

    b="https://codeforces.com/problemset/problem/" + b1 + "/" + a1
    driver.implicitly_wait(5)
    driver.get(b)
    time.sleep(1)

    path1 = path +"/" + num
        
    os.makedirs(path1)

    el = driver.find_element_by_class_name('problem-statement')
    el.screenshot('problem.png')
    problem_path = path1 + "/problem.png" 
    shutil.move("C:/Users/HP/OneDrive/Documents/Selenium Dev Club/Bonus Task 2/problem.png", problem_path)

    inputs = driver.find_elements_by_class_name("input")

    a=1

    for input in inputs:
                        txt_path = path1 + "/input" + str(a) + ".txt"
                
                        f = open(txt_path, "w+")
                        i = driver.find_elements_by_class_name("input")
                
                        f.write(i[a-1].text)
                        lines = f.readlines()
                        f.close()
                

                        txt_path1 = path1 + "/output" + str(a) + ".txt"
                
                        f = open(txt_path1, "w+")
                        i = driver.find_elements_by_class_name("output")
                
                        f.write(i[a-1].text)
                        f.close()

                
                        a=a+1

    
    
 
driver.quit()
    


