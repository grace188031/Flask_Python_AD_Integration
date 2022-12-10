from flask import Flask, redirect, request, render_template
from model import authenticate


app = Flask(__name__)
server_uri = "ldap://192.168.68.132"
domain = "gracepractice.com"

@app.route("/", methods=['POST', 'GET'])
def login():
    context = {}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            authenticate(server_uri, domain, username, password)
            return redirect("/loggedin")
        except ValueError as err:
            context["error"] = f'{err}.message'

    return render_template("login.html", **context)


@app.route("/loggedin")
def loggedin():
    return "Successfully logged in!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port="4099")
    app.run()