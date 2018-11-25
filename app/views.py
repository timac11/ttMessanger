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
    :params: object which contains 
        userId - uuid string
"""


@jsonrpc.method('api.get_messages')
def get_messages(params):
    if params is None or params['user_id'] is None:
        return {
            'error': 'user not found'
        }
    user_id = params.get('user_id')
    result = model.get_messages_by_user_id(user_id)
    return result


"""
    :params: object which contains 
        user_id - uuid string
        chat_id - uuid string
        content - string
        attachment - object 
"""


@jsonrpc.method('api.create_message')
def create_message(params):
    print(params)
    return model.create_message(
        params.get('user_id'),
        params.get('chat_id'),
        params.get('content'),
        params.get('attachment')
    )


"""
    param: object which contains
        message_id
"""


@jsonrpc.method('api.read_messages')
def read_messages(params):
    None
