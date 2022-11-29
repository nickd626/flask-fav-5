from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    favFiveEaglesPlayers = ['Jalen Hurts', 'Jason Kelce', 'Darius Slay', 'Fletcher Cox', 'DeVonta Smith']
    return render_template('index.html', players=favFiveEaglesPlayers)