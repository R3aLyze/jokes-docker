from flask import Flask, jsonify, request
import random

app = Flask(__name__)

jokes = [
    "How do you make an egg-roll? You push it",
    "What would bears be without bees? Ears",
    "What do lawyers wear to court? Lawsuits",
    "How do robots eat pizza? One byte at a time",
    "What do sprinters eat before they race? Nothing. They fast",
    "What's Forrest Gump's password? 1forrest1",
    "What did the tomato say to the other tomato during the race? Ketchup",
    "What do sea monsters eat? Fish and ships",
    "What do you call a sad strawberry? A blue berry",
    "What kind of cheese isn't yours? Nacho cheese"
]

@app.route('/jokes')
def getJoke():
    num = int(request.args.get('num', 1))
    random_joke = random.sample(jokes, num)
    return jsonify({'Joke:': random_joke})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)