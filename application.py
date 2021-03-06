from flask import render_template, request, redirect, url_for, flash
from app import application, db, engine
from app.data_model import team
from develop.prediction import prediction
import pandas as pd


@application.route('/')
def index():

	return render_template('index.html', teams = team.query.all())


@application.route('/result', methods = ['POST'])
def result():

	if request.method == 'POST' and request.form['mainbutton'] == 'submitted':
		home = request.form.get('hometeam')
		away = request.form.get('awayteam')
		
		stats = pd.read_sql_query("select * from stats;", engine)
		result = prediction(home, away, stats)

		return render_template('result.html', result = result, home = home, away = away)
	
	else:
		return redirect(url_for('index'))

if __name__ == "__main__":
	application.run(host = '0.0.0.0', debug = True)