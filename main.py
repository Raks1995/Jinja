from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Hello, it's me."
    time = datetime.datetime.now()
    ucenici = ["Ivan", "Josip", "Marko", "Ante"]
    cities = ["Zagreb", "Madrid", "Vienna", "Beograd"]
    prosjeci = ["4.0", "3.4", "4.3", "2.2"]
    return render_template("index.html", some_text=some_text, time=time, cities=cities, ucenici=ucenici, prosjeci=prosjeci)


@app.route("/about-me")
def about():
    return render_template("about-me.html")


if __name__ == '__main__':
    app.run()
