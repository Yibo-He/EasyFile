# EasyFile

## Backend

After you clone this repo, please

1. create `temp` folder in the root directory
2. create `instance/config.py`, and config following this template

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
TEMP_PATH = r'/c/Users/.../temp'  # must be a absolute path
```

3. run `flask init-db` to create tables

4. run `flask run`

## Frontend

## Project setup

```
npm install

npm install axios
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
