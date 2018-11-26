from flask_jsonrpc.proxy import ServiceProxy
import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://localhost:5000/api/'
server = ServiceProxy(url)


def execute_request(payload):
    return requests.post(url, data=json.dumps(payload), headers=headers)


def get_messages():
    return execute_request(create_payload(
        'api.get_messages',
        [{'user_id': '596b924c-4755-4e4b-a6ef-fcd6403ee552'}]
    ))


def send_message():
    return execute_request(create_payload(
        'api.create_message',
        [{
            'user_id': '596b924c-4755-4e4b-a6ef-fcd6403ee552',
            'chat_id': '596b924c-4755-4e4b-a6ef-fcd6403ee551',
            'content': 'Hello, world!'
        }]
    ))


def create_payload(method, params):
    return {
        'method': method,
        'params': params,
        'id': 1
    }


"""
    In this case there is inly one user with hardcoded 
    user_id = 596b924c-4755-4e4b-a6ef-fcd6403ee552
    chat_id = 596b924c-4755-4e4b-a6ef-fcd6403ee551
    member_id = 596b924c-4755-4e4b-a6ef-fcd6403ee550
    message_id = 596b924c-4755-4e4b-a6ef-fcd6403ee549
"""


if __name__ == '__main__':

    #send_message = send_message()

    get_messages = get_messages()

    print(get_messages.content)
