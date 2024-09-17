import requests
import allure
import data

@allure.step('Отправляем запрос на создание пользователя')
def create_user(payload):
    response = requests.post(data.CREATE_USER_URL, json=payload)
    if response.status_code != 201 and not response.json().get("success", False):
        raise Exception(f"Failed to create user: {response.text}")
    return response

@allure.step('Отправляем запрос на удаление пользователя')
def delete_user(token):
    response = requests.delete(data.REMOVE_USER_URL, headers={"Authorization": token})
    if response.status_code not in (200, 204) and not response.json().get("success", False):
        raise Exception(f"Failed to delete user: {response.text}")
    return response
