# EasyFile

To run the backend framework, you need to config in `instance/config.py`

```python
DEBUG = True
SECRET_KEY = 'dev'                  # Just as an example, not the value we actually use
SALT = 'dev'                        # Just as an example, not the value we actually use
ACCESS_TOKEN_EXPIRES_IN = 1800
REFRESH_TOKEN_EXPIRES_IN = 86400

DATABASE = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'my_pass_word_for_mysql',
    'db': 'the_database_to_use'
}
TEMP_PATH = r'./temp'
```

1. run `flask init-db` to create tables
2. run `flask run`
