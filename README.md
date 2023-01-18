# stackoverflow-V1

[![Maintainability](https://api.codeclimate.com/v1/badges/3b5bfc650d1971aa2fe8/maintainability)](https://codeclimate.com/github/mungaiDaniel/stackoverflow-V1/maintainability) [![Coverage Status](https://coveralls.io/repos/github/mungaiDaniel/stackoverflow-V1/badge.svg?branch=develop)](https://coveralls.io/github/mungaiDaniel/stackoverflow-V1?branch=feature-complete) [![CircleCI](https://dl.circleci.com/status-badge/img/gh/mungaiDaniel/stackoverflow-V1/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/mungaiDaniel/stackoverflow-V1/tree/main)

************************************************************************************************************************************************

## Description

StackOverflow is a platform where people can ask question and provide answers.
I have build Api endpoints with the use of data structure to store data in memory (with no database)

************************************************************************************************************************************************

## Development

This Application is developed using python pure Flask.The data is stored on python data structures

## Endpoints

| METHOD | ENDPOINT                              | DESCRIPTION
|--------|---------------------------------------|---------------------------------
| POST   | /api/v1/question                      | Endpoint to create a question
| GET    | /api/v1/question                      | Endpoint to get all question
| GET    | /api/v1/question/<int:id>             | Endpoint to get one question
| DELETE | /api/v1/question/<int:id>             | Endpoint to Delete a question
| POST   | /api/v1/answer/<int:question_id>      | Endpoint to create a answer
| GET    | /api/v1/answers/<int:question_id>     | Endpoint to get all answers
| GET    | /api/v1/answers/<int:answer_id>       | Endpoint to get one answer
| PUT    | /api/v1/answer/<int:answer_id>        | Endpoint to update an answer
| DELETE | /api/v1/question/<int:answer_id>      | Endpoint to Delete an answer

#### Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python web microframework)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)
- [Pylint](https://www.pylint.org/) (Linting library)
- [Pip3](https://pypi.org/project/pip/) (Python package installer)

#### Getting Started:

**To start the app, please follow the instructions below:**

***Create test and development databases as shown***

**On your terminal**

  $ psql

  $ CREATE DATABASE stackoverflow_lite;

  $ CREATE DATABASE stackoverflow_lite_test;

**On your terminal:**

Install pip:

  $ sudo apt-get install python-pip

Clone this repository:

  $ git clone https://github.com/Nduhiu17/StackOverflow-lite-v1.git

Get into the root directory:

  $ cd StackOverflow-lite-v1/

Install virtual enviroment:

  $ python3.6 -m venv virtual

Activate the virtual environment:

  $ source virtual/bin/activate
  
Install requirements

  $ pip install -r requirements.txt

Create a start.sh file and export your app's secret key inside as shown by example_start.sh

Give the file executable permissions by right clicking the file and checking the execute button as shown by the image below:

![start](https://user-images.githubusercontent.com/30591881/45145592-b6e7fd80-b1c9-11e8-8966-4c9ae39c6f4b.png)

Run the app by:

    $ export FLASK_APP=manage.py
    $ flask run



#### Running the tests

Run the tests by:

    $ coverage run -m pytest