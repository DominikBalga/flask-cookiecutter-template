from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! This is {{cokiecutter.project_name}} - your own Flask app."

if __name__ == "__main__":
    app.run(debug=True)