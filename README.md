# ride_my_way_api_2

[![Build Status](https://travis-ci.org/araaliFarooq/ride_my_way_api_2.svg?branch=master)](https://travis-ci.org/araaliFarooq/ride_my_way_api_2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/06dc688a05034adcbcb97c8ff47ac190)](https://www.codacy.com/app/araaliFarooq/ride_my_way_api_2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/ride_my_way_api_2&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/ride_my_way_api_2/badge.svg?branch=master)](https://coveralls.io/github/araaliFarooq/ride_my_way_api_2?branch=master)


## About
This is an API for a transportation application that allows users (Drivers) to create and add ride offers to which other users (Passengers) make request to join.

## Features
- Register a user
- Login a user
- Get all the offers for logged in users
- Request to join a ride offer
- Create and add a ride offer.
- View a particular ride offer.
- Accept or reject a ride request.
- View all rerquests to a specific ride offer.

## Other features
- View request status

## Tools Used
- [Flask](http://flask.pocoo.org/) - web microframework for Python
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database

## Requirements
Python 3.x.x+
 
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/ride_my_way_api_2.git
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```sh
    $ cd ride_my_way_api_2
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/user/register | True | Create a user account
POST | /api/v1/user/login | True | Login a user

#### Endpoints to create, read user ride offers and requests
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/rides/create_offer | False | Create an offer
GET | /api/v1/rides/view_all_offers | False | Fetch all offers for a logged in user
GET | /api/v1/rides/view_single_offer/<ride_id> | False | Fetch a single offer for a logged in user
GET | /api/v1/rides/send_request/<location>/<destination>/<ride_id> | False | Send a request to join a ride offer for a logged in user
GET | /api/v1/requests/all_requests/<ride_id> | False | View all requests to a specific offer
PUT | /api/v1/rides/requests/status/<status>/<request_id>/<ride_id> | False | Respond to ride requests(Accept or reject)

## Authors
[Araali Sseruwu Farooq](https://github.com/araalifarooq)


