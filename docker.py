from flask import Flask

app = Flask(__name__)

print("practice docker in change for branch")

@app.route("/")
def home():
    return "practice docker in change for branch"

app.run(host="0.0.0.0", port=8080)