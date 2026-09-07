# Student Grade API

A beginner-friendly FastAPI project that returns greetings and converts a student's mark into a letter grade.

## Grade rules

| Mark | Grade |
|---|---|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| 0-59 | E |

## Windows setup

Open the project folder in VS Code, select **Terminal > New Terminal**, and run:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Test in the browser

- Welcome: <http://127.0.0.1:8000/>
- Greeting: <http://127.0.0.1:8000/greet/Sarath>
- Grade: <http://127.0.0.1:8000/grade/Sarath%20Kumar?mark=85>
- Interactive documentation: <http://127.0.0.1:8000/docs>

Press `Ctrl+C` in the terminal to stop the server. Then run `deactivate` to leave the virtual environment.

## Expected grade response

```json
{
  "student_name": "Sarath Kumar",
  "mark": 85,
  "grade": "B",
  "message": "Sarath Kumar scored 85 and received grade B."
}
```

## Validation

- A name accepts English letters and spaces only.
- A mark must be a whole number from 0 through 100.
- Invalid input produces a clear JSON error response.

