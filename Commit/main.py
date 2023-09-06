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
    # return {"answer": ask_question_to_pdf("la réponse à la question :" + quest + request.form['prompt'] + "est-elle correcte ? Explique pourquoi")["choices"][0]["message"]["content"]}
    return {"answer":"test"}

@app.get("/question")
def question():
    quest=ask_question_to_pdf("Propose une question pour vérifier que j'ai bien compris le texte suivant :" )["choices"][0]["message"]["content"]
    return {"answer": quest }


@app.post("/answer")
def retour():
    return {"answer": ask_question_to_pdf("la réponse à la question :" + quest + request.form['answer'] + "est-elle correcte ? Explique pourquoi")["choices"][0]["message"]["content"]}