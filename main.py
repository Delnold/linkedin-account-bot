import json
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH_CHROME_DRIVER = r"ChromeDriver/chromedriver.exe"
URL_LINKEDIN = r"https://www.linkedin.com/"
URL_ACCOUNT_REDIRECT = URL_LINKEDIN + 'in/'
URL_ACCOUNT = ''
URL_ADD_POSITION = "/edit/forms/position/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB"
URL_ADD_PHOTO = "/edit/photo/"
URL_ADD_SUMMARY = "/edit/forms/summary/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB"
URL_ADD_EDUCATION = "/edit/forms/education/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB"
URL_ADD_SKILLS = "/edit/forms/skills/new/?profileFormEntryPoint=PROFILE_COMPLETION_HUB"
EMAIL = input("Email: ")
PASSWORD = input("Password: ")

p_file = open('DataRelated/positions.json')
positions_data = json.load(p_file)

s_file = open('DataRelated/summaries.json')
summary_data = json.load(s_file)

e_file = open('DataRelated/educations.json')
educations_data = json.load(e_file)

s_file = open('DataRelated/skils.json')
skills_data = json.load(s_file)

positions_entries = len(positions_data)
educations_entries = len(educations_data)
skills_entries = len(skills_data)

DELAY = 5

def launch():
    print('Choose the name of the browser for your webdriver:\n' +
          '[1] Chrome\n' +
          '[2] Firefox\n' +
          '[3] Safari\n' +
          '[4] IE \n' +
          '(If the input is incorrect, the default webdriver will be \n' +
          'chromedriver_win32" (ChromeDriver 109.0.5414.74)')

    driver_choice = input('Choice: ')

    choose_webdriver(driver_choice)


def choose_webdriver(driver_choice):

    if driver_choice not in ["1", "2", "3", "4"]:
        print('Invalid choice. Setting up chrome as default')
        service = Service(PATH_CHROME_DRIVER)
        driver = webdriver.Chrome(service=service)
        account_login(driver)
        return

    path_webdriver = input("Provide absolute path to your webdriver (*.exe): ")
    service = Service(path_webdriver)

    if driver_choice is "1":
        driver = webdriver.Chrome(service=service)
    elif driver_choice is "2":
        driver = webdriver.Firefox(service=service)
    elif driver_choice is "3":
        driver = webdriver.Safari(service=service)
    else:
        driver = webdriver.Ie(service=service)
    account_login(driver)
    driver.quit()

def account_login(driver):
    global URL_ACCOUNT
    driver.get(URL_LINKEDIN)
    email_form = driver.find_element(By.ID, "session_key")
    password_form = driver.find_element(By.ID, "session_password")

    email_form.send_keys(EMAIL)
    password_form.send_keys(PASSWORD)
    password_form.submit()

    print('Signing in...')

    soup = BeautifulSoup(driver.page_source, "html.parser")
    if soup.find('div', {'id': 'error-for-password'}):
        print('Error! Please verify your username and password.')
        driver.quit()
    elif driver.title == '403: Forbidden':
        print('LinkedIn is momentarily unavailable. Please wait a moment, then try again.')
        driver.quit()
    else:
        print('Success!\n')

    driver.get(URL_ACCOUNT_REDIRECT)
    URL_ACCOUNT = driver.current_url

    for i in range(positions_entries):
        add_position(driver, i)
    for i in range(educations_entries):
        add_education(driver, i)
    for i in range(skills_entries):
        add_skills(driver, i)
    add_summary(driver)

def add_position(driver, i):
    driver.get(URL_ACCOUNT + URL_ADD_POSITION)
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-title"]')))
        print("Add_Position page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    title_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-title"]')
    employment_form = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-employmentStatus"]')
    company_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-requiredCompany"]')
    location_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-geoPositionLocation"]')
    location_type = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-locationType"]')
    start_date_month_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-start-date"]')
    start_date_year_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-start-date-year-select"]')
    industry_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-industryId"]')
    description_form = driver.find_element(By.XPATH, '//*[@id="multiline-text-form-component-profileEditFormElement-POSITION-profilePosition-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-description"]')

    title_form.clear()
    company_form.clear()
    location_form.clear()
    industry_form.clear()
    description_form.clear()

    title_form.send_keys(positions_data[i]["Title"])
    employment_form.send_keys(positions_data[i]["Employment type"])
    company_form.send_keys(positions_data[i]["Company Name"])
    location_form.send_keys(positions_data[i]["Location"])
    location_type.send_keys(positions_data[i]["Location type"])
    start_date_month_form.send_keys(positions_data[i]["Start date"][0])
    start_date_year_form.send_keys(positions_data[i]["Start date"][1])
    industry_form.send_keys(positions_data[i]["Industry"])
    description_form.send_keys(positions_data[i]["Description"])

    submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button/span')
    submit_button.click()

    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div')))
        print("Position applied!")
    except TimeoutException:
        print("Loading took too much time!")

def add_summary(driver):
    driver.get(URL_ACCOUNT + URL_ADD_SUMMARY)
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, '//*[@id="multiline-text-form-component-profileEditFormElement-SUMMARY-profile-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-summary"]')))

        print("Summary page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    summary_area = driver.find_element(By.XPATH, '//*[@id="multiline-text-form-component-profileEditFormElement-SUMMARY-profile-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-summary"]')
    summary_area.clear()
    summary_area.send_keys(summary_data[0]["summary"])

    submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button/span')
    submit_button.click()

    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember414"]')))
        print("Summary applied!")
    except TimeoutException:
        print("Loading took too much time!")


def add_education(driver, i):
    driver.get(URL_ACCOUNT + URL_ADD_EDUCATION)
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH,
                                                                           '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-school"]')))
        print("Add_Education page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    school_form = driver.find_element(By.XPATH,'//*[@id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-school"]')
    degree_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-degree"]')
    field_of_study = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-fieldsOfStudy"]')
    start_date_month_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-start-date"]')
    start_date_year_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-start-date-year-select"]')
    end_date_month_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-end-date"]')
    end_date_year_form = driver.find_element(By.XPATH, '//*[@id="date-range-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-dateRange-end-date-year-select"]')
    grade_form = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-grade"]')
    activities_form = driver.find_element(By.XPATH, '//*[@id="multiline-text-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-activities"]')
    description_form = driver.find_element(By.XPATH, '//*[@id="multiline-text-form-component-profileEditFormElement-EDUCATION-profileEducation-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-notes"]')

    school_form.clear()
    degree_form.clear()
    field_of_study.clear()
    grade_form.clear()
    activities_form.clear()
    description_form.clear()

    school_form.send_keys(educations_data[i]["School"])
    degree_form.send_keys(educations_data[i]["Degree"])
    field_of_study.send_keys(educations_data[i]["Field of study"])
    start_date_year_form.send_keys(educations_data[i]["Start date"][1])
    start_date_month_form.send_keys(educations_data[i]["Start date"][0])
    end_date_year_form.send_keys(educations_data[i]["End date"][1])
    end_date_month_form.send_keys(educations_data[i]["End date"][0])
    grade_form.send_keys(educations_data[i]["Grade"])
    activities_form.send_keys(educations_data[i]["Activities and societies"])
    description_form.send_keys(educations_data[i]["Description"])

    submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button/span')
    submit_button.click()

    try:
        WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div')))
        print("Education applied!")
    except TimeoutException:
        print("Loading took too much time!")

def add_skills(driver, i):
    driver.get(URL_ACCOUNT + URL_ADD_SKILLS)
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH,
                                                                           '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-SKILL-AND-ASSOCIATION-skill-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-name"]')))
        print("Add_skills page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    skills_form = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-profileEditFormElement-SKILL-AND-ASSOCIATION-skill-ACoAAECTwVEBKX69x4pkEzGcik-8byRm1ef0Jas-1-name"]')
    skills_form.clear()
    skills_form.send_keys(skills_data[i]["skills"])

    submit_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button/span')
    submit_button.click()

    try:
        WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div[1]/div/div/div')))
        print("Skills applied!")
    except TimeoutException:
        print("Loading took too much time!")



"""
Function can`t work due to strange behaviour of Submit button
def add_profile_picture(driver):
    driver.get(URL_ACCOUNT + URL_ADD_PHOTO)
    time.sleep(3)
    photo = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/footer/div/label')
    photo.send_keys("DataRelated/Photos/Male_1.jpg")
"""

if __name__ == "__main__":
    launch()

