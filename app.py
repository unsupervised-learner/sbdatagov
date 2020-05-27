from flask import Flask, render_template
import pandas as pd



app = Flask(__name__)

systems = [
    {
        'name':'Vernon',
        'surname':'Kok',
        'occupation':'Graduate Trainee'
    },
    
    {
        'name':'Algor',
        'surname':'Ithms',
        'occupation':'Researcher'
    }
]

#Landing page
@app.route('/')
def HomePage():
	return( render_template('HomePage.html', systems=systems) )


#about page
@app.route('/adding_procs')
def adding_procs():
	df = pd.read_csv('./proc_db.csv')
    	#render
	return render_template('adding_procs.html', systems=df.iloc[0:, 0]) 

@app.route('/viewing_procs')
def viewing_procs():
	return render_template('viewing_procs.html')

