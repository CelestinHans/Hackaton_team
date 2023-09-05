import flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import Flask
from ask_question_to_pdf import *


app = Flask("myapp")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.post("/prompt")
def retour():
    return {"answer": ask_question_to_pdf(request.form['prompt'])["choices"][0]["message"]["content"]}



