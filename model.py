#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

from db import db

class Contents(db.Model):
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    text = db.Column(db.String(255))
    imageref = db.Column(db.String(255))

    def __init__(self, timestamp, text, imageref=""):
        self.timestamp = timestamp
        self.text = text
        self.imageref = imageref

    def __repr__(self):
        return '<Contents>(%s, %s, %s, %s)' % (self.id, self.timestamp, self.text.encode('utf_8'), self.imageref)


def get_content_all():
    return Contents.query.order_by(Contents.timestamp.desc()).all()

def add_content(text, imageref=""):
    db.session.add(Contents(datetime.datetime.now(), text, imageref))
    db.session.commit()

def del_content(id):
    db.session.delete(db.session.query(Contents).get(id))
    db.session.commit()
