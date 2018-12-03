from flask_jsonrpc.proxy import ServiceProxy
import requests
import json
import sys
import base64

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
    if len(sys.argv) != 2:
        print("Usage: {} filename".format(sys.argv[0]))
        sys.exit(1)
    filename = sys.argv[1]
    service = ServiceProxy('http://127.0.0.1:5000/api/')
    with open(filename, 'rb') as input_file:
        print(filename)
        content = input_file.read()
        b64_content = base64.b64encode(content).decode('utf-8')
        #print(b64_content)

        # response = service.api.upload_file( b64_content, filename )
        # print( "Response: {}".format( response ) )
        response = service.api.upload_file(b64_content, filename)
        print("Response: {}".format(response))
        # content = base64.b64decode( b64_content ).decode('utf8')
        # print( content )

    #send_message = send_message()

    #chats = get_chats_by_user_id()
    #get_messages1 = get_messages('596b924c-4755-4e4b-a6ef-fcd6403ee552')
    #get_messages2 = get_messages('596b924c-4755-4e4b-a6ef-fcd6403ee400')

    #print(dict(None))
