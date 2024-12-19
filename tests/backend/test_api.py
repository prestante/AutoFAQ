import pytest
import requests
import uuid

BASE_URL = "https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3/messages"

@pytest.mark.asyncio
async def test_post_and_verify_message():
    session_id = str(uuid.uuid4())
    headers = {
        "Cookie": f"session-id={session_id}"
    }
    message_data = {
        "message": '{"id": "Some id", "ts": 0, "text": "Test message"}'
    }

    # Отправка POST-запроса
    post_response = requests.post(BASE_URL, headers=headers, files=message_data)
    assert post_response.status_code == 200

    # Верификация через GET-запрос
    get_response = requests.get(BASE_URL, headers=headers)
    assert get_response.status_code == 200
    messages = get_response.json()
    assert any(msg["text"] == "Test message" for msg in messages)

def test_just_post_message():
    session_id = str(uuid.uuid4())
    headers = {
        "Cookie": f"session-id={session_id}"
    }
    message_data = {
        "message": '{"id": "Some id", "ts": 0, "text": "Some text"}'
    }

    response = requests.post(BASE_URL, headers=headers, files=message_data)
    
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["id"] == "Some id"
    assert response_body["text"] == "Some text"
    assert response_body["sessionId"] == session_id

def test_just_get_messages():
    session_id = str(uuid.uuid4())
    headers = {
        "Cookie": f"session-id={session_id}"
    }

    response = requests.get(BASE_URL, headers=headers)
    
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)

def test_post_message_without_body():
    session_id = str(uuid.uuid4())
    headers = {
        "Cookie": f"session-id={session_id}"
    }

    response = requests.post(BASE_URL, headers=headers)
    
    assert response.status_code == 200, 'Намеренная ошибка'