import os

import flask
import google.oauth2.credentials
import google_auth_oauthlib
from flask import Flask, request
from flask_cors import CORS

#from backend.chatbot import bot
from backend.events import get_google_cal_events, CLIENT_SECRETS_FILE, SCOPES
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
    flask.session.clear()

    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load the credentials from the session.
    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])

    events = get_google_cal_events(credentials)
    return {"events": events}


@app.route('/authorize')
def authorize():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(
      # This parameter enables offline access which gives your application
      # both an access and refresh token.
      access_type='offline',
      # This parameter enables incremental auth.
      include_granted_scopes='true')

    # Store the state in the session so that the callback can verify that
    # the authorization server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verify the authorization server response.
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    flask.session['credentials'] = {
      'token': credentials.token,
      'refresh_token': credentials.refresh_token,
      'token_uri': credentials.token_uri,
      'client_id': credentials.client_id,
      'client_secret': credentials.client_secret,
      'scopes': credentials.scopes
    }
    print(f"Credentials: {credentials.__dict__}")

    return flask.redirect(flask.url_for('get_events'))


# @app.route("/chatbot", methods=["POST"])
# def post_interaction():
#     interaction = request.json["interaction"]
#     response = bot.get_response(interaction)
#     return response.text
