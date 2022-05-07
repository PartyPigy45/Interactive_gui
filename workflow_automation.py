import selenium
from selenium import webdriver as wb
import os
from os import path as ps
import time

# TO DO deal with the differrent functions required to initialise the web driver
# remove the variables below and the time dependent checks used by the workflow
# use unittesting to develop the selenium api
TargetJobs = 'https://targetjobs.co.uk/internships'
Muse_url = 'https://www.sheffield.ac.uk/'
Gradcracker = 'https://www.gradcracker.com/search/all-disciplines/engineering-jobs'
drive_cpe260 = 'https://drive.google.com/drive/u/1/folders/0ADQwLtxBAjhwUk9PVA'
drive_cpe270 = 'https://drive.google.com/drive/u/1/folders/0ACNSaKFc0HonUk9PVA'
jm_board = 'https://jamboard.google.com/d/1SqHIdqVxT_se4BaCzIXfmmAqj0j6mEfxB31kEBx-xLI/viewer?f=2'
emg_drive = 'https://drive.google.com/drive/u/1/folders/0AL6GBsvh_FEMUk9PVA'
documents_python = 'https://docs.python.org/3/library/functions.html#func-list'
subject_code = 0
exceptiontime = 120
session_lenght = 120
email_read_time = 10

# open the email untill the read time has expired and calls the blackboard website


def workflow_automation(e_mail, email_read_time):
    x = ps.abspath(r'automated_system\msedgedriver.exe')
    driver = wb.Edge(x)

    # open email and log in
    if e_mail == True:
        driver.get('https://mail.google.com/mail/u/1/#inbox')
        search_box = driver.find_element_by_id('identifierId')
        search_box.send_keys('kuisoko1@sheffield.ac.uk')
        next_buttom = driver.find_element_by_id("identifierNext")
        try:
            next_buttom.click()
        except selenium.common.exceptions.ElementClickInterceptedException as err:
            logger.info(err)
            time.sleep(20)
        time.sleep(10)
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(60*email_read_time)
    else:
        pass

    # blackboard
    driver.get('https://vle.shef.ac.uk/?new_loc=%2Fultra%2Fcourse')
    cookiebox = driver.find_element_by_id('agree_button')
    cookiebox.click()
    userBox = driver.find_element_by_id("user_id")
    userBox.send_keys('fca19kui')
    passwordBox = driver.find_element_by_id('password')
    passwordBox.send_keys('keslerisoko20')
    driver.find_element_by_id('entry-login').click()
    time.sleep(60*session_lenght)


def get_driver(url):
    # setup the driver
    x = ps.abspath(r'msedgedriver.exe')
    driver = wb.Edge(x)

    driver.get(url)
    return driver


def textbooks_opener():
    os.system('start C:/Users/Uchek/OneDrive/Documents/TextBooks')


def get_timetable():
    url = 'https://cmisgonow.sheffield.ac.uk/CMISGo/Web/Timetable'
    x = ps.abspath(r'automated_system\msedgedriver.exe')
    driver = wb.Edge(x)
    driver.get(url)
    time.sleep(10)
    username_search_box = driver.find_element_by_id('username')
    username_search_box.send_keys('fca19kui')
    password_searchbox = driver.find_element_by_id('password')
    password_searchbox.send_keys('keslerisoko20')
    login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
    login_button.click()
    time.sleep(60)


def initialize_workflow(launch):
    os.system('start C:/Users/Uchek/OneDrive/Documents/INSTRUCTION.docx')
    os.system('start C:/Users/Uchek/OneDrive/Documents/Gymnasium.xlsx')
    os.system('start C:/Users/Uchek/OneDrive/Documents/Routine_modified.xlsx')
    os.system('start https://pomofocus.io')
    os.system('start https://docs.google.com/document/d/1lKFhkwju1F5U8LuJYR0_oiIpeLQ8wPCnQoJZKmATgEE/edit')  # drive
    os.system('start https://www.taskade.com/d/zoYsBwsZ7nM6KQhv')  # taskade

    if 'tasks.docx' in launch:
        os.system('start C:/Users/Uchek/OneDrive/Documents/Tasks.docx')
    if 'data structures & Oh.docx' in launch:
        os.system(
            'start C:/Users/Uchek/OneDrive/Documents/DATA_STRUCTURES_AND_BIG_OH.docx')
    if 'data structures and algorithms textbook' in launch:
        os.system(
            'start C:/Users/Uchek/OneDrive/Documents/Data_Structures_and_Algorithms_in_Python.pdf')

    if 'refactoring notes.docx' in launch:
        os.system('start C:/Users/Uchek/OneDrive/Documents/REFACTORING_NOTES.docx')

    if 'clean code.docx' in launch:
        os.system('start C:/Users/Uchek/OneDrive/Documents/Clean_Code.docx')

    if 'mathematics for cs.docx' in launch:
        os.system(
            'start C:/Users/Uchek/OneDrive/Documents/Mathematics_For_Computer_Science.docx')

    if 'why stopped log.docx' in launch:
        os.system('start C:/Users/Uchek/OneDrive/Documents/WHY_STOPPED_Log.docx')

    if 'routine modified.xlsx' in launch:
        os.system(
            'start C:/Users/Uchek/OneDrive/Protocol/Src/Database/Routine_modified.xlsx')

    if 'web development notes.docx' in launch:
        os.system(
            'start C:/Users/Uchek/OneDrive/Documents/Web_development_notes.docx')

    get_timetable()

    try:
        workflow_automation(True, 5)
    except:
        while True:
            time.sleep(60*exceptiontime)


def get_website(url, uni_website=False, check_time=120):
    if uni_website:
        driver = get_driver(url)
        username_search_box = driver.find_element_by_id('username')
        username_search_box.send_keys('fca19kui')
        password_searchbox = driver.find_element_by_id('password')
        password_searchbox.send_keys('keslerisoko20')
        login_button = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
        login_button.click()
        time.sleep(6)
        push_button = driver.find_element_by_xpath(
            '//*[@id="auth_methods"]/fieldset/div[1]/button')
        push_button.click()
        time.sleep(check_time)
    else:
        if url.startswith('htt'):
            driver = get_driver(url)
            time.sleep(check_time)
        else:
            get_driver(f'https://www.bing.com/search?q={url}')
            time.sleep(check_time)
