from dotenv import dotenv_values
import os

config = dotenv_values("../.env")
TOKEN = config.get('7800222511:AAHsM7pQUjnKr655TD9TuZI1kgZGQEgP4Do')
ADMIN_ID = config.get('259158244')
API_URL = f"https://api.telegram.org/bot{TOKEN}/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))