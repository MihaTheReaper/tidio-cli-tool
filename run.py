import sys
import threading

from apps.core.connect import start_browser, establish_chat_session
from apps.http_server.server import start_server
from apps.receiver.receive import ReceiverThread
from apps.sender.send import SenderThread


print("Tidio CLI Tool started...")

ppk = input("Enter Tidio Public Key: ")

if not ppk:
    print(f"Tidio Public Key cannot be empty")
    sys.exit(1)

email = input("Enter your email address for Tidio login: ")

if not email:
    print(f"Email address cannot be empty")
    sys.exit(1)



# Start HTTP server
try:
    http_server = threading.Thread(target=start_server, args=(ppk, ), daemon=True).start()
except Exception as exc:
    print(f"Failed to start HTTP server: {str(exc)}")
    sys.exit(1)

# Start browser
try:
    driver = start_browser()
except Exception as exc:
    print(f"Failed to start browser: {str(exc)}")
    sys.exit(1)

# Establish chat session and make authentication
try:
    driver = establish_chat_session(driver, email)
except Exception as exc:
    print(f"Failed to connect to Local url: {str(exc)}")
    sys.exit(1)

# Start handling receive of messages from Tidio
receiver_thread = ReceiverThread(driver=driver)
receiver_thread.start()

# Start handling sending of messages to Tidio
starter_thread = SenderThread(driver=driver)
starter_thread.start()