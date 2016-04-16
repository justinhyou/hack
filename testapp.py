from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/echo/<id>")
def echo(id):
	if id > 5:
		return "ID is greater than 5"
	return id
if __name__ == "__main__":
	app.run()
