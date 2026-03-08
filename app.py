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
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    randomRank = random.choice(ranks)
    randomSuit = random.choice(suits)
    return render_template("card.html", rank=randomRank, suit=randomSuit)

@app.route('/8ball')
def eightball():
    eightBall = random.randint(1,10)
    eightResult = eightBall
    return render_template("eightball.html", result=eightResult)

@app.route('/gamerecs')
def gamerecs():
    mobas = ["League of Legends", "DOTA 2", "SMITE"]
    fps = ["Counter Strike 2", "Valorant", "Destiny 2"]
    rpgs = ["Skyrim", "Witcher 3", "Elden Ring"]
    horror = ["Resident Evil RE", "Amnesia The Dark Descent"]
    
    randomMobas = random.choice(mobas)
    randomFPS = random.choice(fps)
    randomRPG = random.choice(rpgs)
    randomHorror = random.choice(horror)

    return render_template("gamerecs.html", mobarec = randomMobas, fpsrec = randomFPS, rpgrec = randomRPG, horrorrec = randomHorror)