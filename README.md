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

### Part 1 - Out of band swapping

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

### Part 2 - Implementing partials and triggering events

Baseline branch name = `part2`

Solution branch name = `part2-solution`

#### Exercise

This task has two goals:

1. Improve our project's implementation of Locality of Behaviour by using
   the [django-template-partials](https://github.com/carltongibson/django-template-partials) package. The package has
   already been installed for you so you just need to add the partials within our `partials/` folder directly into our
   `home.html` template.
2. Replace the current out of band swap with a slightly more sophisticated approach,
   a [trigger event](https://htmx.org/headers/hx-trigger/). This will allow you to trigger the swap when a specific
   event occurs i.e. event driven programming.

> [!TIP]
> Create a new view other than the main `HomeView` that returns the appliance table. Make a request to this new view
> when the page is first accessed. See [lazy loading](https://htmx.org/examples/lazy-load/).

### Part 3 - Add polling calls to update the carbon emissions

Baseline branch name = `part3`

Solution branch name = `part3-solution`

The app has two new views that return the total carbon emissions (gCO2eq/h) given the appliances in the db and the
current carbon intensity (gCO2eq/kWh), but these views are not being used yet. Your task is to connect the app with
them to display the current carbon emissions in real time as well as to monitor the carbon intensity evolution.

The carbon intensity can change throughout the day, so it would be good to update it every 5 minutes. The `services.py`
file has a variable called `carbon_emissions_service` which loads a service to get the current carbon intensity from
the [ElectricityMaps](https://app.electricitymaps.com/) API. To set it up, you'll need to get an API key on their
[developer hub](https://app.electricitymaps.com/developer-hub). If you don't want to do that, don't worry, a random
value will be used instead. However, keep in mind that the carbon intensity will remain the same until you restart the
app.

Once you have the API key, set it as an environment variable called `ELECTRICITY_MAPS_API_KEY`. Copy the `.env.example`
file into a new file called `.env` and add the variable there.

#### Exercise

1. Use [polling](https://htmx.org/docs/#polling) to load an alert with the carbon intensity details every 5
   minutes, see the `carbon-intensity-alert` partial in `home.html`. For development purposes, you can set the polling
   interval to a lower value like 5-10 seconds.

2. The total carbon emissions should be displayed in the header of the page, see the `<span>` tag at the top
   of `home.html`. It should be updated both when the carbon intensity changes and when a new appliance is added.

3. The carbon emissions view has a forced delay of 1 second to simulate a slow response from the server. To give some
   feedback to the user, show an [indicator](https://htmx.org/docs/#indicators) while the request is being processed. An
   svg spinner has been provided for you in `static/img/oval.svg`.
