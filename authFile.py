import requests
import config as cfg

def oauth_login():
    CLIENT_ID = cfg.clientID
    SECRET_TOKEN = cfg.secretToken
    GRANT_TYPE = cfg.grantType
    USERNAME = cfg.username
    PASSWORD = cfg.password

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

    data = {'grant_type': GRANT_TYPE, 'username': USERNAME, 'password': PASSWORD }

    headers = cfg.headers

    res = requests.post('https://www.reddit.com/api/v1/access_token', auth = auth, data = data, headers = headers)

    return res