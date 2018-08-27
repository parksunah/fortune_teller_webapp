from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from fortune_teller import home, show_fortune