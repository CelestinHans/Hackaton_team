import flask
from flask import render_template
from flask import Flask


app = Flask("__My-AI__")

@app.route("/")
def menu():
	return render_template('index.html')

from flask import request
from ask_question_to_pdf import *

question= ""

@app.post("/prompt")
#def mm_reponse():
	#return {"answer":request.form['prompt']}
def reponse_AI():
		return {"answer":ask_question_to_pdf(request.form['prompt'])}

@app.get("/question")
def question_AI():
	question = ask_question_to_pdf("pose une question pour vérifier les connaissances sur le texte suivant:")
	return {"answer": question}

@app.post("/answer")
def test_AI():
	res = ask_question_to_pdf("la réponse donnée: \n"+request.form['prompt'] +"\n est elle vraie ou fausse? pour la question"+request.form['question'])
	return {"answer":res}




#res = ask_question_to_pdf("la réponse donnée: \n"+request.form['prompt'] +"\n est elle vraie ou fausse?")
		#return {"answer":res}