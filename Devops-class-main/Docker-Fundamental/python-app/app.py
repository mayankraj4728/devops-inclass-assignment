from flask import Flask  # type: ignore[import-not-found]

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Hello World from Python + Docker!</h1>
    <p><strong>Name:</strong> Mayank Raj</p>
    <p><strong>Roll No:</strong> 24bcs10351</p>
    """

app.run(host="0.0.0.0", port=5000)