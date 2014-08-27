#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('db-server', 'db_endpoint')
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
db = SQLAlchemy(app)
