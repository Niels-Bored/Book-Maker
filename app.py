import os
from bookmaker.BookMaker import generatePDF 
from flask import Flask, send_file, request
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

@app.route("/getbook/")
def getbook():
    child_name = request.args.get("child_name")
    child_fullname = request.args.get("child_fullname")
    date = request.args.get("date")
    dedication = request.args.get("dedication")

    generatePDF(child_name, child_fullname, date, dedication)

    file_path = os.path.join(STATIC_FOLDER, f"{child_name}.pdf")

    return send_file(file_path)

if __name__ == "__main__":
    app.run(debug=True, port=3000) 