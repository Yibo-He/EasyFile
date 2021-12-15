# EasyFile


### Readme

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


#### Some bugs to be fixed:

1. 出现处理错误的时候没有反馈到前端上，下载的时候是一个空的`json`文件?
2. 处理长度大于1的列表似乎有问题
3. entity tagger应该作为全局变量，在初始化的时候Load进来。现在发送请求之后每次都要重新load，要等10秒，因为g不管用...

#### Fixed bugs (to be checked):

1. 处理不了`.doc`（可以不用解决，但是要写清楚提示，之前的提示是上传错误，现在已经改过了）



#### Entity Recognition

把“转换前的字符串”写成`<ENT>`, 就会识别所有的entity然后进行转换。如果不改内容，则把“转换前的字符串”也写成`<ENT>`。
