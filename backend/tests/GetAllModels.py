import requests
import json
from GetAuthToken import get_access_token


def get_all_models():
    url = 'http://127.0.0.1:5000/api/get-all/models'

    with open('token.json', 'r') as file:
        access_token = json.load(file).get('access_token')
    headers = { 'Authorization': f'Bearer {access_token}' }

    return requests.get(url, headers=headers)

response = get_all_models()

if response.status_code == 200:
    print('Accessing model Details successful!')
    data = response.json()
    print(data)
elif response.status_code == 401:
    if get_access_token():
        response = get_all_models()
        if response.status_code == 200:
            print('Accessing model Details successful!')
            data = response.json()
            print(data)
        else:
            print('GET request failed with status code:', response.status_code)
    else:
        print("Invalid username or password")
else:
    print('GET request failed with status code:', response.status_code)