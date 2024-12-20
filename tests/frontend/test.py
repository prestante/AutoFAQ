import pytest
from playwright.async_api import async_playwright

chat_button_selector = "#chat21-launcher-button"
message_input_selector = "#chat21-main-message-context"
send_button_selector = "#chat21-button-send"
chat_message_selector = "span.msg_content.SanitizedHtml"

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


class BasePage:
    def __init__(self, page):
        self.page = page

    async def goto(self, url):
        await self.page.goto(url)

    async def get_current_url(self):
        return self.page.url  # Retrieve the current URL


class ChatPage(BasePage):
    async def open_chat(self):
        await self.page.click(chat_button_selector)

    async def send_message(self, message):
        await self.page.fill(message_input_selector, message)
        await self.page.click(send_button_selector)

    async def get_last_message(self):
        return await self.page.inner_text(chat_message_selector)


# def test_print_current_url(page):
#     chat_page = ChatPage(page)
#     chat_page.goto("http://saucedemo.com")
#     print(f"------{chat_page.get_current_url()}======")

def test_print_current_url(page):
    chat_page = ChatPage(page)
    chat_page.goto("http://saucedemo.com")
    current_url = chat_page.get_current_url()  # Call the new method
    print(current_url)