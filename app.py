from flask import Flask, render_template, request
from calculations import calculate_npv, calculate_payback_period

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    initial_investment = float(request.form["initial_investment"])
    cash_flows = list(map(float, request.form["cash_flows"].split(",")))
    discount_rate = float(request.form["discount_rate"]) / 100

    npv = calculate_npv(initial_investment, cash_flows, discount_rate)
    payback_period = calculate_payback_period(initial_investment, cash_flows)

    return render_template("results.html", npv=npv, payback_period=payback_period)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")
