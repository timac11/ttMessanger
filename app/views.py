from app import app, jsonrpc, model, vk
from flask import request, abort, jsonify,redirect, url_for, session

import json


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return vk.authorize(callback=url_for('vk_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized')
@vk.authorized_handler
def vk_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    access_token = resp['access_token']
    email = resp.get('email')
    session['oauth_token'] = (resp['access_token'], '')
    return "Email: {}".format( email )


@vk.tokengetter
def get_vk_oauth_token():
    return session.get('oauth_token')


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
