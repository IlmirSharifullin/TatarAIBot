import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

TRANSLATER_API_KEY = os.getenv('TRANSLATER_API_KEY')
TRANSLATER_URL = os.getenv('TRANSLATER_URL')

LOGS_CHANNEL_ID = os.getenv('LOGS_CHANNEL_ID')


DB_URL = os.getenv('DB_URL')
TEMP_PROXY = os.getenv('TEMP_PROXY')

engine = create_async_engine(url=DB_URL, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
