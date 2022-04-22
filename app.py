from flask import Flask, redirect, render_template, request
from owla import owla_connector as oc

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)