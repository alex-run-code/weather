# WEATHA

Welcome in Weatha, an application to understand how the weather works.

## Install the requirements

We need to have all our dependencies install, so let's run a:

    pip install -r requirements.txt

## Run the migrations

Let's run the migration this way:

    py manage.py makemigrations

then: 

    py manage.py migrate

## How to populate the database

First, let's create our first metrics and locations by doing: 

    python manage.py create_initial

Because we want to use our API to populate the database, let's run the server:

    python manage.py runserver

Now, in another terminal, let's populate the database with the data (this will take 2 minutes):

    python manage.py populate_db

## How to run the tests

Simply use the following command:

    python manage.py test

## How to use the API

The endpoint is the same for both GET and POST requests:

    /api/weather

To make a GET request, you can use the following filters:
start_date, end_date, metric, location

### GET request

Here's an example for "I want the Tmax in England after 2015-02-02":

    /api/weather?&metric=Tmax&start_date=2015-02-02&location=England

### POST request

To make a POST request, here's how to format the data you want to send:

**Data:**

    {
        "location":"1"
        "metric":"1"
        "date":"2020-03-12"
        "value":"22.2"
    }

**Endpoint:**

    /api/weather

## Need to mess around the admin ?

A superuser is already 

