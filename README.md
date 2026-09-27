# CASEFILE

A command-line detective game written in Python.

Create a detective account, pick an open case, look through the suspects, evidence and witness statements, then name the culprit. Your result is saved to a file.

## Requirements

- Python 3
- No extra packages. CASEFILE uses only the standard library.

## How to run

From the project folder:

```bash
python main.py
```

## How to play

1. Register a detective account, then log in.
2. View the list of open cases and select one.
3. Investigate the case by looking at the suspects, the evidence and the witness statements.
4. Submit your theory by naming the culprit.
5. Your result is saved to `data/records.json`.

## Running the tests

```bash
python3 -m unittest tests.test_cases tests.test_investigation
```

There are 5 tests, all written with Python's built-in `unittest`.

## Project structure

```
main.py                  starts the game
src/
  app.py                 main menu loop
  authentication.py      register / login
  cases.py               list and select cases
  investigation.py       investigation menu
  data_manager.py        all JSON reading and writing
  models.py              classes
  exceptions.py          custom exceptions
data/
  cases.json             case content
  users.json             registered detectives
  records.json           theory submissions
tests/
  test_cases.py
  test_investigation.py
```

## Future improvements

- Hash passwords instead of storing them as plain text
- Add tests that check what functions do, not just the data
- Use the model classes everywhere instead of passing raw dictionaries