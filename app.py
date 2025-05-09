from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour toi, bienvenue dans EventManager ✨"

if __name__ == "__main__":
    app.run(debug=True)
