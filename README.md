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

The workshop is divided into 3 parts, each one adding new features to the app or improving an existing one. Each part
has a baseline branch that you can use to start the exercises, as well as a proposed solution.

### Part 1

Baseline branch name = `part1`

Solution branch name = `part1-solution`

The home view currently shows a table with the existing appliances. There is an `Add new` button on the top right of the
table which doesn't do anything yet. Just under it, there is a form to add a new appliance. When the form is submitted,
a POST request is made to the server to create the new appliance. The whole page is then reloaded to show the new
appliance on the table.

#### Exercise

1. Make the `Add new` button show the appliance form when clicked, without reloading the page.
2. When the `Create` button is clicked, submit the form with HTMX and update the appliances table to show the new
   appliance, without reloading the page.

### Part 2 - Add polling calls to update the carbon emissions

Baseline branch name = `part2`

Solution branch name = `part2-solution`

The app has two new views that return the total carbon emissions (gCO2eq/h) given the appliances in the db and the
current carbon intensity (gCO2eq/kWh). The total carbon emissions is displayed on the header of the page, see the
`<span>` tag at the top of `home.html`. It updates through a client event both when the carbon intensity changes and
when a new appliance is created.

The carbon intensity can change throughout the day, so it would be good to update it every 5 minutes. The `services.py`
file has a variable called `carbon_emissions_service` which loads a service to get the current carbon intensity from
the [ElectricityMaps](https://app.electricitymaps.com/) API. To set it up, you'll need to get an API key on their
[developer hub](https://app.electricitymaps.com/developer-hub). If you don't want to do that, don't worry, a random
value will be used instead. However, keep in mind that the carbon intensity will remain the same until you restart the
app.

Once you have the API key, set it as an environment variable called `ELECTRICITY_MAPS_API_KEY`. Copy the `.env.example`
file into a new file called `.env` and add the variable there.

#### Exercise

1. The carbon emissions view has a forced delay of 1 second to simulate a slow response from the server. To give some
   feedback to the user, show an [indicator](https://htmx.org/docs/#indicators) while the request is being processed. An
   svg spinner has been provided for you in `static/img/oval.svg`.

2. Use [polling](https://htmx.org/docs/#polling) to load an alert with the carbon intensity details every 5
   minutes, see the `carbon-intensity-alert` partial in `home.html`. The new alerts should be appended to the top of the
   list, newer first. For development purposes, you can set the polling interval to a lower value like 5-10 seconds.

### Part 3 - Edit and delete appliances

Baseline branch name = `part3`

The app is now complete, with the ability to add new appliances and see how they affect the home's carbon footprint.
However, there is no way to edit or delete existing appliances, because appliances are not always on.

#### Exercise

1. Add another column to the appliance table that contains a toggle button on each row. When clicked, a PUT request
   should be made to toggle the `is_active` appliance property. The request should update the appliance in the db and
   trigger an event to update the total carbon emissions.
2. Add another column to the appliance table that contains a delete button/icon on each row. When clicked, a DELETE
   request should be made to delete the appliance from the db. The row should be removed from the table without
   reloading the page, and an event should be triggered to update the total carbon emissions.
