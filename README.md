# Pytest Test Framework with Testomatio Integration

An example test automation framework using pytest with integrated reporting to Testomatio.io for both UI and API testing.

## Features

- **API Testing**: RESTful API tests using requests library
- **UI Testing**: Web UI tests using Selenium WebDriver
- **Testomatio Integration**: Automatic test reporting and synchronization
- **Configurable Environment**: Environment-based configuration using .env files
- **Parallel Execution**: Support for parallel test execution
- **HTML Reports**: Built-in HTML reporting with pytest-html

## Project Structure

```
pytest_test_fw/
├── tests/
│   ├── api/                    # API test cases
│   │   ├── test_jsonplaceholder_api.py
│   │   └── test_users_api.py
│   ├── ui/                     # UI test cases
│   │   └── test_example_ui.py
│   └── conftest.py            # Pytest configuration and fixtures
├── utils/
│   ├── api_client.py          # API client helper
│   └── ui_helpers.py          # UI testing helpers
├── scripts/
│   ├── run_tests.py           # Test execution script
│   └── testomatio_sync.sh     # Testomatio sync script
├── requirements.txt           # Python dependencies
├── pytest.ini               # Pytest configuration
├── .env.example             # Environment variables template
└── README.md               # This file
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configuration

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` file with your settings:
```env
# Testomatio Configuration
TESTOMATIO=your_testomatio_token_here
TESTOMATIO_RUN=Example Test Run
TESTOMATIO_ENV=staging
TESTOMATIO_LABELS=automated,pytest

# Test Configuration
BASE_URL=https://jsonplaceholder.typicode.com
UI_BASE_URL=https://example.com
BROWSER=chrome
HEADLESS=false
TIMEOUT=30
```

### 3. WebDriver Setup

For UI tests, ensure you have the appropriate WebDriver installed:

- **Chrome**: Download ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/)
- **Firefox**: Download GeckoDriver from [GitHub releases](https://github.com/mozilla/geckodriver/releases)

## Usage

### Running Tests

#### Basic test execution:
```bash
# Run all tests
pytest

# Run API tests only
pytest tests/api/

# Run UI tests only
pytest tests/ui/

# Run tests with specific marker
pytest -m smoke
pytest -m regression
```

#### Using the test runner script:
```bash
# Run all tests with Testomatio reporting
python scripts/run_tests.py --report

# Run API tests with sync to Testomatio
python scripts/run_tests.py --suite api --sync

# Run smoke tests only
python scripts/run_tests.py --marker smoke --report
```

### Testomatio Integration

#### Sync tests to Testomatio:
```bash
pytest --testomatio sync
```

#### Report test results:
```bash
pytest --testomatio report
```

#### Remove Testomatio IDs from tests:
```bash
pytest --testomatio remove
```

#### Debug mode:
```bash
pytest --testomatio debug
```

### Test Markers

The framework uses the following pytest markers:

- `@mark.api`: API tests
- `@mark.ui`: UI tests
- `@mark.smoke`: Smoke tests
- `@mark.regression`: Regression tests
- `@mark.testomatio('@T12345678')`: Testomatio test ID

## Test Examples

### API Test Example

```python
@mark.api
def test_get_all_posts(self, api_client):
    """Test getting all posts"""
    response = api_client.get('/posts')

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100
```

### UI Test Example

```python
@mark.ui
def test_example_com_title(self, driver, config):
    """Test that example.com has correct title"""
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
```

## Continuous Integration

### GitHub Actions Example

```yaml
name: Test Execution

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests with Testomatio reporting
      env:
        TESTOMATIO: ${{ secrets.TESTOMATIO }}
        HEADLESS: true
      run: |
        pytest --testomatio report
```

## Troubleshooting

### Common Issues

1. **WebDriver not found**: Ensure ChromeDriver/GeckoDriver is in your PATH
2. **Testomatio token error**: Check your TESTOMATIO environment variable
3. **Import errors**: Verify all dependencies are installed correctly

### Debug Mode

Run tests in debug mode to see detailed Testomatio integration logs:
```bash
pytest --testomatio debug -v
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License.