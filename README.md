# User Todo List Flask RESTful Microservice

This is a Flask-based microservice for managing user-specific todo lists. It provides basic CRUD operations and user authentication.

## Setup

1. Install Docker: https://docs.docker.com/get-docker/
2. Clone this repository: `git clone [https://github.com/username/todo-microservice.git](https://github.com/Reverseflash2022/User-Todo-List-Flask-RESTful-Microservice.git)`
3. Navigate to the repository: `cd todo-microservice`
4. Build the Docker image: `docker build -t todo-microservice .`
5. Run the Docker container: `docker run -p 5000:5000 todo-microservice`

The application will be available at `http://localhost:5000`.

## API Endpoints

- POST /register: Register a new user
- POST /login: Login a user
- GET /todos: Get all todos for the logged-in user
- POST /todos: Create a new todo for the logged-in user
- PUT /todos/<int:todo_id>: Update a specific todo for the logged-in user
- DELETE /todos/<int:todo_id>: Delete a specific todo for the logged-in user
