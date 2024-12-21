import pytest
from pages.chat_page import ChatPage

# Фикстура для перехода на страницу и открытия окна чата
@pytest.fixture(scope="function")
def chat_page(my_page):
    chat_page = ChatPage(my_page)
    chat_page.goto("https://autofaq.ai")
    chat_page.click_chat_button()
    return chat_page

@pytest.mark.frontend
def test_open_chat(chat_page):
    assert chat_page.is_chat_open(), "Чат не открыт"

@pytest.mark.frontend
def test_send_message(chat_page):
    my_message = 'Привет, бот!'
    
    chat_page.type_message(my_message)
    chat_page.wait_a_second(500)
    chat_page.send_message()
    chat_page.wait_a_second(500)
    
    messages = chat_page.get_chat_messages()
    assert my_message == messages[-1].text_content(), \
        f"Ожидаем '{my_message}' в качестве последнего сообщения. Получили '{messages[-1].text_content()}'"  # Проверка, что последнее сообщение равно отправленному

@pytest.mark.frontend
def test_send_multiple_messages(chat_page):
    my_messages = ['Привет, бот!', 'Как дела?', 'Что нового?']
    
    for message in my_messages:
        chat_page.type_message(message)
        chat_page.wait_a_second(500)
        chat_page.send_message()
        chat_page.wait_a_second()

    messages = chat_page.get_chat_messages()
    for message in my_messages:
        assert message in [m.text_content() for m in messages], \
            f"Ожидаем '{message}' в сообщениях. Получили '{[m.text_content() for m in messages]}'"

@pytest.mark.frontend
def test_close_chat(chat_page):
    chat_page.click_chat_button()
    assert not chat_page.is_chat_open(), "Чат не закрыт"