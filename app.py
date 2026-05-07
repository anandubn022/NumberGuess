from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

random_num = random.getrandbits(16) # random 16 bit number

@app.route("/guess", methods = ["POST"])
def number_guess():
    global random_num
    user_input = request.get_json()
    user_guess = int(user_input.get("userGuess"))

    if user_guess == random_num:
        return jsonify({"message":"The number was guessed"})
    else:
        if user_guess > random_num:
            return jsonify({"message":"The number is smaller"})
        else:
            return jsonify({"message":"The number is larger"})

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)