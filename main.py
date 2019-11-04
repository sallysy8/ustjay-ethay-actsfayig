import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_latinizer_response(fact_string):
    data = {'input_text': fact_string}
    response = requests.post(
        'https://hidden-journey-62459.herokuapp.com/piglatinize/',
        data=data
        # allow_redirects=False
        #params={'q': 'requests+language:python'},
        #headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    )

    return response


@app.route('/')
def home():
    fact = get_fact()
    response = get_latinizer_response(fact)
    return response.url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
