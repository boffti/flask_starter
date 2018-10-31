# Flask Starter Project

This is a barebones Flask project to jumpstart your Web App

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Concepts Used

- Flask 
- JINJA Templating
- CSS Styling
- JQuery Basics
- JQuery AJAX - GET and POST
- Forms
- SQLITE 3 Databases

### Prerequisites

1. Install Python from [here](https://www.python.org/downloads/).

2. Open command prompt and type 
    ```
    python --version 
    ```

    If Python is successfully installed, you should see
    ```
    Python 3.x.x
    ```
3. Ensure pip is installed by opening command prompt and typing

    ```
    pip --version
    ```
    If pip is successfully installed, you should see
    ```
    pip x.x from <path to pip>
    ```

4. Download and install Visual Studio Code from [here](https://code.visualstudio.com/).
5. Clone or download this repository to your computer and extract it.

### Installing

This will help you set up your dev environment.

1. Open command prompt and run the following - 
    ```
    pip install flask
    ```
    This will install the Flask package globally on your computer

2. Navigate to your projet directory and hold <kbd>Shift</kbd> and right click inside the project folder. Click on '<i>Open command window here'</i> in the dropdown that appears.

3. In the command window, notice that it is already navigated to the project folder.
4. Set the flask environment variable by executing the following
    ```
    set FLASK_APP=app.py
    ```



## Running the app
1. Enable debugging mode for the flask app
    ```
    set FLASK_DEBUG=1
    ```
2. Run the app
    ```
    flask run
    ```
    You will see a success message that the server was started.

3. Open the browser and navigate to <strong><i>[127.0.0.1:5000/](127.0.0.1:5000/)</i></strong> which is your localhost.


## Deployment

Lets cross that bridge when we get to it.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [JQuery](https://jquery.com/) - JS framewoek
* [MD Bootstrap](https://mdbootstrap.com/) - CSS framework

