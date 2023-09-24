import os
import dotenv
import requests

dotenv.load_dotenv()
BASE_URL = os.environ.get('BASE_URL')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def get_bearer_token():
    #requests.post(f'{BASE_URL}/api/v1/auth/login', json={'email': EMAIL, 'password': PASSWORD}).json()
    response = requests.post(f'{BASE_URL}/auth/login', json={'email': EMAIL, 'password': PASSWORD})
    if response.status_code != 200:
        raise Exception('Unable to authenticate user')
    else:
        return response.json()['token']

def get_today_analytics():
    token = get_bearer_token()
    print(token)
    response = requests.get(f'{BASE_URL}/analytics/getDailyAnalytics', headers={'Authorization': token})
    if response.status_code != 200:
        raise Exception('Failed retrieving daily analytics: ' + response.json()['error'])
    else:
        return response.json()
