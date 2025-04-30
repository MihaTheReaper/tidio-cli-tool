import sys
import threading
import time

from selenium.common import InvalidSessionIdException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ReceiverThread(threading.Thread):
    def __init__(self, driver: WebDriver):
        threading.Thread.__init__(self)
        self.driver = driver
        self.seen = set()

    def receive_message(self):
        """
        Receive message from Tidio

        :return:
        """
        try:
            WebDriverWait(self.driver, 5).until(
                ec.frame_to_be_available_and_switch_to_it((By.ID, "tidio-chat-iframe"))
            )

            messages = WebDriverWait(self.driver, 5).until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".message-operator .message-content"))
            )
            for msg in messages:
                text = msg.text
                if text not in self.seen:
                    print("Received message:", text)
                    self.seen.add(text)

            self.driver.switch_to.parent_frame()
        except InvalidSessionIdException:
            raise
        except Exception as exc:
            print(f"Failed to get message: {str(exc)}")
            self.driver.refresh()


    def run(self):
        try:
            while True:
                self.receive_message()
                time.sleep(1)
        except Exception as exc:
            print(f"Failed to process received message, session dropped or invalid: {str(exc)}")
        finally:
            self.driver.quit()
            sys.exit(1)