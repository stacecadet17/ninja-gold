from flask import Flask, session, redirect, request, render_template
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'earnings' not in session:
        session['earnings'] = 0
    if 'activities' not in session:
        session['activities'] = ""
    return render_template('index.html')

@app.route('/process_money', methods= ['POST'])
def process():
    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        session['earnings'] += gold
        newactivity = "You found gold!"
        session['activities'] = session['activities'] + newactivity
        print newactivity
        print gold
    elif request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        session['earnings'] += gold
        newactivity = "You found gold!"
        session['activities'] = session['activities'] + newactivity
        print newactivity
        print gold
    elif request.form['building'] == 'house':
        gold = random.randrange(2, 6)
        session['earnings'] += gold
        newactivity = "You found gold!"
        session['activities'] = session['activities'] + newactivity
        print newactivity
        print gold
    else:
        gold = random.randrange(-50, 51)
        if gold < -1:
            session['earnings'] -= abs(gold)
            newactivity = "You lost gold :("
            session['activities'] = session['activities'] + newactivity
            print newactivity
            print gold
        else:
            session['earnings'] += gold
            newactivity = "winner winner chicken dinner"
            session['activities'] = session['activities'] + newactivity
            print newactivity
            print gold
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()

    return redirect('/')

app.run(debug = True)
