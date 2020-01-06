from flask import Flask
from flask import render_template
from flask import request, url_for, redirect
from flask import jsonify
import requests
import json
import io

import random
import string

import datetime 

app = Flask(__name__)

user = "ex@gmail.com"

# # ERROR resource not found page
# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('serviceOfflineTemplate.html', type="found", services = microservices, login = user, key = key)


@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='favicon.ico'), code=302)

############ HTML #############
@app.route('/')
def homePage():
	return render_template("homepage.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	global user
	if request.method == 'POST':
		if "user" in request.form:
			user = request.form["user"]
			return render_template("login.html", user = user)
	if request.method == 'GET':
		if request.args.get("email") != None and request.args.get("pass") != None:
			print("ENTER")
			return redirect(url_for('Dashboard'))
	return redirect(url_for('homePage'), code=302)

@app.route('/dashboard')
def Dashboard():
	return render_template("dashboard.html", active = "dashboard", content=render_template("dashExample.html"))

@app.route('/dashboard/sell')
def DashboardSell():
	global user
	return render_template("dashboard.html", active = "sell", content=render_template("sell.html", user = user))

@app.route('/sell', methods=['POST'])
def Sell():
	return render_template("dashboard.html", active = "sell", content=render_template("generate.html", user = user))


@app.route('/dashboard/buy')
def DashboardBuy():
	return render_template("dashboard.html", active = "buy", content=render_template("buy.html"))


@app.route('/buy/<secret>', methods=['GET'])
def Buy(secret):
	return render_template("dashboard.html", active = "buy", content=render_template("buy.html"))

if __name__ == '__main__':
	app.run(debug=True, port=45000)