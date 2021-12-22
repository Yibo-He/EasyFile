DEBUG = True
SECRET_KEY = 'dev'
SALT = 'dev'
ACCESS_TOKEN_EXPIRES_IN = 1800
REFRESH_TOKEN_EXPIRES_IN = 86400

DATABASE = {
    "host": "127.0.0.1",
    "port": 3306,
    'user': "user",
    'passwd': "passwd",
    'db':   "EasyFile"
}

TEMP_PATH = r'TEMP_PATH'
STORAGE_PATH = r'STORAGE_PATH'