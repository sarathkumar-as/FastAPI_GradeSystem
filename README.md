# My First FastAPI Project

A beginner-friendly FastAPI project containing a welcome endpoint and a personalized greeting endpoint.

## Features

- `GET /` returns a welcome message.
- `GET /greet/{name}` returns a personalized greeting.
- Automatic interactive documentation is available at `/docs`.

## Setup and run

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open these URLs in a browser:

- Application: <http://127.0.0.1:8000/>
- Greeting example: <http://127.0.0.1:8000/greet/Sarath>
- Interactive API documentation: <http://127.0.0.1:8000/docs>

Press `Ctrl+C` in the terminal to stop the server.
