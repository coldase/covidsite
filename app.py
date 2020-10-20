from flask import Flask, render_template, redirect, request
from funks import *

app = Flask(__name__)

covid_data = {}

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		try:
			country = request.form["country"]
			if country.lower() in get_country():
				covid_data.update(get_data(country))
				return redirect("/")
			else:
				return redirect("/")
		except:
			return redirect("/")
	return render_template("index.html", data=covid_data)

if __name__ == "__main__":
	app.run(debug=True)