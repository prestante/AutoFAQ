import pytest

@pytest.mark.frontend
def test_open_chat(chat_page):
    assert chat_page.is_chat_open(), "Чат не открыт"

@pytest.mark.frontend
def test_send_message(chat_page):
    my_message = 'Привет, бот!'
    
    chat_page.type_message(my_message)
    chat_page.please_wait()
    chat_page.send_message()
    chat_page.please_wait()
    
    messages = chat_page.get_chat_messages()
    assert my_message == messages[-1].text_content(), \
        f"Ожидаем '{my_message}' в качестве последнего сообщения. Получили '{messages[-1].text_content()}'"  # Проверка, что последнее сообщение равно отправленному

@pytest.mark.frontend
def test_send_multiple_messages(chat_page):
    my_messages = ['Привет, бот!', 'Как дела?', 'Что нового?']
    
    for message in my_messages:
        chat_page.type_message(message)
        chat_page.please_wait()
        chat_page.send_message()
        chat_page.please_wait(1000)

    messages = chat_page.get_chat_messages()
    for message in my_messages:
        assert message in [m.text_content() for m in messages], \
            f"Ожидаем '{message}' в сообщениях. Получили '{[m.text_content() for m in messages]}'"

@pytest.mark.frontend
def test_chat_header_background_color(chat_page):
    background_color = chat_page.get_chat_header_background_color()
    assert background_color == "rgb(24, 55, 217)", \
        f"Намеренно неожиданный цвет фона заголовка окна чата: {background_color}"

@pytest.mark.frontend
def test_close_chat(chat_page):
    chat_page.click_chat_button()
    assert not chat_page.is_chat_open(), "Чат не закрыт"