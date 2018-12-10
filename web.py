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

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/netlibram/")
def netlibram_start():
    r = int(random.randrange(1, len(netlibram), 1))
    return redirect("/netlibram/%d" % r, 303)

@app.route("/netlibram/<int:effectid>")
def netlibram_lookup(effectid):
    effectid -= 1 # A dirty way to fix the indexing (I think lol)
    if effectid >= netlibram_total:
        nl_max_exceeded = "The maximum effect for the Net Libram is {:,}!".format(netlibram_total)
        return render_template('nlresult.html', result=nl_max_exceeded)
    elif effectid == -1:
        return render_template('dice_error.html')
    elif effectid < -1:
        # I think it might be possible to get here but I haven't figured out how yet
        return "How did you even get here?"
    else:
        resultnum = effectid + 1 # for rendering the actual effect number in the title
        return render_template('nlresult.html', result=netlibram[effectid], resultnum=resultnum)

if __name__ == "__main__":
    app.run()