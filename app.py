import os
import io
import time
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = b'bb,hjd87li7fiopsddfrgt5'

@app.route("/")
def index():
    return render_template('selection.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000) 