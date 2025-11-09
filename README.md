# Carbon Home Watcher 🏡

Carbon Home Watcher is an app that allows users to monitor their home's carbon footprint. It's a simple carbon footprint
tracker, where users can add their home appliances and see how they affect their home's carbon footprint. The app is
built using Django, PostgreSQL and HTMX.

This app has been designed as a way to showcase the use of HTMX in a Django project. HTMX is a library that allows you
to build modern web applications with minimal JavaScript. It allows you to update parts of the page without reloading
the entire page, amongst other things, which can make your app feel faster and more responsive.

The idea of this repo is not only to show an example of how you can use Django with HTMX, but also to provide a set of
step-by-step exercises/instructions to familiarise yourself with some basic HTMX features.

## Getting started

To get started with this project, you'll need to either:

* Have Docker installed on your machine. If you don't have Docker installed, you can download it from
  the [official Docker website](https://docs.docker.com/get-docker/).
* Or, you can load the project locally. To do this, you'll need to have [python](https://www.python.org/)
  and [PostgreSQL](https://www.postgresql.org/) installed locally.

### Running the project with Docker

To run the project, you need to have the [Docker](https://docs.docker.com/) daemon running.

#### Set up database

Before deploying the app, you'll need to set up the database by applying the
initial [Django migrations](https://docs.djangoproject.com/en/5.1/topics/migrations/). To apply them, run the following
command:

    docker-compose run --rm web python manage.py migrate

#### Deploy the app

To deploy the app, run the following command:

    docker-compose up

### Running the project locally

1. Create a virtual environment with the project's dependencies:

    ```bash
    python -m venv venv/
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Create a PostgreSQL database:

    ```bash
    createdb carbonhomewatcher
    ```

3. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the Django server:

    ```bash
    python manage.py runserver
    ```

## Workshop step by step instructions

The workshop is divided into 5 parts, each one adding a new feature to the app or improving an existing one. Each part
has a baseline branch that you can use to start the exercises, as well as a proposed solution.

### Part 1

Baseline branch name = `part1`

Solution branch name = `part1-solution`

The home view currently shows a table with the existing appliances. There is an `Add new` button on the top right of the
table which makes a request via HTMX to the server to get the form to add a new appliance. When the form is submitted, a
POST request is made to the server to create the new appliance. The page is then reloaded to show the new appliance on
the table.

#### Exercise

Your task is to update the app so that when the form is submitted, the new appliance is added to the table without
reloading the page. The form should disappear and some text should be shown to confirm that the appliance has been
created successfully. To replace the table, use an [out of band swap](https://htmx.org/docs/#oob_swaps).
