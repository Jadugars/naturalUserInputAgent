from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json
from sutime import SUTime

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        text = str(request.json["text"])
        sutime = SUTime(mark_time_ranges=True, include_range=True)
        return jsonify(sutime.parse(text))


@app.route("/")
def index():
    test = ["I have an English class at 10am tomorrow", 
        "I have a AI class 8pm on Thursday", 
        "I have PL lectures from 8am to 12am the day after tomorrow"]

    sutime = SUTime(mark_time_ranges=True, include_range=True)

    for i in range(3):
        print(sutime.parse(test[i]))
    
    return "Hello World"
