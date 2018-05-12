from flask import Flask
from flask import render_template
from subprocess import call
app = Flask(__name__)

FLASK_STATIC_PATH='static'
ICONS_PATH=FLASK_STATIC_PATH
FLASK_ADDRESS='0.0.0.0'
FLASK_PORT=8080

@app.route("/")
def index():
    return render_template('index.html', icons=ICONS_PATH)

if __name__ == "__main__":
    call(["/etc/init.d/nginx", "start"])
    app.run(debug=True, host=FLASK_ADDRESS, port=FLASK_PORT)

