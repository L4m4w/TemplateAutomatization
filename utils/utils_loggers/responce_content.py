import requests
import allure
import json

def response_body(response):
    content_type = response.headers.get('Content-Type')

    if content_type:
        # Проверка типа содержимого
        if 'application/json' in content_type:
            response_json = response.json()
            allure.attach(
                body=json.dumps(response_json, indent=4),
                name="Response Body (JSON)",
                attachment_type=allure.attachment_type.JSON,
                extension='json'
            )
        elif 'text/html' in content_type:
            response_text = response.text
            allure.attach(
                body=response_text,
                name="Response Body (HTML)",
                attachment_type=allure.attachment_type.TEXT,
                extension='html'
            )
        elif 'application/xml' in content_type:
            response_text = response.text
            allure.attach(
                body=response_text,
                name="Response Body (XML)",
                attachment_type=allure.attachment_type.XML,
                extension='xml'
            )
        else:
            response_text = response.text
            allure.attach(
                body=response_text,
                name="Response Body (Unknown)",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
    else:
        print("Content-Type не найден")