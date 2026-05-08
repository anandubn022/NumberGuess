from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

limit = 65536
random_num = random.randint(0, limit)

@app.route('/limit', methods = ["POST"])
def set_limit_gen_random():
    user_input = request.get_json()
    global limit, random_num
    limit_check = user_input.get("upperLimit")
    if limit_check:
        limit = int(user_input.get("upperLimit"))
    else:
        limit = 65536
    random_num = random.randint(0, limit)
    return jsonify({"ul": f"Current randomiser limit is {limit}."})

@app.route("/guess", methods = ["POST"])
def number_guess():
    global random_num
    user_input = request.get_json()
    user_guess = int(user_input.get("userGuess"))

    if user_guess == random_num:
        return jsonify({"message":"The number was guessed."})
    else:
        if user_guess > random_num:
            return jsonify({"message":"The number is smaller."})
        else:
            return jsonify({"message":"The number is larger."})

@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)