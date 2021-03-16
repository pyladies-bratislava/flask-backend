# Google Calendar APIs in Pyladies Bratislava website

##### What is API?
API is an abbreviation for an _Application Programming Interface_ which serves for exchanging data. 
APIs define the format of the data together with the way of reaching them, e.g request types or authentification methods.

##### Google APIs
Google Services offer Google APIs for communication and integration with other services. 
The communication is secured by [OAuth 2.0](https://en.wikipedia.org/wiki/OAuth) protocol.
One of the APIs offered by Google Services are Google Calendar APIs.

### Google Calendar APIs in Pyladies Bratislava website
The goal of our Pyladies Bratislava Events' page is to show events from the public calendar owned by bratislava@pyladies.com Google account.
Pyladies Bratislava website is a third-party service which communicate with Google Services via 
[server-to-server interaction](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount), since no user consent is required.

##### Step 1: _Enabling Google APIs_
In the [Google API Console](https://console.cloud.google.com/iam-admin/serviceaccounts) the APIs have to be enabled.

##### Step 2: _Obtaining Service Account_
For reaching Google Calendar APIs via server-to-server interaction the OAuth2.0 aouthorization with _service account_ is necessary.
The _service account_ can be obtained in the [Google API Console](https://console.cloud.google.com/iam-admin/serviceaccounts) and 
contains credentials such as a generated unique e-mail address and a public/private key pair for authentication.

##### Step 3: _Storing Service Account Credentials in Heroku_
When our website's backend hosted in [Heroku server](https://dashboard.heroku.com/apps/bratislava-flask-backend/) 
calls the Google Calendar APIs from Google Services it uses the Service Account Credentials credentials for authentication. 
The credentials are stored as configuration variables in Heroku server.

##### Step 4: _Request and authentication of the Google Calendar APIs_
For requesting Google Calendar APIs from our website's backend using python these libraries are used:
 - [google-api-python-client](https://pypi.org/project/google-api-python-client/)
 - [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/)
 - [google-auth](https://pypi.org/project/google-auth/)

The credentials stored in Heroku are used for authentication.
