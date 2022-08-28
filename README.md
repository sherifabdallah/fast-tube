# FastTube
FastTube YouTube Downloader helps you save Youtube videos to your device. You can choose from a variety of formats and qualities to download.


## Table of Content
- [Youtube Ad Blocker](#youtube-ad-blocker)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [URL](#url)
  * [Author](#author)

## Tools
1. Python
2. Django
3. Pytube
5. youtube-search-python
4. CSS
5. JavaScript


## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/fast-tube fast-tube
```
* Install Python 3.8 venv, pip and compiler

```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd fast-tube
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

* then you will have to migrate the db

```sh
(venv)$ python manage.py migrate --run-syncdb
```
* Collect all the static files your are using in all the apps even the third party apps you installed by pip
```sh
(venv)$ python manage.py collectstatic
```

* Finally run The FastTube Server
```sh
(venv)$ python manage.py runserver
```
* And navigate to `http://127.0.0.1:8000`.


## URL
* You can also navigate to the main website without needing to install python, you can navigate it from [here](https://fasttube.pythonanywhere.com)
## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
