import requests

base_url = f'https://petstore.swagger.io/v2'
headers = {'accept': 'application/json'}


def create_user(username: str):
    new_user = {
        "id": 0,
        "username": username,
        "firstName": "James",
        "lastName": "Bond",
        "email": "qw@www.ru",
        "password": "123",
        "phone": "+79876543210",
        "userStatus": 1
    }

    resp = requests.post(base_url + '/user', json=new_user)

    if resp.status_code == 200:
        uid = resp.json()['message']
        print(f'Пользователь {username} успешно создан (id = {uid})')
        print(f'Содержимое ответа:\n'
              f'{resp.json()}')
    else:
        print('Произошла ошибка при создании пользователя')
        print(f'Содержимое ответа сервера:\n'
              f'{resp.json()}')
        uid = 0

    return uid


def get_user(username: str):
    print('\nИщем пользователя в базе...')
    resp = requests.get(base_url + f'/user/{username}', headers=headers)
    if resp.status_code == 200:
        print(f'Пользователь {username} найден. Содержимое ответа:\n'
              f'{resp.json()}\n')
    elif resp.status_code == 400:
        print('Не верно указано имя пользователя')
    elif resp.status_code == 404:
        print(f'Пользователь {username} не найден')


def update_user(username: str):
    new_user = {
        "id": 0,
        "username": username,
        "firstName": "Jamesy",
        "lastName": "Bondy",
        "email": "qw@www.ru",
        "password": "123",
        "phone": "+79876543210",
        "userStatus": 1
    }

    resp = requests.put(base_url + f'/user/{username}', headers=headers, json=new_user)

    if resp.status_code == 200:
        print(f'Обновление выполнено успешно! Содержимое ответа:\n'
              f'{resp.json()}\n')
    elif resp.status_code == 400:
        print('Не верно указано имя пользователя')
    elif resp.status_code == 404:
        print('Пользователь не найден')


def delete_user(username: str):
    resp = requests.delete(base_url + f'/user/{username}', headers=headers)

    if resp.status_code == 200:
        print(f'Удаление пользователя {username} выполнено успешно! Содержимое ответа:\n'
              f'{resp.json()}')
    elif resp.status_code == 400:
        print('Не верно указано имя пользователя')
    elif resp.status_code == 404:
        print('Пользователь не найден')

    print()


if __name__ == '__main__':
    user_name = 'user007'
    user_id = create_user(user_name)
    get_user(user_name)
    update_user(user_name)
    delete_user(user_name)
    get_user(user_name)
