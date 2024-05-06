# gunicorn_config.py
import os
from dotenv import load_dotenv

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Gunicorn config
bind = "0.0.0.0:8000"
workers = 1