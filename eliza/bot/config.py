import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


# check all vars
if TOKEN is None:
    raise ValueError("Telegram TOKEN is invalid.")
