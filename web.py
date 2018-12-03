import io
import random
from flask import Flask, render_template, request

app = Flask(__name__)

with io.open("effects.txt", 'r', encoding='utf8') as effects_source:
    effects = effects_source.readlines()
effect_number = len(effects)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def index_post():
    range_error = "Please enter a number between 1 and %d!" % effect_number
    type_error = "Please enter an integer!"
    input_number = request.form["number"]
    
    # This is a bit sloppy but hey, it makes sure I'm only trying to use an integer
    if type(input_number) is int:
        if input_number > effect_number:
            return range_error
        elif input_number < 1:
            return range_error        
        else:
            return effects[input_number - 1]
    else:
        return type_error
        
# def return_effect():
#    r = random.randrange(0, len(effects) - 1, 1)
#    return effects[r]
 
if __name__ == "__main__":
    app.run()