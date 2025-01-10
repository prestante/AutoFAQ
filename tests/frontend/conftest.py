import pytest_asyncio
import allure
from time import sleep
from playwright.async_api import async_playwright
from tests.frontend.pages.chat_page import ChatPage

@pytest_asyncio.fixture(scope="function")
async def my_playwright():
    async with async_playwright() as p:
        yield p

@pytest_asyncio.fixture(scope="function")
async def my_browser(my_playwright):
    browser = await my_playwright.chromium.launch(headless=False)
    yield browser
    await browser.close()

@pytest_asyncio.fixture(scope="function")
async def my_page(my_browser):
    context = await my_browser.new_context(record_video_dir="allure-results/")
    my_page = await context.new_page()
    yield my_page
    await context.close()

@pytest_asyncio.fixture(scope="function")
async def chat_page(my_page):
    chat_page = ChatPage(my_page)
    await chat_page.goto("https://autofaq.ai")
    await chat_page.click_chat_button()
    return chat_page

# # Фикстура для автоматического добавления скришнота и видеозаписи в allure при возникновении ошибки
# @pytest.fixture(scope="function", autouse=True)
# def add_screenshot_and_video_on_failure(my_page, request):
#     yield
#     if request.node.rep_call.failed:
#         my_page.screenshot(path="allure-results/screenshot.png")
#         allure.attach.file("allure-results/screenshot.png", attachment_type=allure.attachment_type.PNG)
#         my_page.close()
#         sleep(1)  # Для того, чтобы видео успело сохраниться
#         allure.attach.file(my_page.video.path(), attachment_type=allure.attachment_type.WEBM)