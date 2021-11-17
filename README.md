# EasyFile

To run the backend framework, you need to config in `instance/config.py` 
```python
DEBUG = True
SECRET_KEY = 'dev'
DATABASE = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'my_pass_word_for_mysql',
    'db': 'the_database_to_use'
}
TEMP_PATH = r'D:\Downloads\EasyFile\temp'
```

1. run `flask init-db` to create tables
2. run `flask run`
