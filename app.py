from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_now = now
    current_month = now.strftime("%B")
    return render_template("index.html", now=current_now, year=current_year, month=current_month, day=current_day)
