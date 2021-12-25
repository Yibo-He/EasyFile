# EasyFile

First you should clone this repo, and then do the following steps to run the backend and front end

## Backend

1. Enter the directory of backend(./backend)
2. Install ghostscript and mysql. If you are using ubuntu, you can run:
```
sudo apt install ghostscript mysql-server python3-flask
```
3. Install the python package required by running:
```
pip3 install -r requirements.txt
```

4. Setup mysql and create a database for this project
4. Create `temp` folder `storage` folder in the root directory of backend
5. Create `instance/config.py`, and config following this template

```python
DEBUG = False
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
TEMP_PATH = r'/.../temp'  # must be a absolute path
STORAGE_PATH = r'/.../storage'  # must be a absolute path
```

3. Run `flask init-db` to create tables
4. Run `flask run`

## Frontend

1. Enter the directory of frontend(./frontend)
2. Install npm. If you are using ubuntu, you can install it by the following instruction:
```
sudo apt install npm
```
3. Setup frontend by the following instructions:
```
npm install
npm install axios
```
4. Begin to serve by the following command:

```
npm run serve
```
## Deployment
If you are just testing it on your local computer, you can ignore the follow steps, and access `localhost:8080` to use `EasyFile`.

If you want to deploy this system on a server, you should do the follow things:

1. Find all `localhost:5000` in the code of file `*.vue` of frontend and replace them with `ip:port`(the ip address must can be access by the clients)
2. Run the backend by `flask run -p port -h 0.0.0.0` rather than above
3. Build the frontend by:
```
npm run build
```
4. Setup a nginx server
(If you are not so sensitive to loading speed, you can ingore 3. and 4. and run front end by `npm run serve`)

