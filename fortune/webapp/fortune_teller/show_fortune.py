import random


from flask import render_template, request
from fortune_teller import app

@app.route('/fortune', methods=['POST'])
def show_fortune():
    name = request.form['username']
    with open('/Users/seijinjung/Desktop/fortunes.txt') as f:
        lines = f.readlines()
    return render_template('fortune.html', username=name, fortune_text = random.choice(lines))
