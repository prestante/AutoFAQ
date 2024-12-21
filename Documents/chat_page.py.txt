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

    def send_message(self, message):
        self.page.fill(message_input_selector, message)
        self.page.click(send_button_selector)

    def get_last_message(self):
        return self.page.inner_text(chat_message_selector)