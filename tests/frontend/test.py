import pytest
from playwright.sync_api import sync_playwright

chat_button_selector = "#chat21-launcher-button"
message_input_selector = "#chat21-main-message-context"
send_button_selector = "#chat21-button-send"
chat_message_selector = "span.msg_content.SanitizedHtml"

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)  # headless=False для видимого выполнения
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url


class ChatPage(BasePage):
    def open_chat(self):
        self.page.click(chat_button_selector)

    def send_message(self, message):
        self.page.fill(message_input_selector, message)
        self.page.click(send_button_selector)

    def get_last_message(self):
        return self.page.inner_text(chat_message_selector)


# def test_print_current_url(page):
#     chat_page = ChatPage(page)
#     chat_page.goto("http://saucedemo.com")
#     current_url = chat_page.get_current_url()
#     print(current_url)

def test_open_chat(page):
    chat_page = ChatPage(page)
    # print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
    chat_page.goto("https://autofaq.ai")