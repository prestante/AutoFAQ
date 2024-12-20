import pytest
from playwright.async_api import async_playwright

@pytest.fixture(scope="session")
async def playwright():
    async with async_playwright() as p:
        yield p

@pytest.fixture(scope="session")
async def browser(playwright):
    browser = await playwright.chromium.launch(headless=False)  # headless=False для видимого выполнения
    yield browser
    await browser.close()

@pytest.fixture(scope="function")
async def page(browser):
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()