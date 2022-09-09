import time
import requests
import sys
import configparser

"""
Создание папки на полигоне
"""
class Ya_disk():
    def read_token_ya_disk(self):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("start_data.ini")  # читаем конфиг
        return str(config["Poligon"]["token_poligon"].strip('"'))

    def create_new_catalog(self):
        time_requests_struct = time.localtime()
        time_requests = time.strftime("%d_%m_%Y", time_requests_struct)
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.read_token_ya_disk()}'}
        parameters_catalog = {"path": {f'foto_vk_{time_requests}'}}
        res = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers,
                           params=parameters_catalog,     timeout=5)
        if str(res.status_code) not in '409, 202, 201, 200':
            sys.exit("Ошибка запроса создания папки на Я.диске - {response.status_code}")
        return res.status_code

if __name__ == "__main__":
    status = []
    def main():
        user_catalog_create = Ya_disk()
        status = user_catalog_create.create_new_catalog()
        print(status)
        return status

    main()