#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask, request, url_for, render_template, redirect
from flask_wtf import Form

from werkzeug import secure_filename

from wtforms import TextField, FileField
from wtforms.validators import Required

from restclient import SimpleRestClient
from swift import SwiftUploader

from uuid import uuid4

from config import config

app = Flask(__name__)

class TextForm(Form):
    text = TextField('Please write something and hit enter', validators=[Required()])

class PhotoForm(Form):
    upload = FileField('', validators=[Required()])

@app.route('/', methods=('GET', 'POST'))
def index():
    form = TextForm(csrf_enabled=False)
    photo = PhotoForm(csrf_enabled=False)
    client = SimpleRestClient()

    if request.method == 'POST' and form.validate() and photo.validate_on_submit():
        filename = uuid4().hex + "-" + secure_filename(photo.upload.data.filename)
        path = config.get('swift', 'upload_path') + filename

        photo.upload.data.save(path)
        s = SwiftUploader()
        imageref = s.upload_image(filename, path)
        os.remove(path)

        client.post_content(form.text.data, imageref)
        return redirect(url_for('index'))
    else:
        contents = client.get_contents()
        return render_template('web.html',
                               TITLE='bbs',
                               FORM=form,
                               PHOTO=photo,
                               CONTENTS=sorted(contents.items(), key=lambda x: int(x[0]), reverse=True))


if __name__ == '__main__':
    s = SwiftUploader()
    s.initialize_container()
    app.run(host="0.0.0.0", port=80, debug=True)
