#!/usr/bin/python3
""" Flask web application """
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ funtion displays Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ funtion displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ funtion displays HBNB """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ funtion displays Python is cool """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """display “n is a number” only if n is an integer
       and / The default value of text is “is cool”"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_templates_n(n):
    """display “n is a number” only if n is an integer
       / display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display page only if x is an integer"""
    if n % 2 == 0:
        even = 'even'
    else:
        odd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           even=odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
