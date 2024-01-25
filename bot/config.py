import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', None)
DB_URL = os.getenv('DB_URL', None)
