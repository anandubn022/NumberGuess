from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

random_num = random.getrandbits(16) # random 16 bit number

@app.route("/guess", methods = ["POST"])
def number_guess():
    global random_num
    user_input = request.get_json()
    user_guess = int(user_input.get("userGuess"))
    upper_limit = int(user_input.get("upperLimit"))

    if user_guess == random_num:
        return jsonify({"message":"The number was guessed", "ul": upper_limit})
    else:
        if user_guess > random_num:
            return jsonify({"message":"The number is smaller", "ul": upper_limit})
        else:
            return jsonify({"message":"The number is larger", "ul": upper_limit})

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)