from pages.base_page import BasePage
from custom_selectors.chat_selectors import (
    chat_button_selector,
    message_input_selector,
    send_button_selector,
    chat_message_selector
)

class ChatPage(BasePage):
    def open_chat(self):
        self.page.click(chat_button_selector)

    def is_chat_open(self):
        return self.page.is_visible(message_input_selector)

    def send_message(self, message):
        self.page.fill(message_input_selector, message)  # Вводим текст в поле ввода
        self.page.wait_for_timeout(500)  # Даем странице время на обработку введенного текста
        self.page.click(send_button_selector)  # Отправляем сообщение

    def get_last_message(self):
        return self.page.inner_text(chat_message_selector)