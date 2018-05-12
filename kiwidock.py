from flask import Flask
from flask import render_template
from subprocess import call
app = Flask(__name__)

FLASK_STATIC_PATH='static'
ICONS_PATH=FLASK_STATIC_PATH
FLASK_ADDRESS='0.0.0.0'
FLASK_PORT=8080
APP_ROOT_DIR='/app'

@app.route("/")
def index():
    return render_template('index.html', icons=ICONS_PATH)

if __name__ == "__main__":
    call(['/etc/init.d/nginx', 'start'])
    call(['uwsgi', '--ini', APP_ROOT_DIR + '/kiwidock_uwsgi.ini'])
    app.run(debug=True, host=FLASK_ADDRESS, port=FLASK_PORT)

