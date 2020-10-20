from scrapper import get_jobs
from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    jobs = None
    word = request.args.get("word")
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNum=len(jobs))

# @app.route("/<username>")
# def contact(username):
#   return f"Hello your username is: {username}"


app.run(host="192.168.0.7")
