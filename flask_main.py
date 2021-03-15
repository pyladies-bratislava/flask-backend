import os

from google.oauth2 import service_account
from flask import Flask, request
from flask_cors import CORS

#from backend.chatbot import bot
from backend.events import get_google_cal_events, SERVICE_ACCOUNT_FILE, SCOPES
from backend.scraping import get_pyladies_about_info


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/health")
def get_health():
    return {"health": "ok"}


@app.route("/menu")
def get_menu():
    return {"menu": ["Meetups Calendar", "Chat Bot", "Scholarships", "About us", "Vote for a topic"]}


@app.route("/about")
def get_about():
    pyladies_about_info = get_pyladies_about_info()
    return {"about": "From international Pyladies website:" + pyladies_about_info}


@app.route("/events")
def get_events():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    events = get_google_cal_events(credentials)
    return {"events": events}


# @app.route("/chatbot", methods=["POST"])
# def post_interaction():
#     interaction = request.json["interaction"]
#     response = bot.get_response(interaction)
#     return response.text
