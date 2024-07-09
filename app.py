
from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

@app.route('/')
def hello():
    count = session.get('count', 0)
    session['count'] = count + 1
    return f"You have refreshed this page {session['count']} times."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
