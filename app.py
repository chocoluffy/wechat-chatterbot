# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from flask.ext.api import FlaskAPI
from flask import request, current_app, abort, jsonify
import json

### using mongolab uri.
chatbot = ChatBot(
    'Luffy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter"
    ],
    database='chattbot',
    database_uri='mongodb://adatech:adaseikou@ds019916.mlab.com:19916/chattbot'
)

d = json.loads(open('conversation_unicode.json').read()) # a better way to load json file data.

# chatbot.train("chatterbot.corpus.chinese")
app = FlaskAPI(__name__)

@app.route('/chat', methods=['POST'])
def chat():
	token = request.data.get('auth')
	if token == 'yushunzhe':
		query = request.data.get('query')
		if query in d.keys():
			return {"response": d[query]}	
		else:
			return {"response": str(chatbot.get_response(query))}
	else:
		return {"response": "wrong password."}

if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
