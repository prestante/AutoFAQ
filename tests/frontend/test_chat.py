import pytest
from pages.chat_page import ChatPage
from time import sleep

# Фикстура для перехода на страницу и открытия окна чата
@pytest.fixture(scope="function")
def chat_page(my_page):
    chat_page = ChatPage(my_page)
    chat_page.goto("https://autofaq.ai")
    chat_page.open_chat()
    return chat_page

@pytest.mark.frontend
def test_open_chat(chat_page):
    assert chat_page.is_chat_open(), "Чат не открыт"

@pytest.mark.frontend
def test_send_message(chat_page):
    chat_page.send_message("Привет, бот!")
    sleep(5)