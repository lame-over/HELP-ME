from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

#scoreboard = []

def bot_r():
    # бот
	choose = ['rock', 'paper', 'scisors', 'lizard', 'spock']
	return choose[random.randint(1,5)]

def game(bot, player_choice):
    winner = 'YOU LOSE! ;-;'
    # логика игры
    if player_choice == 'rock' and (bot == 'scisors' or bot == 'lizard'):
        winner = 'YOU WIN!'
    elif player_choice == 'paper' and (bot == 'rock' or bot == 'spock'):
        winner = 'YOU WIN!'
    elif player_choice == 'scisors' and (bot == 'paper' or bot == 'lizard'):
        winner = 'YOU WIN!'
    elif player_choice == 'lizard' and (bot == 'paper' or bot == 'spok'):
        winner = 'YOU WIN!'
    elif player_choice == 'spock' and (bot =='rock' or bot == 'scisors'):
        winner = 'YOU WIN!'
    elif player_choice == bot:
        winner = 'Draw!'
    
    return winner


@app.route("/")
def r():
    return render_template('index.html')

@app.route("/game")
def hello():        
    return render_template("start.html")

@app.route("/rules")
def rule():
    return render_template('rules1.html')

#@app.route('/game/<name>')
#def hell(name):
#    user_exist = False
#    for user in scoreboard:
#        user_exist = True
#        user['name'] == name
#       user['choose'] == None
#    if not user_exist:
#       scoreboard.append({"name": name, "choose": None})
#    
#    return render_template('list.html', scoreboard=scoreboard)

@app.route("/game/<choose>")
def end(choose):
    player_choice = choose.lower()
    bot = bot_r()
    winner = game(bot, player_choice)
    # Вывод попедителя
    return render_template("ending.html", users=["sublime text 3", "visual studio"], winner=winner, player_choice=player_choice, bot=bot)

if __name__ == "__main__":
    app.run()
