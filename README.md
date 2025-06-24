# MCP Project

## Continuous Integration

This project uses GitHub Actions for continuous integration to ensure code quality. The CI pipeline runs automatically on pull requests to the `main` branch.

### CI Workflow

The CI workflow performs the following checks:

1. **Linting with Pylint**: Checks code style and quality using Pylint
2. **Type Checking with Mypy**: Verifies type annotations using Mypy

### Running Checks Locally

To run the same checks locally before submitting a pull request:

1. Install the required development dependencies:
   ```bash
   pip install pylint mypy types-requests
   ```

2. Run Pylint:
   ```bash
   pylint --rcfile=.pylintrc *.py
   ```

3. Run Mypy:
   ```bash
   mypy --config-file mypy.ini *.py
   ```

## Configuration Files

- `.github/workflows/python-ci.yml`: GitHub Actions workflow configuration
- `.pylintrc`: Pylint configuration
- `mypy.ini`: Mypy configuration

## Project Dependencies

See `requirements.txt` for the list of project dependencies.