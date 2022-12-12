import os
from flask import Flask, render_template, request, flash, redirect, url_for
from db import *





app = Flask(__name__)

@app.route("/")
def index():
    expenses = get_data()
    return render_template('page.html', exps=expenses)

if __name__ == "__main__":
    app.run(debug=True)