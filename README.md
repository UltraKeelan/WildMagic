# WildMagic

WildMagic is a lightweight webapp to give you random spell effects from the Net Libram. Inspired by the Wild Magic Sorcerer in D&D, I was driven by laziness to create this tool to regurgitate a random spell effect from the [Net Libram of Random Magical Effects Version 2.00](https://centralia.aquest.com/downloads/NLRMEv2.pdf) by Orrex.

Check out a [live version of the application](http://wildmagic.web.illinois.edu/), running on cPanel using Phusion Passenger.

## Getting Started

Once you have your Python environment configured (see prerequisites), you should be able to clone-n-go. I also created this with some level of extensibility in mind, and I may improve this in the future. Currently, if you want to use a different set of effects, you should be able to simply replace netlibram.txt with your newline-delimited list of effects. Any further changes or additions might require some extra mucking about in the code. Hopefully I'll make that better someday.

### Prerequisites

WildMagic runs in Python 3.x with a few extra things. I'm not going to flesh out how to configure your Python env, because many others before me have done excellent jobs. The only non-default package that I use is

```
flask
```
Flask ships with Jinja2, which I make use of to prettify the page.

### Installing

If your Python env is configured with Flask, you should be able to clone and then run the following:

```
python web.py
```
The console will display some helpful info about how to connect to the server from a browser, some fun warnings, as well as the requests that it's serving.

## Deployment
My deployment flow for WildMagic is a bit ugly, since cPanel doesn't like a git repo and an app directory existing in the same folder. I tried to fool it with some symlink wizardry, but nothing worked. In any case, the only notable deviation from my flow and a standard Flask application is that, because cPanel uses Phusion Passenger, I have to set `application = app` in web.py, and then include `from web import application` as the only line in passenger_wsgi.py. For deploying on other platforms, see [Flask Deployment Options](http://flask.pocoo.org/docs/1.0/deploying/)

## Built With

* [Flask](http://flask.pocoo.org/) - The microframework used
* [web.illinois.edu](https://web.illinois.edu/) - cPanel hosting

## Contributing

If you notice any bugs or odd behavior, or have a feature request, feel free to start an issue or submit a pull request.

## Authors

* **Keelan Lang** - [klang-uofi](https://github.com/klang-uofi/)

## License

This project is licensed under the GNU GPL - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Orrex, for creating the [Net Libram](https://centralia.aquest.com/downloads/NLRMEv2.pdf)
* Wizards of the Coast for publishing 5E
* Stu Turner, for being a kind enough DM to let me use the Net Libram as a 
* Braxton Spence and Kyle Mitchell for helping me think through this and turning me around when I started sprinting in the wrong directions.
