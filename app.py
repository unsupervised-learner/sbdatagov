from flask import Flask, render_template, request, redirect, url_for
import pandas as pd



app = Flask(__name__)


#Landing page
@app.route('/')
def HomePage():
	return( render_template('HomePage.html') )


#about page
@app.route('/adding_procs', methods=['POST', 'GET'])
def adding_procs():
	df = pd.read_csv('./proc_db.csv')
    	#render
	return render_template('adding_procs.html', systems=df.iloc[0:, 0]) 

#viewing proocesses
@app.route('/viewing_procs', methods=['POST', 'GET'])
def viewing_procs():
	df = pd.read_csv('./proc_db.csv')

	if request.method == 'POST':
		proc_to_view = request.form['system_selected']
		return( redirect(url_for('proc_view', process_to_view = proc_to_view)) )
	else:			
		return render_template('viewing_procs.html', systems=df.iloc[0:, 0])

@app.route('/<process_to_view>')
def proc_view(process_to_view):
	return( render_template('proc_view.html', process_to_view=process_to_view) ) 



if __name__ == '__main__':
	app.run(debug=True)