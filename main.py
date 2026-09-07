"""Beginner FastAPI project: greeting and student grade API."""

import re

from fastapi import FastAPI, HTTPException, Path, Query


# Create the FastAPI application.
app = FastAPI(
    title="Student Grade API",
    description="A beginner API for greetings and student grade calculation.",
    version="1.0.0",
)


def validate_student_name(name: str) -> str:
    """Return a cleaned name or raise an error when it is invalid."""
    cleaned_name = " ".join(name.strip().split())

    if not cleaned_name:
        raise HTTPException(status_code=400, detail="Student name cannot be empty.")

    if not re.fullmatch(r"[A-Za-z ]+", cleaned_name):
        raise HTTPException(
            status_code=400,
            detail="Student name must contain only letters and spaces.",
        )

    return cleaned_name


def calculate_grade(mark: int) -> str:
    """Convert a mark from 0 to 100 into a letter grade."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


@app.get("/", summary="Show the welcome message")
def read_root() -> dict[str, str]:
    """Return a simple JSON welcome message."""
    return {"message": "Hello, FastAPI! Welcome to the Student Grade API."}


@app.get("/greet/{name}", summary="Greet a person by name")
def greet_person(
    name: str = Path(..., description="Name containing only letters and spaces"),
) -> dict[str, str]:
    """Return a personalized greeting."""
    valid_name = validate_student_name(name)
    return {"message": f"Hello, {valid_name}!"}


@app.get("/grade/{student_name}", summary="Calculate a student's grade")
def get_student_grade(
    student_name: str = Path(
        ...,
        description="Student name containing only letters and spaces",
    ),
    mark: int = Query(
        ...,
        ge=0,
        le=100,
        description="Whole-number mark from 0 to 100",
    ),
) -> dict[str, str | int]:
    """Validate a student and return the grade for the supplied mark."""
    valid_name = validate_student_name(student_name)
    grade = calculate_grade(mark)

    return {
        "student_name": valid_name,
        "mark": mark,
        "grade": grade,
        "message": f"{valid_name} scored {mark} and received grade {grade}.",
    }

