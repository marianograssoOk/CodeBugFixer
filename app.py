from flask import Flask, request, render_template
from openai import OpenAI
import config
app = Flask(__name__)
# API Token
client = OpenAI(api_key = config.API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()