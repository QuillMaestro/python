from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
    setup, punchline = get_joke()
    if setup and punchline:
        return render_template('joke.html', setup=setup, punchline=punchline)
    else:
        return "Oops! Failed to get a joke. Try again later."

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return joke["setup"], joke["punchline"]
    return None, None

if __name__ == '__main__':
    app.run()
