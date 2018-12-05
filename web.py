import io
import random
from flask import Flask, render_template, request, redirect, url_for

# Braxton Spence, [03.12.18 23:13]
# make a function (essentially a template) taking a number and returning
# the page for that number. you can have @app.route('/') generate a
# random number in the range you're looking at and call the function
# with that number to generate the response body, and you can set up
# another route @app.route('/<int:effect_id>') that that calls the
# function with the effect_id from the url
# 
# The page just has to contain a link to yourhostname/ and if you want
# to tell it your roll you just go to yourhostname/0123
# 
# if you want to get fancier, you can have the thing you decorate with
# @app.route('/') instead generate a random effect id and then send a
# redirect (3xx) response that goes to that random number, which would
# cause that effect id to be present in your navigation history, so you
# could go back to it if needed later.

app = Flask(__name__)

with io.open("effects.txt", 'r', encoding='utf8') as effects_source:
    effects = effects_source.readlines()
totaleffects = len(effects)

# random generator, returns a string
def random_number():
    r = random.randrange(0, len(effects) - 1, 1)
    return r

@app.route("/")
def index():
    return render_template('index.html')

# For inputting a genuine roll
@app.route("/", methods=["POST"])
def index_post():
    rangeerror = "Please enter a number between 1 and %d!" % totaleffects
    typeerror = "Please enter an integer!"
    inputnumber = request.form["number"]
    
    # This is a bit sloppy but hey, it makes sure I'm only trying to use
    # an integer
    if type(inputnumber) is int:
        if inputnumber > totaleffects:
            return rangeerror
        elif inputnumber < 1:
            return rangeerror        
        else:
            return effects[inputnumber - 1]
    else:
        return typeerror

@app.route("/<int:effectid>")
def return_effect(effectid):
    return effects[effectid]

 
if __name__ == "__main__":
    app.run()