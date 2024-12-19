import pytest
from pages.chat_page import ChatPage

@pytest.mark.frontend
async def test_open_chat(page):
    chat_page = ChatPage(page)
    await chat_page.goto("https://autofaq.ai")

    # Click to open the chat widget
    await chat_page.open_chat()

    # Assert that the chat is open
    assert await page.is_visible("#chat21-main-message-context")