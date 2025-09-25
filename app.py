from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_now = now
    current_month = now.strftime("%B")
    return render_template("index.html", now=current_now, year=current_year, month=current_month, day=current_day)


@app.route('/card')
def card():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    randomRank = random.choice(ranks)
    randomSuit = random.choice(suits)
    return render_template("card.html", rank=randomRank, suit=randomSuit)
