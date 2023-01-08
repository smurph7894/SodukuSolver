from flask_app import app
from flask import render_template, redirect, request, session
from flask_app import solver 


@app.route('/new-sudoku')
def home():
        return render_template('newSudoku.html')

@app.route ('/solve-sudoku', methods=['POST'])
def new_sudoku():
        print(request.form)
        data = solver.chooseSolveLevel(request.form)
        if data:
                session['results'] = data
                return redirect('/results')
        
@app.route('/results')
def solved_sudoku():
        results = session["results"]
        session["results"] = None
        return render_template('results.html', results=results)
