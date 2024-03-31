# Comics publisher
A small script that downloads one comic from [xkcd](https://xkcd.com/) and posts it in public telegram channel.

## How to install
Download github repository and install python libraries from `requirements.txt`:
```bash
git clone https://github.com/AlexRikka/devman_xkcd.git
cd devman_xkcd
pip install -r requirements.txt
```

You will need telegram API tokens. Create `.env` file in project folder and add next token variables to it: 
- TG_BOT_HTTP_KEY = telegram bot token.
- TG_CHANNEL_NAME = telegram channel link in @name format.

Run script with following command:  
```
python main.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.