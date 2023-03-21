# FastAPI Docker App

This is a simple web application built with FastAPI and Docker containers. The application provides two API endpoints, which return a simple message and a JSON response with some data.

## How to Use

1. Install Docker and Python 3.7+ on your local machine.
2. Clone this repository: `git clone https://github.com/yourusername/fastapi-docker-app.git`.
3. Navigate to the project directory: `cd fastapi-docker-app`.
4. Build the Docker images: `docker-compose build`.
5. Start the application and web front-end containers: `docker-compose up`.
6. Open a web browser and navigate to `http://localhost:8080` to access the web front-end. You can also access the API endpoints directly by visiting `http://localhost:8000/api/` and `http://localhost:8000/api/items/42?q=test`.

## Credits

This project was created by [Joel Fourhman](https://github.com/joelfourhman) with advice and help from [Johnny Irvin](https://github.com/johnnyirvin). 
If you have any questions or suggestions, feel free to create an issue or pull request on GitHub.
