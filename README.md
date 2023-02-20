# Quiz Web App

This is a Django-based web application that allows users to create their own quizzes and answer quizzes created by other users. After answering a quiz, the user can see all the answers and the correct answers highlighted in green, and the wrong answers highlighted in red.

## Installation
Clone the project from GitHub:

```bash
git clone https://github.com/charlysgy/private-backend.git
``` 

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install django
```

Run the migrations:
```bash
python manage.py migrate
``` 

## Usage
To start the server, run:

```bash
python manage.py runserver
```

You can then access the web app by navigating to http://localhost:8000/ in your web browser.

## Creating a quiz
To create a quiz, click on the link on the home page. You will be prompted to enter a theme. Once you have done so, you can add questions to your quiz . Each question requires a title and at least four possible answers, one of which is correct. You can add at least one question and at most ten.

## Answering a quiz
To answer a quiz, click on a theme on on the home page. Once you have selected a quiz, you will be presented with the quiz questions one by one. For each question, select the answer you think is correct, after you have answered all the questions, click the "Validate" button. You will be shown the results page, which displays all the answers and highlights the correct answers in green and the incorrect answers in red.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Before submitting a pull request, please make sure your changes are consistent with the project's coding style and have been tested thoroughly.
