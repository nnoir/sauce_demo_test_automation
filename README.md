# Project Name: Sauce Demo Test Automation


## Description


This projects represents automated test for web-app Sauce Demo using Python and Selenium. In tests are including functionality of login page, adding a product to cart, filtering etc


## Technology Stack

-Python 3.11

-Selenium

-pytest

-WebDriver Manager

-Docker (for containerized execution)

-Pytest-xdist (parallel test execution)

-SQL (for test data)

## Installation

1. Clone repository:


    git clone https://github.com/nnoir/Sauce-Demo-Test-Automation.git

2. Go to Project Directory


    cd sauce_demo_test_automation

3. Download requirements(Windows):


    pip install -e .

3. Dowload requirements(Docker):
   

    docker-compose up --build --abort-on-container-exit


4. Tests start:
   ```
   .\venv\Scripts\Activate.ps1
   ```

   ```
   pytest
   ```

if u want to start specific test:

    pytest -k "test_sort_by_lower_price"

if iu want to start all test in parallel(auto = CPU core count):

    pytest -n auto

## Project Structure

test/: Directory with tests

pages/: Directory with pages (Pages Object Model)

conftest.py: Settings and fixtures for pytest

## Notes
The project supports both local and Dockerized execution.

Environment-specific variables are loaded using python-dotenv.

You can control which environment file to load using ENV_FILE:


    ENV_FILE=.env.local pytest