import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))

DB_PATH = os.getenv("DB_PATH")
