from flask import render_template
from fortune_teller import app, forms

@app.route('/')
def home():
    form = forms.NameForm()
    return render_template('home.html', form=form)