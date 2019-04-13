from flask import Flask
from flask_jsonrpc import JSONRPC
from app import config
from flask_oauth import OAuth
from flask_sqlalchemy import SQLAlchemy
import boto3

app = Flask(__name__)

jsonrpc = JSONRPC(app, '/api/')

app.secret_key = 'oXFBpEnJMlFWX5jNQ9Yp'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/messenger'

db = SQLAlchemy(app)

s3_session = boto3.session.Session()
s3_client = s3_session.client( service_name='s3',\
                               endpoint_url=config.S3_ENDPOINT_URL,\
                               aws_access_key_id=config.S3_ACCESS_ID,\
                               aws_secret_access_key=config.S3_SECRET_KEY  )

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
