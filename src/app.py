from flask import Flask
from flask_s3 import FlaskS3
app = Flask(__name__)
app.config['hkowrada'] = 'mybucketname'
s3 = FlaskS3(app)

