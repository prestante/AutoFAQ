from tests.frontend.pages.base_page import BasePage
from tests.frontend.custom_selectors.chat_selectors import (
    chat_button_selector,
    message_input_selector,
    send_button_selector,
    chat_message_selector,
    chat_header_selector
)

class ChatPage(BasePage):
    async def click_chat_button(self):
        await self.page.click(chat_button_selector)

    async def is_chat_open(self):
        return await self.page.is_visible(message_input_selector)

    async def type_message(self, message):
        await self.page.fill(message_input_selector, message)

    async def send_message(self):
        await self.page.click(send_button_selector)

    async def please_wait(self, milliseconds=500):
        await self.page.wait_for_timeout(milliseconds)

    async def get_chat_messages(self):
        return await self.page.query_selector_all(chat_message_selector)

    async def get_chat_header_background_color(self):
        return await self.page.evaluate(
            """(selector) => {
                const element = document.querySelector(selector);
                return getComputedStyle(element).backgroundColor;
            }""",
            chat_header_selector
        )