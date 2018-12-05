import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
application = app

with io.open("effects.txt", 'r', encoding='utf8') as effects_source:
    effects = effects_source.readlines()
totaleffects = len(effects)

@app.route("/")
def index():
    r = int(random.randrange(0, len(effects) - 1, 1))
    return redirect(r, 303)

@app.route("/<int:effectid>")
def effect_lookup(effectid):
    return effects[effectid]

if __name__ == "__main__":
    app.run()