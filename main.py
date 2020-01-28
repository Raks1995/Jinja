from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Hello, it's me."
    time = datetime.datetime.now()
    cities = ["Zagreb", "Madrid", "Vienna", "Beograd"]
    return render_template("index.html", some_text=some_text, time=time, cities=cities)


@app.route("/about-me")
def about():
    return render_template("about-me.html")


if __name__ == '__main__':
    app.run()
