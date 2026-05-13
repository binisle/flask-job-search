# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT
