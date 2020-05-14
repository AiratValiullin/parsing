import requests
import json
user = input('Введите логин пользователя: ')
repos = requests.get(f'https://api.github.com/users/{user}/repos')
n = 1
data = json.loads(repos.text)
# pprint(data)
for i in data:
    for k, v in i.items():
        if k == 'archive_url':
            print(f'{n} {v}')
            n += 1