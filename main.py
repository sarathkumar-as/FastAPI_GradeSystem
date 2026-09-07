"""A beginner-friendly FastAPI project with two GET endpoints."""

# Import the FastAPI class from the installed fastapi package.
from fastapi import FastAPI


# Create the FastAPI application object.
# This information appears in the automatic API documentation.
app = FastAPI(
    title="My First FastAPI Project",
    description="A basic API containing welcome and greeting endpoints.",
    version="1.0.0",
)


# Create a GET endpoint for:
# http://127.0.0.1:8000/
@app.get("/")
def read_root():
    """Return a welcome message confirming that the API is running."""

    # FastAPI automatically converts this dictionary into JSON.
    return {
        "message": "Hello, FastAPI!",
        "status": "The API is working successfully.",
    }


# Create a GET endpoint with a path parameter called "name".
# Example: http://127.0.0.1:8000/greet/Sarath
@app.get("/greet/{name}")
def greet_user(name: str):
    """Return a personalized greeting using the name from the URL."""

    # The f-string places the supplied name inside the message.
    return {
        "name": name,
        "message": f"Hello, {name}! Welcome to my FastAPI project.",
    }