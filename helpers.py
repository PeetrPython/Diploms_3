import string
import random
import api


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email(length):
    return generate_random_string(length) + '@yandex.ru'


def generate_random_field(field, length):
    if field == 'email':
        return generate_random_email(length)
    return generate_random_string(length)


def generate_new_user_credentials(empty_field=None):
    email = generate_random_email(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    credentials = {
        "email": email,
        "password": password,
        "name": name
    }
    if empty_field:
        credentials[empty_field] = ""
    return credentials


def create_user(credentials):
    response = api.create_user(credentials)

    response_payload = response.json()
    if not response_payload.get('success', False):
        raise Exception(f"Failed to create user: {response.text}")

    credentials['accessToken'] = response_payload['accessToken']
    return credentials


def delete_user(credentials):
    api.delete_user(credentials['accessToken'])
