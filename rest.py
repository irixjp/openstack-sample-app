#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Flask, jsonify, request

import model
from db import db

app = Flask(__name__)

@app.route('/bbs', methods=['GET'])
def get_content():
    data = {}
    for i in model.get_content_all():
        data[i.id] = {'timestamp': i.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                      'text': i.text.encode('utf-8')}

    response = jsonify(data)
    response.status_code = 200
    db.session.close()
    return response

@app.route('/bbs', methods=['POST'])
def add_content():
    ret = json.loads(request.data)
    model.add_content(ret['text'])
    response = jsonify(ret)
    response.status_code = 201
    db.session.close()
    return response


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=5555, debug=True)

