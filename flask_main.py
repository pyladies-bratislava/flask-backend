from flask import Flask, request
from flask_cors import CORS

#from backend.chatbot import bot
from backend.events import get_google_cal_events
from backend.about import get_pyladies_about_text


app = Flask(__name__)
CORS(app)
BASE_DIR = app.root_path

@app.route("/health")
def get_health():
    return {"health": "ok"}


@app.route("/menu")
def get_menu():
    return {"menu": ["Meetups Calendar", "Chat Bot", "Scholarships", "About us", "Vote for a topic"]}


@app.route("/about")
def get_about():
    about = get_pyladies_about_text()
    return {"about": about}


@app.route("/events")
def get_events():
    events = get_google_cal_events()
    return {"events": events}


# @app.route("/chatbot", methods=["POST"])
# def post_interaction():
#     interaction = request.json["interaction"]
#     response = bot.get_response(interaction)
#     return response.text
