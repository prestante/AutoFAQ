import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def my_playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def my_browser(my_playwright):
    browser = my_playwright.chromium.launch(headless=True)  # headless=False для видимого выполнения
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def my_page(my_browser):
    context = my_browser.new_context()
    my_page = context.new_page()
    yield my_page
    context.close()