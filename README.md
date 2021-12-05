# EasyFile

#### Bugs:

1. 出现处理错误的时候没有反馈到前端上，下载的时候是一个空的json文件
2. 处理不了`.doc`（暂时先不解决了，但是要写清楚提示）
3. 下载时遇到问题`127.0.0.1 - - [05/Dec/2021 15:11:48] "GET /download/formatted_haoshibo&13&xxx.docx│  App running at:
    HTTP/1.1" 404 -`



### Readme

After you clone this repo, please

1. create `tmp` folder in the root directory
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

