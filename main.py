from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Hello, it's me."
    time = datetime.datetime.now()
    ucenici = ["Ivan", "Josip", "Marko", "Ante"]
    cities = ["Zagreb", "Madrid", "Vienna", "Beograd"]
    prosjeci = ["4.0", "3.4", "4.3", "2.2"]
    return render_template("index.html", some_text=some_text, time=time, cities=cities, ucenici=ucenici,
                           prosjeci=prosjeci)


@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about-me.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_password = request.form.get("contact-password")

        print(contact_name)
        print(contact_email)
        print(contact_password)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response


if __name__ == '__main__':
    app.run()
