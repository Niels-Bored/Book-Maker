import os
from bookmaker.BookMaker import generatePDF 
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = b'bb,hjd87li7fiopsddfrgt5'

CURRENT_FOLDER = os.path.dirname(__file__)
STATIC_FOLDER = os.path.join(CURRENT_FOLDER, "static")

@app.route("/")
def index():
    return {"status": "running"}

@app.route("/form/", methods=["GET", "POST"])
def form():
    return render_template('form.html', error="")


@app.route("/getbook/")
def getbook():
    file_name = request.args.get("file_name")
    child_name = request.args.get("child_name")
    child_fullname = request.args.get("child_fullname")
    date = request.args.get("date")
    dedication = request.args.get("dedication")

    generatePDF(file_name, child_name, child_fullname, date, dedication)

    file_path = os.path.join(STATIC_FOLDER, f"{file_name}.pdf")

    return send_file(file_path)

if __name__ == "__main__":
    app.run(debug=True, port=3000) 
