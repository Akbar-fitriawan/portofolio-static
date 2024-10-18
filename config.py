import os
from os import path
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()


class Config:
    # Mengambil konfigurasi dari environment variables atau fallback ke default value
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    # Debugging
    DEBUG = True




