from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch a random quote from Quotable API
    response = requests.get("https://api.quotable.io/random")
    quote_data = response.json()
    quote = f'"{quote_data["content"]}" — {quote_data["author"]}'
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/new-quote')
def new_quote():
    response = requests.get("https://api.quotable.io/random")
    return response.json()  