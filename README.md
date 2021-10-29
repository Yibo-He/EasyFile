<<<<<<< HEAD
# Test of branch backend_gmq 
=======
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
```

1. run `flask init-db` to create tables
2. run `flask run`
>>>>>>> 7e6f5a4bb14f47b32c16e4fad5104e17cd5d88dd
