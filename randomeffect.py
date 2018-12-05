import io
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

with io.open("effects.txt", 'r', encoding='utf8') as effects_source:
    effects = effects_source.readlines()
totaleffects = len(effects)

@app.route("/")
def index():
    r = random.randrange(0, len(effects) - 1, 1)
    return redirect(url_for(random_effect))

@app.route("/<effectid>")
def random_effect(effectid):
    return effects(effectid)

if __name__ == "__main__":
    app.run()