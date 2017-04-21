from flask import Flask, jsonify, request
import os
import requests
from pprint import pprint
import json
import logging
import logstash

#added this K
#from cfenv import AppEnv

#added this K
#env = AppEnv()
#env.LOG_HOST  # 'test-app'
#env.LOG_PORT  # 5000

if 'LOG_HOST' not in os.environ or 'LOG_PORT' not in os.environ:
    raise(Exception("LOG_HOST OR LOG_PORT NOT DEFINED"))

POST_URL = "http://{host}:{port}/log".format(host=os.environ['LOG_HOST'],port=os.environ['LOG_PORT'])

host = os.environ['LOG_HOST']

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))

app = Flask(__name__)

def log_request(req):
    extra = {
        'ip': request.environ.get('X-Forwarded-For', request.remote_addr),
        'url': req.full_path,
    }
    test_logger.info('honeypot: ', extra=extra)

#data to log

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def honey(path):
    log_request(request)
    return jsonify({'CF result': 'ok'})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)



