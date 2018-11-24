import datetime
import json


def application(env, start_response):
    data = {'time': str(datetime.datetime.now()), 'url': env['SERVER_NAME'] + ':' + env['SERVER_PORT'] + env['RAW_URI']}
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [bytes(json.dumps(data), 'utf-8')]