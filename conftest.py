import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def config():
    """Configuration fixture"""
    return {
        'base_url': os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com'),
        'ui_base_url': os.getenv('UI_BASE_URL', 'https://example.com'),
        'browser': os.getenv('BROWSER', 'chrome'),
        'headless': os.getenv('HEADLESS', 'false').lower() == 'true',
        'timeout': int(os.getenv('TIMEOUT', '30'))
    }

@pytest.fixture(scope="session")
def driver(config):
    """WebDriver fixture"""
    browser = config['browser'].lower()
    headless = config['headless']

    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config['timeout'])
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def api_session():
    """Requests session fixture for API tests"""
    import requests
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    })
    yield session
    session.close()