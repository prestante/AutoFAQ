from pages.base_page import BasePage
from custom_selectors.chat_selectors import (
    chat_button_selector,
    message_input_selector,
    send_button_selector,
    chat_message_selector
)

class ChatPage(BasePage):
    async def open_chat(self):
        await self.page.click(chat_button_selector)

    async def send_message(self, message):
        await self.page.fill(message_input_selector, message)
        await self.page.click(send_button_selector)

    async def get_last_message(self):
        return await self.page.inner_text(chat_message_selector)
    
    async def return_url(self):
        return await self.page.url