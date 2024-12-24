import pytest
import allure
from time import sleep
from playwright.sync_api import sync_playwright
from pages.chat_page import ChatPage

@pytest.fixture(scope="function")
def my_playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def my_browser(my_playwright):
    browser = my_playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def my_page(my_browser):
    context = my_browser.new_context(record_video_dir="allure-results/")
    my_page = context.new_page()
    yield my_page
    context.close()

# Фикстура для перехода на страницу и открытия окна чата
@pytest.fixture(scope="function")
def chat_page(my_page):
    chat_page = ChatPage(my_page)
    chat_page.goto("https://autofaq.ai")
    chat_page.click_chat_button()
    return chat_page

# Фикстура для автоматического добавления скришнота и видеозаписи в allure при возникновении ошибки
@pytest.fixture(scope="function", autouse=True)
def add_screenshot_and_video_on_failure(my_page, request):
    yield
    if request.node.rep_call.failed:
        my_page.screenshot(path="allure-results/screenshot.png")
        allure.attach.file("allure-results/screenshot.png", attachment_type=allure.attachment_type.PNG)
        my_page.close()
        sleep(1)  # Для того, чтобы видео успело сохраниться
        allure.attach.file(my_page.video.path(), attachment_type=allure.attachment_type.WEBM)