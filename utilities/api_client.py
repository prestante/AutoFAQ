# import requests
# import json

# class ApiClient:
#     BASE_URL = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"

#     def send_message(self, message):
#         headers = {
#             "Content-Type": "application/json",
#             "Accept": "application/json"
#         }
#         payload = {
#             "message": message
#         }
#         response = requests.post(self.BASE_URL, headers=headers, data=json.dumps(payload))
#         return response

#     def send_empty_request(self):
#         headers = {
#             "Content-Type": "application/json",
#             "Accept": "application/json"
#         }
#         response = requests.post(self.BASE_URL, headers=headers, data="{}")
#         return response