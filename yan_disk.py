import requests


folder_name = 'unittest_dir_1'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
token = ''
params = {'path': folder_name}
headers = {'Content-Type': 'application/json',
           'Authorization': f'OAuth {token}'}


def create_folder():
    res = requests.put(url, params=params, headers=headers)
    return res


def delete_folder():
    res = requests.delete(url, params=params, headers=headers)
    return res


if __name__ == '__main__':
    create_folder()
    delete_folder()
