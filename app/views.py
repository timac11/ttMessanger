import time

from app import app, jsonrpc, model, vk, s3_client, config
from flask import request, abort, jsonify,redirect, url_for, session, make_response
import base64

import hmac
import hashlib


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


def auth_decorator(f):
    def wrapper(*args, **kwargs):
        token = request.cookies.get('oauth_token')
        session_token = get_vk_oauth_token()
        if token != session_token:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper


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


@jsonrpc.method('api.get_user_chats')
def get_user_chats(params):
    print(params)
    return model.get_chats_by_user_id(params.get('user_id'))


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


# TODO user id should be got from session
# TODO try catch
@jsonrpc.method('api.upload_file')
def upload_file(b64content, filename, user_id, chat_id, mime_type):
    content = base64.b64decode(b64content).decode('utf-8')
    s3_client.put_object(Bucket=config.S3_BUCKET_NAME, Key=filename, Body=content)
    message_id = model.create_message(user_id, chat_id, '')
    model.create_attachment(user_id, chat_id, message_id, mime_type, filename)
    return b64content


@jsonrpc.method('api.download_file')
def download_file(filename):
    response = s3_client.get_object(Bucket=config.S3_BUCKET_NAME, Key=filename)
    content = base64.b64decode(base64.b64encode(response.get('Body').read())).decode('utf-8')
    return content


@app.route('/api/base')
def base():
    return 'Hello, world'


def generate_key(key, message):
    key = bytes(key, 'utf8')
    message = bytes(message, 'utf8')

    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()
    return base64.b64encode(signature1)


@app.route('/api/file/<string:filename>')
def get_file(filename):
    response = make_response()

    now = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    string_to_sign = "GET\n\n\n\nx-amz-date:{}\n/{}/{}".format(now, config.S3_BUCKET_NAME, filename)
    signature = generate_key(config.S3_SECRET_KEY, string_to_sign).decode('utf8')
    print("String to sign: [{}], signature: [{}]".format(string_to_sign,\
                                                         signature))
    response.headers['Authorization'] = "AWS {}:{}".format(config.S3_ACCESS_ID, signature)
    response.headers['X-Amz-Date'] = now
    response.headers['Date'] = now
    response.headers['Host'] = "{}.hb.bizmrg.com".format(config.S3_BUCKET_NAME)
    response.headers['X-Accel-Redirect'] = "/s3/{}".format(filename)
    print(response.headers)
