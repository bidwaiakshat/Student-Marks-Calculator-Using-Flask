# Student Marks Calculator

## Project Description
A simple web application built using Python and Flask that accepts student marks and calculates the total, percentage, and pass/fail result.

## Features
- Student name input
- Marks entry for five subjects
- Input validation
- Total marks calculation
- Percentage calculation
- Pass/fail result
- Error messages for invalid inputs

## Technologies Used
- Python
- Flask
- HTML

## Project Structure
```text
my_flask_project/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    ├── index.html
    ├── result.html
    └── about.html
```

## Installation

1. Install Python.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   `python -m venv .venv`

4. Activate the environment on Windows:

   `.venv\Scripts\activate`

5. Install dependencies:

   `python -m pip install -r requirements.txt`

## How to Run

Execute:

`python app.py`

Open the local address displayed in the terminal, usually `http://127.0.0.1:5000`.

## Calculation Rules
- Each subject is marked out of 100.
- Total marks are the sum of all three subjects.
- Percentage is the total divided by 5.
- A student passes if they score at least 40 in every subject.

## Testing
Test valid marks, empty fields, negative marks, marks above 100, and non-numeric input.