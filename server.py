from flask_jsonrpc.proxy import ServiceProxy
import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://localhost:5000/api/'


"""
    In this case there is inly one user with hardcoded 
    user_id = 596b924c-4755-4e4b-a6ef-fcd6403ee552
    chat_id = 596b924c-4755-4e4b-a6ef-fcd6403ee551
    member_id = 596b924c-4755-4e4b-a6ef-fcd6403ee550
    message_id = 596b924c-4755-4e4b-a6ef-fcd6403ee549
"""


if __name__ == '__main__':
    server = ServiceProxy(url)

    payload = {
        'method': 'api.get_messages',
        'params': [
            {
                'user_id': '596b924c-4755-4e4b-a6ef-fcd6403ee552'
            }
        ],
        'id': 1
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.content)
