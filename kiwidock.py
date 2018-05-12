from flask import Flask
from flask import render_template
from os import path
app = Flask(__name__)

FLASK_STATIC_PATH='static'
ICONS_PATH=FLASK_STATIC_PATH

@app.route("/")
def index():
    return render_template('index.html', icons=ICONS_PATH)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

