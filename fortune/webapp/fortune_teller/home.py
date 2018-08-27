from flask import render_template
from fortune_teller import app, forms

@app.route('/')
def home():
    form = forms.NameForm()

    # The following two lines are for understanding forms, and are not used
    # for the web app.
    print(form.username())
    print(form.submit())

    return render_template('home.html', form=form)