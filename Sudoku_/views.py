"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from Sudoku_ import app
from Sudoku_ import Solve
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Sudoku')
def Sudoku():
    output = dict()
    output["c00"] = 0
    return render_template(
        'sudoku.html',
        title='Sudoku',
        year=datetime.now().year,
        output = output
    )

@app.route('/sudokuDetails', methods = ["POST"])
def SudokuDetails():
    
    x = list()
    details = dict(request.form)
    for i in details.values():
        if i:
            x.append(int(i))
        else:
            x.append(0)
    sol = Solve.solve(x)
    if(sol == 0):
        error = "No solution possible"
        return render_template(
            'sudoku.html',
            title='result',
            year=datetime.now().year,
            error = error
        )

    time = sol[0]
    result = sol[1]
    
    return render_template(
            'sudoku.html',
            title='result',
            year=datetime.now().year,
            output = result,
            time = time
        )

@app.route('/test')
def test():
    output = dict()
    #output["c00"] = 1
    #output["c01"] = 2
    #output["c02"] = 3
    return render_template(
            'sudoku.html',
            title='result',
            year=datetime.now().year,
            output = output
        )
