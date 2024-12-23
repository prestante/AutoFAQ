from pages.base_page import BasePage
from custom_selectors.chat_selectors import (
    chat_button_selector,
    message_input_selector,
    send_button_selector,
    chat_message_selector,
    chat_header_selector
)

class ChatPage(BasePage):
    def click_chat_button(self):
        self.page.click(chat_button_selector)

    def is_chat_open(self):
        return self.page.is_visible(message_input_selector)

    def type_message(self, message):
        self.page.fill(message_input_selector, message)
        
    def send_message(self):
        self.page.click(send_button_selector)

    def wait_a_second(self, milliseconds=1000):
        self.page.wait_for_timeout(milliseconds)

    def get_chat_messages(self):
        return self.page.query_selector_all(chat_message_selector)
    
    def get_chat_header_background_color(self):
        return self.page.evaluate(
            """(selector) => {
                const element = document.querySelector(selector);
                return getComputedStyle(element).backgroundColor;
            }""",
            chat_header_selector
        )