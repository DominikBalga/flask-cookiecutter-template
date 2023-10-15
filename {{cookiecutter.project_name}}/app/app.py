from flask import Flask, render_template, redirect, url_for, flash, send_from_directory
import os

# Create a Flask application instance
app = Flask(__name__)

logo_img = "{{cookiecutter.project_name}}/app/static/images/dummy.png" #os.path.basename("{{cookiecutter.logo_img_url}}")
@app.route("/")
def home():
    return render_template("index.html", img_name=logo_img)

if __name__ == "__main__":
    app.run(debug=True)