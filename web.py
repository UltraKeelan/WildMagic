import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
application = app # this is for Passenger, which expects application

# This will import any newline-delimited effects files passed to it as a text file
def import_effects(effectlist):
    # I was running into encoding errors when using regular ol' open so I used io's
    with io.open(effectlist, 'r', encoding='utf8') as effects:
        return effects.readlines()

nlsource = "nltable.txt"
wmsource = "wmtable.txt"

nl = import_effects(nlsource)
wm = import_effects(wmsource)

# Checks validity of inputs, and then returns a rendered template
# (or possibly a string)
def effect_lookup(table, tablename, id):
    tablelength = len(table)
    id -= 1
    if id >= tablelength:
        # If you know of a better way to do this string, please
        # for the love of god submit a pull request
        return ("The maximum length for the %s table is {:,}!".format(tablelength) % tablename)
    elif id == -1:
        # This will happen if they pass a 0
        # Grrrr this will break things I think...
        return "That's not how dice work!"
    elif id < -1:
        # I haven't figured out if this is possible, but there may
        # be a way for 
        return "How did you even get here?"
    else:
        return table[id]

# Most of the below is self explanatory for anyone familiar with Flask. I get
# a little funky in places, but for the most part it's all pretty human
# readable. I also use a touch of Jinja2 to make things look nicer since, by
# default, Flask sticks everything in <p> (I think???)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/netlibram/")
def netlibram_start():
    r = int(random.randrange(1, len(nl), 1))
    return redirect("/netlibram/%d" % r, 303)

@app.route("/netlibram/<int:effectid>")
def netlibram_lookup(effectid):
    result = effect_lookup(nl, "Net Libram", effectid)
    return render_template('nlresult.html', result=result, resultnum=effectid)

@app.route("/wildmagic/")
def wm_start():
    r = int(random.randrange(1, len(nl), 1))
    return redirect("/wildmagic/%d" % r, 303)

@app.route("/wildmagic/<int:effectid>")
def wm_lookup(effectid):
    result = effect_lookup(wm, "Wild Magic", effectid)
    return render_template('wmresult.html', result=result, resultnum=effectid)

if __name__ == "__main__":
    app.run()