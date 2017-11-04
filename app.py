#!/usr/bin/python3

from flask import Flask, render_template, request, json
from random import shuffle
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/generate", methods=['POST'])
def generate():
    _participants = request.form['participants']
    if _participants:
        players = _participants.split()
        pairs = []
        for index, player in enumerate(players):
            remainder = players[index + 1:]
            if not remainder:
                break
            else:
                for opponent in remainder:
                    pairs.append((player, opponent))
        print(pairs)
        shuffle(pairs)
        print(pairs)
        return json.dumps({'message': pairs})
    else:
        return json.dumps({'error': 'You need at least 3 participants for this to be any fun!!'})

if __name__ == "__main__":
    app.run()
