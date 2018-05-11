from flask import Flask
from flask import render_template
from os import path
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', icons='static')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

