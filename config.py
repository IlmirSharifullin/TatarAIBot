import os

from dotenv import load_dotenv

load_dotenv()

TRANSLATER_API_KEY = os.getenv('TRANSLATER_API_KEY')
TRANSLATER_URL = os.getenv('TRANSLATER_URL')

LOGS_CHANNEL_ID = os.getenv('LOGS_CHANNEL_ID')