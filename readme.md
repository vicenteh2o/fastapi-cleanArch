## Installation

1. Clone the repository:

```bash
git clone https://github.com/vicenteh2o/fastapi-cleanArch.git
cd fastapi-cleanArch
```

2. Install all dependencies:

- python3 -m venv venv (This creates a folder named venv/ containing an isolated Python environment.)
- source venv/bin/activate (This activates the virtual environment.)

```bash
pip3 install -r requirements-dev.txt
pip3 install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
python3 -m uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Testing

### Automated Testing with pytest

The project supports automated testing using pytest and httpx. Create test files to test your API endpoints:

```bash
# Run all tests
python3 -m pytest

# Run tests with verbose output
python3 -m pytest -v

# Run specific test file
python3 -m pytest test_main.py
```

## Development

### Project Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications

### Testing Dependencies

- **pytest**: Testing framework for Python applications
- **httpx**: Async HTTP client for testing FastAPI applications

### Code Quality Dependencies

- **ruff**: Fast Python linter and code formatter (replaces flake8, black, isort, and more)

### Local Development

```bash
# Install in development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Setting Up Pre-commit Hook

To ensure code quality and run tests automatically
before each commit and include Ruff linting, you can set up a pre-commit hook:

1. Create the pre-commit hook file:

```bash
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
echo "🔍 Running FastAPI tests with pytest..."
pytest --maxfail=1 --disable-warnings -q
RESULT=$?

if [ $RESULT -ne 0 ]; then
  echo "❌ Tests failed. Commit aborted."
  exit 1
fi
echo "✅ All tests passed!"

echo "🔍 Running Ruff lint check..."
ruff check .
if [ $? -ne 0 ]; then
    echo "❌ Ruff check failed. Fix issues before committing."
    exit 1
fi
echo "✅ Ruff check passed!"
EOF
```

2. Make the pre-commit hook executable:

```bash
chmod +x .git/hooks/pre-commit
```

Now, every time you commit changes, the hook will automatically run your tests. If any tests fail, the commit will be prevented, ensuring that only working code is committed to the repository.

## Production Environment & CI/CD

### GitHub Actions Workflow

For team or production environments, you'll want to add automated code quality checks and tests to CI tools such as GitHub Actions. Create `.github/workflows/ci.yml`:

```yaml
name: FastAPI CI/CD Pipeline

on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Ruff Linting
        run: |
          echo "🔍 Running Ruff code quality checks..."
          python3 -m ruff check .

      - name: Run Ruff Formatting Check
        run: |
          echo "🎨 Checking code formatting with Ruff..."
          python3 -m ruff format --check .

      - name: Run Tests
        run: |
          echo "🧪 Running FastAPI tests with pytest..."
          python3 -m pytest --maxfail=1 --disable-warnings -q
```

### Code Quality Tools

The project uses **Ruff** for fast Python linting and formatting:

```bash
# Check for linting issues
python3 -m ruff check .

# Fix auto-fixable issues
python3 -m ruff check . --fix

# Format code
python3 -m ruff format .

# Check formatting without changing files
python3 -m ruff format --check .
```
