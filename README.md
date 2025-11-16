# Carbon Home Watcher 🏡

Carbon Home Watcher is an app that allows users to monitor their home's carbon footprint. It's a simple carbon footprint
tracker, where users can add their home appliances and see how they affect their home's carbon footprint. The app is
built using Django and HTMX.

This app has been designed as a way to showcase the use of HTMX in a Django project. HTMX is a library that allows you
to build modern web applications with minimal JavaScript. It allows you to update parts of the page without reloading
the entire page, amongst other things, which can make your app feel faster and more responsive.

The idea of this repo is not only to show an example of how you can use Django with HTMX, but also to provide a set of
step-by-step exercises/instructions to familiarise yourself with some basic HTMX features.

## Getting started

To get started with this project, you'll need to have 
[uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) installed locally.

### Running the project locally

1. First, apply the database migrations with:

    ```bash
    uv run manage.py migrate
    ```
   
2. Start the development server with:

    ```bash
    uv run manage.py runserver
    ```

## Workshop step-by-step instructions

The workshop is divided into 4 parts, each one adding new features to the app or improving an existing one. Each part
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
reloading the page. The form should disappear and some text should be shown to inform the user that the appliance has
been created successfully.

> [!TIP]
> You'll need to replace two elements in the DOM but hx-target only lets you target one.
> See [out of band swap](https://htmx.org/docs/#oob_swaps).
