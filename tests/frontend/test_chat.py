import pytest
from pages.chat_page import ChatPage
from time import sleep

@pytest.mark.frontend
def test_open_chat(page):
    chat_page = ChatPage(page)
    chat_page.goto("https://autofaq.ai")
    print(chat_page.return_url())

#     sleep(2)

    # Click to open the chat widget
    # await chat_page.open_chat()

    # Assert that the chat is open
    # assert await page.is_visible("#chat21-main-message-context")