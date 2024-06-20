# My Blog Application

Welcome to the **My Blog** application! This project is built with Flask and provides a simple blogging platform. Below you will find instructions on how to set up and run the project, as well as an overview of the project structure.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Templates](#templates)
  - [index.html](#indexhtml)
  - [post.html](#posthtml)
- [License](#license)

## Project Overview

This application is a Flask-based blog platform that retrieves blog posts from a remote API and displays them on the homepage. Users can click on individual posts to view their details.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/my-blog.git
   cd my-blog

2. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt

## Running the Application

Once you have installed the dependencies, you can run the Flask application with the following command:
    ```sh
    flask run

The application will be accessible at http://127.0.0.1:5000.

## Project Structure
    ```arduino
    my-blog/
    ├── static/
    │   └── css/
    │       └── styles.css
    ├── templates/
    │   ├── index.html
    │   └── post.html
    ├── app.py
    ├── post.py
    ├── requirements.txt
    └── README.md


