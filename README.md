# stackoverflow-V1

[![Maintainability](https://api.codeclimate.com/v1/badges/417b95c91d52c4ed7201/maintainability)](https://codeclimate.com/github/mungaiDaniel/stackoverflow-V1/maintainability) [![Coverage Status](https://coveralls.io/repos/github/mungaiDaniel/stackoverflow-V1/badge.svg?branch=develop)](https://coveralls.io/github/mungaiDaniel/stackoverflow-V1?branch=feature-complete)

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
