import flask
from flask import render_template, session, jsonify
from flask import Flask


app = Flask("__My-AI__")
app.secret_key = 'la_cle'

from flask_session import Session

app.config['SESSION_TYPE'] = 'filesystem'  # You can choose other storage options
Session(app)


@app.route("/")
def menu():
	return render_template('index.html')

from flask import request
from ask_question_to_pdf import *

question= ""

@app.post('/historic')
@app.get('/historic')
def historic():
	if 'past_messages' in session:
		return jsonify({"historic" : session["past_messages"]})
	else:
		return {"historic" : []}

def add_ai_message(message):
	if not "past_messages" in session:
			session["past_messages"] = []
	session["past_messages"].append([message, 1])

def add_human_message(message):
	if not "past_messages" in session:
		session["past_messages"] = []
	session["past_messages"].append([message, 0])


@app.post("/prompt")
def reponse_AI():
		add_human_message(request.form['prompt'])
		answer = ask_question_to_pdf(request.form['prompt'])
		add_ai_message(answer)

		return {"answer": answer}


@app.get("/question")
def question_AI():
	question = ask_question_to_pdf("Poses une question pour vérifier les connaissances sur le texte suivant:")
	add_ai_message(question)
	return {"answer": question}


@app.post("/answer")
def test_AI():
	add_human_message(request.form['prompt'])
	res = ask_question_to_pdf("La réponse donnée: \n"+request.form['prompt'] +"\n est elle vraie ou fausse? pour la question "+request.form['question'])
	add_ai_message(res)
	return {"answer":res}




#res = ask_question_to_pdf("la réponse donnée: \n"+request.form['prompt'] +"\n est elle vraie ou fausse?")
		#return {"answer":res}