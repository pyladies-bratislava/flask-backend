# Pyladies Bratislava's Website - backend

We have 2 json API backends: one done with [Flask](https://flask.palletsprojects.com/en/1.1.x/)
and another with [FastAPI](https://fastapi.tiangolo.com/). Both are Python frameworks.

In the future we want to have several backends running simultaneously.
By default Flask runs on port 8000 and FastAPI on 5000.

We are managing Python versions and packages with `virtualenv` at the moment but in the future we will also introduce `poetry`.

## How to run the backends?

Common stuff:

1. Create a virtual environment called `.venv` (if you have Python version 2. and 3., use command: `python3 -m venv .venv`):
~~~
$ python -m venv .venv
~~~
2. Activate virtual environment. (Activated virtual environment will be indicated by (.venv) in the beginning of the terminal line.)
 - on Windows:
~~~
$ .venv\Scripts\activate
~~~
 - on Linux or Mac:
~~~
$ source .venv/bin/activate
~~~
3. Install the requirements:
~~~
(.venv)$ pip install -r requirements.txt
~~~
At this moment you have both Flask and FastAPI installed in your `virtualenv`.

To run Flask:
1. Create a `.env` file with the following environmental variables:
~~~
FLASK_APP=flask_main
FLASK_ENV=development
~~~
2. Start Flask:
~~~
(.venv)$ flask run
~~~

To run FastAPI:
~~~
(.venv)$ uvicorn fastapi_main:app --reload
~~~

### How to create a file in windows terminal:

1. Type copy con testfile.txt, but replace testfile with the desired file name. Press Enter.
2. Type your desired text. This is rudimentary text editor, but it's good for quick notes or code. You can use the Enter key as you type to move to the next line if you wish.
3. Press Ctrl+Z when you're finished editing the file. This saves everything you've typed into the file.
