# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").lower()
    jobs = load_jobs()
    results = [
        job for job in jobs
        if keyword in job.get("title", "").lower()
        or keyword in job.get("company_name", "").lower()
        or keyword in job.get("description", "").lower()
    ]
    return render_template("search.html", keyword=keyword, results=results)

# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

# /BLUEPRINT
