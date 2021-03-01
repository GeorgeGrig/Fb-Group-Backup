from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import itertools

download_dir = 'D:\\Programming\\Current\\Fb-Group-Backup\\Downloads'
groupUrl = 'https://www.facebook.com/groups/PhysicsDepThess/'

# Set Firefox preferences so that the file automatically saves to disk when downloaded
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.dir",download_dir)
profile.set_preference("browser.download.folderList",2)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/pdf,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream')
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.helperApps.neverAsk.openFile","application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.useWindow", False)
profile.set_preference("browser.download.manager.focusWhenStarting", False)
profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference("browser.download.manager.closeWhenDone", True)
profile.set_preference("pdfjs.disabled", True)


# todo
# add show newest files first
# get more info from post (poster name and post date)
def login():
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.facebook.com/login/web/')
    input()
    return driver

def goto_group_files(groupUrl,driver):
    #Navigate to group files
    driver.get(groupUrl+'files/')
    # Scroll down to reveal all files
    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # Get all triple dots button locations
    dots = driver.find_elements_by_css_selector('span.tmrshh9y.pfnyh3mw.j83agx80.bp9cbjyn')
    top_bar = driver.find_element_by_css_selector('div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y')
    download_urls = []
    #Scroll back to the top
    driver.execute_script("window.scrollTo(0, 220)")
    time.sleep(1)
    #For each dot, might skip the first two
    for dot in dots:
        if not dot == dots[0]  and not dot == dots[1]:
            view_port_height = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
            element_top = "var elementTop = arguments[0].getBoundingClientRect().top;"
            js_function = "window.scrollBy(0, elementTop-(viewPortHeight/2));"
            scroll_into_middle = view_port_height + element_top + js_function
            driver.execute_script(scroll_into_middle, dot)
            ActionChains(driver).click(dot).perform()
            time.sleep(1)
            # Get download link from current dot
            try:
                download_urls.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/a[1]").get_attribute('href'))
            except:
                print('Failed to find download button')
            time.sleep(1)
            # Click on top bar to hide previous download button
            ActionChains(driver).click(top_bar).perform()
            print(len(download_urls))
        k = 1
    for url in download_urls:
        print(f'Now doing file: {k} out of {len(download_urls)}')
        k +=1
        driver.get(url)
        time.sleep(2)

driver = login()
goto_group_files(groupUrl,driver)