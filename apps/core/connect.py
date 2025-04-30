import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def start_browser() -> WebDriver:
    """
    Initialize browser interactions and connection to Tidio via browser widget
    Please note that local HTTP server should be already running

    :return:
    """
    print("Initializing browser...")
    time.sleep(5)   # wait a couple of seconds for HTTP server to start
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:8000/')
    time.sleep(2)   # wait a couple of seconds for driver to load
    return driver

def establish_chat_session(driver: WebDriver, email: str) -> WebDriver:
    """
    Send initial message to authenticate the user and establish chat session
    Needs only on first message

    :param driver: webdriver instance
    :param email: Email for authentication for Tidio chat session
    :return: None
    """
    print("Establishing chat session...")
    WebDriverWait(driver, 10).until(
        ec.frame_to_be_available_and_switch_to_it((By.ID, "tidio-chat-iframe"))
    )

    button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "button-body"))
    )
    button.click()

    textarea = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "new-message-textarea"))
    )
    textarea.send_keys("Starting new session...")

    button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, "send-button"))
    )
    button.click()

    email_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your email...']"))
    )
    email_input.send_keys(email)

    submit = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CLASS_NAME, "tidio-1davhch"))
    )
    submit.click()

    driver.switch_to.parent_frame()
    return driver
