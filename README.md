# Django Project

This is my first Django project, which consists of multiple applications. Each application serves a different purpose. Let's dive into the details of each application.

## Applications

### Hello

The Hello application is a simple greeting app. It allows you to say hello to anyone or anything. You can input a name or an object, and the application will display a greeting message accordingly.

### New Year Checker

The New Year Checker application is a simple HTML page renderer. It tells you whether it is currently the new year or not. It displays a message indicating whether it is a new year or not based on the current date.

### Tasks

The Tasks application is a mini-project for creating a TODO list using Django Forms. It provides client-side and server-side validation to ensure that tasks are entered correctly. It also includes CSRF token protection to prevent Cross-Site Request Forgery (CSRF) attacks, and sessions to store unique data on the server side for each new visit to the website.

## Getting Started

To run this Django project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Python (version 3.9.5 or higher) if you haven't already.
3. Create a virtual environment and activate it.
4. Install the required dependencies by running the following command:

5. Apply the database migrations by running the following command:
```
python manage.py migrate
````
6. Start the development server by running the following command:
````
python manage.py runserver
````
7. Open your web browser and navigate to `http://localhost:8000` to access the project.

## Features

- **Hello**: Say hello to anyone or anything.
- **New Year Checker**: Check if it is the new year or not!
- **Tasks**: Create a TODO list using Django forms. Includes client-side and server-side validation, CSRF token protection, and sessions.

## Usage

1. Navigate to the Tasks application in your web browser.
2. Create a new task by filling out the form and submitting it.
3. The form will perform client-side validation to ensure that the task is entered correctly.
4. Upon submission, the form will perform server-side validation to further validate the task and save it to the database.
5. The CSRF token is automatically included in the form to prevent CSRF attacks.
6. The task will be added to the TODO list, and you can view, update, or delete tasks as needed.
7. Sessions are used to store unique data on the server side for each new visit to the website.

## Template Inheritance

Django's template inheritance allows us to create a layout.html file that contains the general structure of our page. Other templates can inherit from this layout.html file and define specific content blocks.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request describing your changes.
