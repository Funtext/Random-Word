import json, os, string, random
from flask import Flask, Response, request, render_template
from flask_cors import cross_origin
from tinydb import TinyDB, Query
from random import randint

app = Flask(__name__)
app.secret_key = os.urandom(12)

words_json = json.loads( open('words.json', 'r').read() )
swear_json = json.loads( open('swear.json', 'r').read() )

@app.route('/')
def _index():
    return render_template('index.html')

@app.route('/word')
@cross_origin()
def _word():
        number = 1
        all_words = []
        for i in range(0, number):
            word = dictionary[randint(0, len(dictionary) - 1)]
            all_words.append(word)
        return Response(json.dumps(all_words), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
