import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

if os.getenv("IS_DOCKER"):
    load_dotenv(".env.docker")
else:
    load_dotenv(".env.local")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # No webdriver-manager
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()