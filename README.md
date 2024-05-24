# Comics publisher
A small script that downloads one comic from [xkcd](https://xkcd.com/) and posts it in public telegram channel.

## Environment

### Requirements
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2). Download github repository and install python libraries from `requirements.txt`:
```bash
git clone https://github.com/AlexRikka/devman_xkcd.git
cd devman_xkcd
pip install -r requirements.txt
```

### Environment variables
You will need telegram API tokens. Create `.env` file in project folder and add next token variables to it: 
- TG_BOT_HTTP_KEY = telegram bot token.
- TG_CHANNEL_NAME = telegram channel link in @name format.

## Run
Run script with following command:  
```
python main.py
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org).