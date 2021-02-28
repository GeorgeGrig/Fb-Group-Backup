from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#options = Options()
#options.headless = False
download_dir = 'D:\\Programming\\Current\\Fb-Group-Backup\\Downloads'
# Set Firefox preferences so that the file automatically saves to disk when downloaded

#fp.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/pdf,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream')
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

groupUrl = 'https://www.facebook.com/groups/PhysicsDepThess/'
def login():
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.facebook.com/login/web/')
    input()
    return driver

def navigate_group(groupUrl,driver):
    driver.get(groupUrl)

def goto_group_files(groupUrl,driver):
    driver.get(groupUrl+'files/')
    SCROLL_PAUSE_TIME = 1
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
    dots = driver.find_elements_by_css_selector('span.tmrshh9y.pfnyh3mw.j83agx80.bp9cbjyn')
    download_urls = []
    #driver.execute_script("window.scroll(0, 0);")
    time.sleep(1)
    for dot in dots:
        if not dot == dots[0]:
            driver.execute_script("arguments[0].scrollIntoView();",dot)
            ActionChains(driver).click(dot).perform()
            time.sleep(1)
            download_urls.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/a[1]").get_attribute('href'))
            time.sleep(1)
            ActionChains(driver).click(dot).perform()
            print(len(download_urls))
        k = 1
    for url in download_urls:
        print(f'Now doing file: {k} out of {len(download_urls)}')
        k +=1
        driver.get(url)
        time.sleep(1)

driver = login()
goto_group_files(groupUrl,driver)