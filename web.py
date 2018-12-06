import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
application = app

with io.open("netlibram.txt", 'r', encoding='utf8') as netlibram_source:
    netlibram = netlibram_source.readlines()
netlibram_total = len(netlibram)

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
        return "The maximum effect for Net Libram is %d" % netlibram_total
    elif effectid == 0:
        return render_template('dice_error.html')
    elif effectid < 0:
        return "How did you even get here?!"
    else:
        return netlibram[effectid]

if __name__ == "__main__":
    app.run()