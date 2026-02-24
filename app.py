from flask import Flask
app= Flask(__name__)
@app.route("/")
def index():
	return"<h1>Leric Raju</h1><br><h2>Appid=2409308</h2>"
if __name__ =="__main__":
	app.run(host="0.0.0.0",port=5001,debug=True)