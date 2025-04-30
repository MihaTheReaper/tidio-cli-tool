import sys
import threading
import time

from selenium.common import InvalidSessionIdException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SenderThread(threading.Thread):
    def __init__(self, driver: WebDriver):
        threading.Thread.__init__(self)
        self.driver = driver

    def send_message(self, message: str) -> None:
        """
        Send message to Tidio

        :param message: message to send
        :return: None
        """
        try:
            WebDriverWait(self.driver, 5).until(
                ec.frame_to_be_available_and_switch_to_it((By.ID, "tidio-chat-iframe"))
            )

            textarea = WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.ID, "new-message-textarea"))
            )
            textarea.send_keys(message)

            button = WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.ID, "send-button"))
            )
            button.click()

            self.driver.switch_to.parent_frame()
        except InvalidSessionIdException:
            raise
        except Exception as exc:
            print(f"Failed to send message: {str(exc)}")
            self.driver.refresh()


    def run(self):
        time.sleep(2)   # wait for first received message from Tidio chat
        print("Type messages:")
        try:
            while True:
                user_input = input(">> ")
                if user_input.lower() == 'exit':
                    raise KeyboardInterrupt
                if user_input:
                    self.send_message(user_input)
                time.sleep(1)
        except Exception as exc:
            print(f"Failed to process sending of message, session dropped or invalid: {str(exc)}")
        finally:
            self.driver.quit()
            sys.exit(1)
