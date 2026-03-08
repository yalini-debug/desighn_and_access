from flask import Flask, render_template, request
import sqlite3
from risk_engine import calculate_risk
from policy_engine import access_decision

app = Flask(__name__)

def check_user(username,password):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
    user = cursor.fetchone()

    conn.close()

    return user

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        device = request.form["device"]
        location = request.form["location"]
        app_risk = request.form["app_risk"]

        user = check_user(username,password)

        if user:

            role = user[3]

            score = calculate_risk(role,device,location,app_risk)

            decision = access_decision(score)

            return render_template("dashboard.html",
                                   username=username,
                                   role=role,
                                   risk_score=score,
                                   decision=decision)

        else:
            return "Invalid Login"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)