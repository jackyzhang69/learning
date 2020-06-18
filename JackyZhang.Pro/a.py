from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from selenium.webdriver.common.keys import Keys
import time



def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'html.parser')
    return soupdata


def getNoc():
    driver = webdriver.Chrome()
    url = "https://www.jobbank.gc.ca/wagereport/occupation/20977"
    driver.get(url)

    inputbox=driver.find_element_by_id("ec-wages:wagesInput")
    inputbox.clear()

    
    inputbox.send_keys('0114')

    driver.execute_script("document.getElementById(\"ec-wages:j_id_73_3_k\").click")

    mytable=driver.find_elements_by_css_selector('td')
    print(mytable[5].)

    time.sleep(10)


getNoc()



