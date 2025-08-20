from flask import Flask, render_template
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')  # This should be 'MAIL_PORT', not just 'PORT'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/example_route")
def example_route():
    return render_template("example_route.html")

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)))
