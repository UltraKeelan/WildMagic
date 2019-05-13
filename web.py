import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Passenger is expecting the app you're trying to run to be called "application"
# but I'm not sure if you can change Flask's assignment to just be "application"
application = app

# This will import any newline-delimited effects files passed to it as a text file
def import_effects(effect_list):
    # I was running into encoding errors when using regular ol' "open" so I
    # switched to the  io library
    with io.open(effect_list, "r", encoding="utf8") as effects:
        return effects.readlines()

# Paths for effects tables you'd like to import. I'm using relative paths but
# absolute paths should (might?) be fine too
nl_source = "nltable.txt"
wm_source = "wmtable.txt"

# Running the import function
nl = import_effects(nl_source)
wm = import_effects(wm_source)

# Checks validity of inputs, and then returns a rendered template
def effect_lookup(table, name, id):
    t_length = len(table)
    id -= 1
    if id >= t_length:
        return ("The maximum length for the {} table is {:,}!".format(name, t_length))
    elif id == -1:
        # This will happen if they pass a 0
        return "That's not how dice work!"
    elif id < -1:
        # I haven't figured out if this is possible, but there may be a way to
        # get here somehow
        return "How did you even get here?"
    else:
        return table[id]

# Most of the below is self explanatory for anyone familiar with Flask. I get
# a little funky in places, but for the most part it's all pretty human
# readable. I also use a touch of Jinja2 to make things look nicer since, by
# default, Flask sticks everything in <p> (I think???)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/egg")
def egg():
    return render_template("egg.html")

@app.route("/netlibram/")
def netlibram_start():
    r = int(random.randrange(1, len(nl), 1))
    return redirect("/netlibram/%d" % r, 303)

@app.route("/netlibram/<int:effect_id>")
def netlibram_lookup(effect_id):
    result = effect_lookup(nl, "Net Libram", effect_id)
    return render_template("nlresult.html", result=result, resultnum=effect_id)

@app.route("/wildmagic/")
def wm_start():
    r = int(random.randrange(1, len(wm), 1))
    return redirect("/wildmagic/%d" % r, 303)

@app.route("/wildmagic/<int:effect_id>")
def wm_lookup(effect_id):
    result = effect_lookup(wm, "Wild Magic", effect_id)
    return render_template("wmresult.html", result=result, resultnum=effect_id)

if __name__ == "__main__":
    app.run()