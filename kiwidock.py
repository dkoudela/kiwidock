from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "I want to attend the Kiwi.com Weekend in the Cloud"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

