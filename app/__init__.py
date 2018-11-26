from flask import Flask
from flask_jsonrpc import JSONRPC
from app import config
from flask_oauth import OAuth

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api/')

oauth = OAuth()

vk = oauth.remote_app('vk',
                      base_url='https://api.vk.com/method/',
                      request_token_url=None,
                      access_token_url='https://oauth.vk.com/access_token',
                      authorize_url='https://oauth.vk.com/authorize',
                      consumer_key=config.VK_APP_ID,
                      consumer_secret=config.VK_APP_SECRET,
                      request_token_params={'scope': 'email'})

from .views import *
