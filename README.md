# Test Repository

A test repository for validating the **Coding Agent** project.

This repo contains sample code with intentional issues (bugs, missing tests, style problems) that the Coding Agent can practice resolving via GitHub issues.

## Structure

```
├── src/
│   ├── calculator.py      # Basic calculator with a bug
│   ├── string_utils.py    # String utilities (missing edge case handling)
│   └── data_processor.py  # Data processing module
├── tests/
│   ├── test_calculator.py
│   ├── test_string_utils.py
│   └── test_data_processor.py
├── requirements.txt
└── README.md
```

## Sample Issues to Create

1. **Bug**: `calculator.py` — division method doesn't handle division by zero
2. **Bug**: `string_utils.py` — `reverse_words` fails on empty strings
3. **Feature**: Add a `power` method to the calculator
4. **Test**: Improve test coverage for `data_processor.py`
5. **Refactor**: Add type hints throughout the codebase

## Running Tests

```bash
pip install -r requirements.txt
pytest tests/ -v
```
