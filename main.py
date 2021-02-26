from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import time

options = Options()
options.headless = False

groupUrl = 'https://www.facebook.com/groups/PhysicsDepThess/'
def login():
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.facebook.com/login/web/')
    input()
    return driver

def navigate_group(groupUrl,driver):
    driver.get(groupUrl)

def goto_group_files(groupUrl,driver):
    driver.get(groupUrl+'files/')
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    dots = driver.find_elements_by_class_name("tmrshh9y pfnyh3mw j83agx80 bp9cbjyn")
    for dot in dots:
        ActionChains(driver).click(dot).perform()
        download = driver.find_element_by_class_name("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb").get_attribute('href')
        driver.get(download)