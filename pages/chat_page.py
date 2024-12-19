from .base_page import BasePage
from ..selectors.chat_selectors import *

class ChatPage(BasePage):
    async def open_chat(self):
        await self.page.click(chat_button_selector)

    async def send_message(self, message):
        await self.page.fill(message_input_selector, message)
        await self.page.click(send_button_selector)

    async def get_last_message(self):
        return await self.page.inner_text(chat_message_selector)