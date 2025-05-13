# Project Name: Sauce Demo Test Automation


## Description


This projects represents automated test for web-app Sauce Demo using Python and Selenium. In tests are including functionality of login page, adding a product to cart, filtering etc


## Technology Stack

-Python 3.11

-Selenium

-pytest

-WebDriver Manager

## Installation

1. Clone repository:

    '''bash
    git clone https://github.com/nnoir/Sauce-Demo-Test-Automation.git

2. Go to Project Directory

    cd sauce_demo_test_automation

3. Download requirements:

    pip install -r requirements.txt

4. Tests start:

   pytest

if u want to start specific test:

    pytest -k "test_sort_by_lower_price"

## Project Structure

test/: Directory with tests

pages/: Directory with pages (Pages Object Model)

conftest.py: Settings and fixtures for pytest

requirements.txt: Dependencies list

## Dependencies

    Selenium
    WebDriver Manager
    pytest