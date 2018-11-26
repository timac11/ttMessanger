from flask_jsonrpc.proxy import ServiceProxy
import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://localhost:5000/api/'
server = ServiceProxy(url)


def execute_request(payload):
    return requests.post(url, data=json.dumps(payload), headers=headers)


def get_messages(user_id):
    return execute_request(create_payload(
        'api.get_messages',
        [{'user_id': user_id}]
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


def get_chats_by_user_id():
    return  execute_request(create_payload(
        'api.get_user_chats',
        [{
            'user_id': '596b924c-4755-4e4b-a6ef-fcd6403ee552'
        }]
    ))

def create_payload(method, params):
    return {
        'method': method,
        'params': params,
        'id': 1
    }


"""
    In this case there is only one user with hardcoded 
    user_id = 596b924c-4755-4e4b-a6ef-fcd6403ee552
    chat_id = 596b924c-4755-4e4b-a6ef-fcd6403ee551
    member_id = 596b924c-4755-4e4b-a6ef-fcd6403ee550
    message_id = 596b924c-4755-4e4b-a6ef-fcd6403ee549
"""


if __name__ == '__main__':

    #send_message = send_message()

    #chats = get_chats_by_user_id()
    #get_messages1 = get_messages('596b924c-4755-4e4b-a6ef-fcd6403ee552')
    #get_messages2 = get_messages('596b924c-4755-4e4b-a6ef-fcd6403ee400')

    print(dict(None))
