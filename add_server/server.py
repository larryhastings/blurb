#!/usr/bin/env python3

from flask import Flask, request, render_template
import hashlib
import time

app = Flask(__name__)

def sortable_time():
    return time.strftime("%Y.%m.%d.%H.%M.%S", time.gmtime())

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
	section = request.form['section']
	text = request.form['text']
	whatsnew = request.form['whatsnew']

	filename = "Misc/NEWS.d/next/" + ".".join([
        section,
        sortable_time(),
        hashlib.md5(text.encode("utf-8")).hexdigest(),
        whatsnew,
        "rst",
        ])

	return render_template("result.html", text=text, filename=filename)


if __name__ == "__main__":
    app.run()