import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
application = app # this is for Passenger, which expects application

# I was running into encoding errors when using regular ol' open so I used io's
with io.open("netlibram.txt", 'r', encoding='utf8') as netlibram_source:
    netlibram = netlibram_source.readlines()
netlibram_total = len(netlibram)

# Most of the below is self explanatory for anyone familiar with Flask. I get
# a little funky in places, but for the most part it's all pretty human
# readable. I also use a touch of Jinja2 to make things look nicer since, by
# default, Flask sticks everything in <p> (I think???)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/netlibram")
def netlibram_start():
    r = int(random.randrange(0, len(netlibram) - 1, 1))
    return redirect("/netlibram/%d" % r, 303)

@app.route("/netlibram/<int:effectid>")
def netlibram_lookup(effectid):
    if effectid > netlibram_total:
        nl_max_exceeded = "The maximum effect for Net Libram is {:,}!".format(netlibram_total)
        return render_template('nlresult.html', result=nl_max_exceeded)
    elif effectid == 0:
        return render_template('dice_error.html')
    elif effectid < 0:
        return "How did you even get here?!"
    else:
        return render_template('nlresult.html', result=netlibram[effectid])

if __name__ == "__main__":
    app.run()