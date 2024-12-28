from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os 
import sys


application_path=os.path.dirname(sys.executable)
now=datetime.now()
dd_mm_yy=now.strftime("%d %m %y")

option = Options()
option.add_argument('--headless=new')

option.binary_location='C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
website="https://www.thesun.co.uk/sport/football/"
path="C:/Users/user/.cache/selenium/chromedriver/win64/131.0.6778.204/chromedriver.exe"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service,options=option)    

driver.get(website)
# driver.implicitly_wait(2)

containers=driver.find_elements(by='xpath',value='//div[@class="teaser__copy-container" and .//a[@href]]')

# containers = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((, '//div[@class="teaser__copy-container"]'))
# )



titles=[]
subtitles=[]
links=[]

for container in containers:
    title=container.find_element(by='xpath',value='./a/span').text
    subtitle=container.find_element(by='xpath',value='./a/h3').text
    # try:
    link=container.find_element(by='xpath',value='./a').get_attribute("href")
    # except:
    #     link="N/A"
    # this would become container instead of driver 
    # print("--------------------------------------------\n")
    # print(container.get_attribute('outerHTML'))
    # print("\n--------------------------------------------")



    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    



my_dict={'title':titles,'subtitles':subtitles,'link':links}

df_headlines=pd.DataFrame(my_dict)

neuz_filename=f"headline{dd_mm_yy}.csv"
saving_loc=os.path.join(application_path,neuz_filename)

df_headlines.to_csv(saving_loc)

driver.quit()

