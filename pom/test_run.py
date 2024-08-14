from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import random
import string
from pom.pages.contact_us_page import ContactPage
from pom.pages.search_next_page import SearchPage
from pom.pages.scroll_page import ScrollPage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    #yield the driver
    yield driver
    #close the driver
    driver.quit()

def generate_random_email():
    domain = "test.com"
    email_length = 8
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=5))

def generate_random_phone():
    return "98" + ''.join(random.choices(string.digits, k=8))

def test_random_generator(driver):
    name = generate_random_name()
    email = generate_random_email()
    phone = generate_random_phone()
    contact_page=ContactPage(driver)
    contact_page.open_contact_page("https://www.nepalec.edu.np/contact-us")
    driver.maximize_window()
    time.sleep(1)
    contact_page.enter_name(name)
    time.sleep(1)
    contact_page.enter_phone(phone)
    time.sleep(1)
    contact_page.enter_email(email)
    time.sleep(1)
    contact_page.click_education()
    time.sleep(1)
    contact_page.click_course()
    time.sleep(1)
    contact_page.enter_percentage("75%")
    time.sleep(1)
    contact_page.click_country()
    time.sleep(1)

    #check to see email is valid or not
    if contact_page.is_valid_email(email):
        print(f"{email} is valid email address")
    else:
        print(f"{email} is invalid email address")

    #check to see phone number is valid or not
    if contact_page.is_valid_phone(phone):
        print(f"{phone} is valid phone number")
    else:
        print(f"{phone} is invalid phone number")


def test_search_next_page(driver):
    search_page=SearchPage(driver)
    search_page.open_sharesansar_page("https://www.sharesansar.com/")
    driver.maximize_window()
    time.sleep(1)
    search_page.do_search("NIBLACE")
    time.sleep(1)
    search_page.submit_search()
    time.sleep(1)
    search_page.click_news()
    time.sleep(1)
    search_page.click_page2()
    time.sleep(1)
    search_page.click_page3()
    time.sleep(1)

def test_scroll_page(driver):
    scroll_page=ScrollPage(driver)
    scroll_page.open_gadgetbyte_page("https://www.starbucks.com/")
    driver.maximize_window()
    time.sleep(1)
    scroll_page.scroll_home_page()
    time.sleep(1)
    scroll_page.click_link()
    time.sleep(1)
    scroll_page.scroll_learn_more_page()
    time.sleep(1)

