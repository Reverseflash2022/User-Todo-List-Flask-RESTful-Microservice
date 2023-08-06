# User Todo List Flask RESTful Microservice

This repository contains a production-ready, robust, and comprehensive RESTful microservice for managing a user's to-do list.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the Application](#running-the-application)
- [Testing with Postman](#testing-with-postman)
- [API Endpoints & Test Data](#api-endpoints--test-data)
- [Contributions](#contributions)
- [License](#license)

## Features
- CRUD operations for managing todos.
- Robust user authentication and authorization.
- Rate limiting for preventing abuse.
- Comprehensive error handling and logging.
- API versioning.
- Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.
- Database migrations with Flask-Migrate.

## Getting Started

### Prerequisites

- Python 3.6 or newer.
- Virtual environment (`venv`).
- MySQL server running locally or remotely.
- Postman for API testing.

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-github-username/todo-microservice.git
    cd todo-microservice
    ```

2. **Setup Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # If you're using bash
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables:** Adjust any values in the `.env` file if necessary. Then, export these variables to your shell:
    ```bash
    export $(cat .env | xargs)
    ```

### Database Setup

1. **Initialize Database:**
    ```bash
    flask db init
    ```

2. **Run Migrations:**
    ```bash
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

### Running the Application

Start the Flask application with the following command:
```bash
python run.py
```

...Your application should now be running on `http://localhost:5000`.

## Testing with Postman

1. **Launch Postman:** Start the Postman desktop app on your MacBook.

2. **Setup Requests:** To facilitate your testing, here are some sample endpoints:

    - **Register User:**
      - Method: POST
      - URL: `http://localhost:5000/api/v1/register`
      - Body: JSON (e.g., `{"username": "alice", "password": "wonderland"}`)

    - **Login User:** 
      - Method: POST
      - URL: `http://localhost:5000/api/v1/login`
      - Body: JSON (e.g., `{"username": "alice", "password": "wonderland"}`)

      Upon a successful login, you'll receive a JWT token. Keep it safe, and use it for authenticated routes.

    - **Create Todo:** 
      - Method: POST
      - URL: `http://localhost:5000/api/v1/todos`
      - Headers: 
        - Key: `Authorization`
        - Value: `Bearer YOUR_JWT_TOKEN`
      - Body: JSON (e.g., `{"title": "Buy groceries", "description": "Milk, Bread, Eggs"}`)

    - **Get All Todos:** 
      - Method: GET
      - URL: `http://localhost:5000/api/v1/todos`
      - Headers: 
        - Key: `Authorization`
        - Value: `Bearer YOUR_JWT_TOKEN`

    - Add more requests as per the available API endpoints.

3. **Logging Out:** 
    - Method: POST
    - URL: `http://localhost:5000/api/v1/logout`
    - Headers: 
      - Key: `Authorization`
      - Value: `Bearer YOUR_JWT_TOKEN`

**Note:** Replace `YOUR_JWT_TOKEN` with the token you receive upon logging in. Always ensure that you're using the test data and not any real credentials while testing.

## API Versioning

The current version of the API is v1. You can find the version in the URL (e.g., `/api/v1/`). We've incorporated this to facilitate potential future improvements without causing disruptions to existing clients.

## Continuous Integration/Continuous Deployment (CI/CD)

We employ GitHub Actions to achieve a smooth CI/CD pipeline. Every push to this repository triggers the CI pipeline, which runs unit tests. Successful merges into the main branch then trigger the CD pipeline.

## Contributions

Contributions are always welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Troubleshooting & Feedback

Should you encounter any issues, please check the logs generated by the application. For further inquiries or feedback, feel free to raise an issue on GitHub.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.

---

Thank you for choosing the User Todo List Flask RESTful Microservice. We hope you find it efficient and easy to use.

