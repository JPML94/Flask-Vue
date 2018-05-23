# Flask-VueJs-App

## Features
* Minimal Flask App with modular Config
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* Starter [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) with Babel and ESlint.
* [Vuex](https://vuex.vuejs.org/) for state management
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://vuex.vuejs.org/) for backend communication
* Sample Vue [Filters](https://vuejs.org/v2/guide/filters.html)
* Heroku Configuration with one-click deployment

## Installation

##### Before you start

* Make sure node + npm are installed (tested with npm v5.6)
	```
	$ npm --v
	```

* Python 3 is installed (tested with 3.6). Type 'exit()' to get out of the python shell.
	```
	$ python3
	```

* Clone this repository:

	```
	$ git clone https://github.com/JPML94/Flask-Vue.git
	$ cd Flask-Vue
	```

##### Create a virtual enviroment inside the project folder and install the packages located in Pipfile:
 - For Windows and Linux:
	```
	$ pip install --user pipenv
	$ pipenv install
	```
 - For Mac:
	```
	$ brew install pipenv
	```

* Install npm dependencies for client side

	```
	$ cd app/client/angler
	$ npm install
	```

##### Virtual Environment

Make sure you're inside your virtual environment before starting the server and client by running:

```
$ pipenv shell
```

Make sure to do this on the root application folder, in this case called 'Flask-Vue'

##### Api Server

From the root directory run:

```
$ python -m app serve_api
```

This will start the flask development server on `localhost:5000` (renders dist folder on angler app) and will respond to all requests on `/api.`.
This command is the same as running `python run.py`

##### Client Server

Start another terminal window, make sure you're in the project folder and virtual environment active (pipenv shell), then run:

```
$ python -m app serve_client
```

This will launch your browser and server the Vue application on `localhost:8080`. T
he vue app will hit `localhost:5000` to fetch resources.

This combination allows you have both your backend python files, as well as the Vue app files autoreload on each file save.

##### Setup ESLint and python to recognize your environment

For your editor to recognize your python libraries run:
```
$ pipenv --py
```
Copy that path to your editor settings, for example in Visual Studio Code python.pythonPath = {path-to-python-environment}

To get automatic linting for your Vue files in VS Code you need to add this to your settings file:
eslint.validate": [
        "javascript", {
            "language": "vue",
            "autoFix": true
        }

## Production Server

* Build your Vue Application:
```
$ python -m app build
```
This commands is a shorcut for cd-ing into `/app/client/vue_app` and running `$ npm run build`.

* Commit your code

* Setup your heroku app:

	```
	$ heroku apps:create flask-vue
	$ heroku config:set FLASK_CONFIG=Production
	$ heroku config:set SECRET=ThisIsTheSecretSuperKey2
	$ heroku git:remote --app flask-vue
	```
* Push your application to heroku:

	```$ git push heroku```
