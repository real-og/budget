from flask import Flask, render_template, request
from db import *

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        amount = request.form['amount']
        cat = request.form['cat']
        date = request.form['date']
        if is_digit(amount):
            add_expense(cat, date, amount)
    expenses = get_data()
    return render_template('page.html',
                           exps=expenses,
                           data={'Task' : 'Hours per Day'} | get_data_by_cat()
                           )

@app.route("/<month>")
def show_by_month(month):
    data = {'Task' : 'Hours per Day'} | get_data_by_cat(int(month))
    return render_template('by_month.html', data = data, month=month)

if __name__ == "__main__":
    app.run(debug=True)