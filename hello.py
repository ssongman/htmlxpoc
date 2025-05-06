# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head>
        <script src="https://unpkg.com/htmx.org@1.9.10"></script>
      </head>
      <body>
        <button hx-get="/hello" hx-target="#result">Say Hello</button>
        <div id="result"></div>
      </body>
    </html>
    """

@app.route("/hello")
def hello():
    return "Hello, HTMX!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)