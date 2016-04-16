import os

from flask import render_template, request
from yelpapi import YelpAPI

from chirp import app

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather/")
def getWeather():
	return render_template("weather.html", locn="Claremont")

@app.route("/search/")
def search():
	entry = request.args.get("major")
	if (entry == "math"):
		return render_template("math.html")
	if (entry == "neuro"):
		return render_template("math.html")
	return request.args.get("major")

# @app.route("/testapp/")
# def testing():
#     if __name__ == '__main__':
#     	app.run(debug=true)