from flask_app import app
from flask import render_template, redirect, request
from flask_app import solver 


@app.route('/new-sudoku')
def home():
        return render_template('newSudoku.html')

@app.route ('/solve-sudoku', methods=['POST'])
def new_sudoku():
        if solver.solve_one(request.form):
                return redirect('/results')

@app.route('/results')
def solved_sudoku():
        results = solver.solve_one
        return render_template('results.html', results=results)