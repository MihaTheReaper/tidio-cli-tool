# Tidio CLI Tool 

## Summary
### This application Selenium Python library to simulate user action to interact with Tidio chat.
The core functionality of your program should include:
1. [x] Initialization: using Tidio Public Key and Email address
2. [x] Connecting to the Tidio Chat: Establish a connection to the chat vi Chrome by using the chat identifiers.
3. [x] Sending Messages: a user can send messages via the terminal with 1 second interval between them
4. [x] Receiving Messages: Receiving messages are not block the ability to send messages and received with 1 second polling interval
5. [x] All sent and received messages are logged into terminal
6. [x] Error Handling: implemented where needed

### Before running the application a user need to have the following information:
* Tidio Public Key
* Email address for Tidio login

### Important Note
* Direct Websocket option currently not supported. Tidio does not offer a WebSocket API for real-time communication.
* Using Tidio's OpenAPI and Webhooks cannot be used with Tidio free account


## Requirements
* Python 3.12.10+
* Selenium 
* Chrome installed

## Dev Tool
* PyCharm 2025.1

## Assumptions
* User should want 1 second before typing new message
* Received messages polling interval is 1 second

### Setup environment

#### Install requirements
```console
pip install -r requirements.txt
```

#### Install Chrome
```
Install Chrome browser on your local machine
```

#### 

### Tidio 
* Register on Tidio
* Login to Tidio using your credentials
* Open live conversations tab in your Tidio
* Join conversion to interact with client


### Clone Repository (GitHub)

```console
git clone MihaTheReaper/tidio-cli-tool
```

### Run the Tool

```console
run.py
```

### Closing the Tool
```console
KeyboardInterrupt or enter 'exit' into the chat
```
Please note that closing the application could take a couple of seconds