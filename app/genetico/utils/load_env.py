import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../.env'))

load_dotenv(dotenv_path)

def get_env(key, default=None):
    return os.getenv(key, default)
