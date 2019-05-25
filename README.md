News Highlights
====================

- - - -
Author: [Mark Opondo](https://github.com/opond99)

## Description
This is an application that allows a user to get news highlights according to popularity and trends from different categories like sports, technology, business, science and entertaimet.

---------------------------------------------------------------------

## Features

 + List various news sources
 + Categorize news sources


## Technology used

* [python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)


## Installation Reqirements
 This application is not limmited to any os, all you need to have it up and running is:
* python3.6
* Flask
* Flask-Bootstrap
* Flask-Script
* pip3
* Github account

## Installation 
# Cloning into rrepository
```bash
git clone https://github.com/opondo99/News-highlights && cd News-highlights
```

# Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6.6 -m venv virtual
source virtual/bin/activate
```
# Dependencies
### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
* Flask==1.0.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6

## Running the application
To use the application clone the project from https://github.com/opondo99/News-highlights and create a start.sh file in the root folder and add this piece of code.

```bash
export NEWS_API_KEY=<YOUR API KEY>
export SECRET_KEY=<YOUR SECRET KEY>

python3 manage.py runserver
``` 
To get an api key you need to have an account at https://newsapi.org/ and generate your own api key.

## License ([Apache License]http://www.apache.org/licenses/) 

This project is licensed under the apache license, [Mark Opondo](https://github.com/opond99)
