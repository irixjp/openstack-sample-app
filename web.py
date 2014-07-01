#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template, redirect
from flask_wtf import Form

from wtforms import TextField
from wtforms.validators import DataRequired

from restclient import SimpleRestClient

app = Flask(__name__)

class TextForm(Form):
    text = TextField('Please write something and hit enter', validators=[DataRequired()])


@app.route('/', methods=('GET', 'POST'))
def index():
    form = TextForm(csrf_enabled=False)
    client = SimpleRestClient()

    if request.method == 'POST' and form.validate():
        client.post_content(form.text.data)
        return redirect(url_for('index'))
    else:
        contents = client.get_contents()
        return render_template('web.html', 
                               TITLE='bbs', 
                               FORM=form, 
                               CONTENTS=sorted(contents.items(), key=lambda x: int(x[0]), reverse=True))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

