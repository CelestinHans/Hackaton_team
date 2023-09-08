# Hackathon Ponts ENPC

## Install

- when opening VSCode, install the suggested extensions (Python, Black Formatter and Pylance)
- create your python environment `python3 -m venv .venv`
- copy the `.env.example` file to a `.env` file
- replace the `OPENAI_API_KEY` and `OPENAI_ORGANIZATION` env variables with the real values
- activate your environment with `  `
- download necessary data with `python -m nltk.downloader all`
- run the server with `flask --app main run --debug`

The server should answer on http://localhost:5000

You can deactivate the environment with `deactivate`.

## Adding librairies

if you need to use a new librairies, you can do it with pip
`pip install [library name]` or `pip3 install [library name]`

## Commandes Git Bash
cd "C:\\Users\\cmmcc\\Desktop\\Tp1et2"
python3 -m venv .venv
source .venv/Scripts/activate
export FLASK_APP=main.py
export FLASK_ENV=development
flask --app main run --debug
*python ask_question_to_pdf.py

#a faire à chaque nouvel environnement
pip install -r requirements.txt
python -m nltk.downloader all



*cat name_file: voir l interieur d un fichier
*ls: liste des fichiers
*pip install flask
*pip install openai
*cp .env.example .env
*cp: copie les variables d environnements de .env.example .env

*python ask_question_to_pdf.py  #lance le fichier sous python
*si pas d effet flask run: supprimer .venv et relancer