from flask import Flask, render_template, request, jsonify
from wordleguesser import getNextGuesses
import json
from collections import Counter
#from wordleguesser import guesser function

app = Flask(__name__)


@app.route("/")
def index():
    guesscnts = {5: 4715, 4: 4517, 6: 2708, 3: 1434, 7: 753, 8: 353, 9: 174, 10: 100, 2: 61, 11: 32, 12: 6, 1: 1, 13: 1}
    collapsed = Counter()
    for k, v in guesscnts.items():
        if k > 6:
            collapsed["6+"] += v
        else:
            collapsed[str(k)] = v

    return render_template("index.html", guesscnts=json.dumps(collapsed))


@app.route("/submit", methods=["POST"])

def submit():
    data = request.get_json()
    guess = data.get("guess")
    feedback = data.get("feedback")
    previousGuesses = data.get('previous')
    wordlist = data.get("wordlist")
    nextGuesses = getNextGuesses(guess, feedback, previousGuesses, wordlist)
    return jsonify({"nextGuesses": nextGuesses})

if __name__ == "__main__":
    app.run(debug=True)
