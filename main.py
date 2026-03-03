from flask import Flask, request, render_template
import random

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        return {"status": random.randint(1, 100)}
    else:
        return render_template("metode.html")


app.run(debug = True)

