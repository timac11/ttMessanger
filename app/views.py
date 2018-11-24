from app import app, jsonrpc, model
from flask import request, abort, jsonify

import json


@app.route("/<string:name>/")
@app.route("/")
def index(name='World'):
    return 'Hello {}!'.format(name)


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return '''<html><head></head><body>
        <form method="POST" actions="/form/">
            <input name="first_name">
            <input name="last_name">
            <input type="submit">
        </form></body></html>
        '''
    else:
        response = jsonify( request.form )
        return response


"""
    :param: object which contains userId
"""


@jsonrpc.method('api.get_messages')
def get_messages(params):
    data = json.loads(request.data)
    print(data)
    if params is None or params['user_id'] is None:
        return {
            'error': 'user not found'
        }
    user_id = params['user_id']
    return model.get_messages_by_user_id(user_id)


@jsonrpc.method('api.send_message')
def send_message():
    return None


@jsonrpc.method('api.read_messages')
def read_messages():
    return None



