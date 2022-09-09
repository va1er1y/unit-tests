import requests
import time
import  Ya_disk_create_catalog
import  unittest
from parameterized import parameterized

"""
Тестирование кода создания папки на полигоне
"""

fault_create = [(400,), (401,), (403,), (404,), (423,), (503,)]

class test_create_catalog(unittest.TestCase):
    def setUp(selfself) -> None:
        print('setUp => START TEST')

    def test_1_create_ok(self):
        user_catalog_create = Ya_disk_create_catalog.Ya_disk()
        result = user_catalog_create.create_new_catalog()
        if result == 201 or result == 409:
            result = 200
            self.assertEqual(result, check_catalog())

    @parameterized.expand(fault_create)
    def test_2_create_flt(self, number_fault):
        user_catalog_create_flt = Ya_disk_create_catalog.Ya_disk()
        results = user_catalog_create_flt.create_new_catalog()
        self.assertEqual(results, number_fault)

    def tearDown(self) -> None:
        print('tearDown => END TEST')

a = Ya_disk_create_catalog.Ya_disk()
b= a.read_token_ya_disk()
def check_catalog():
    time_requests_struct = time.localtime()
    time_requests = time.strftime("%d_%m_%Y", time_requests_struct)
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {b}'}
    parameters_catalog = {"path": {f'foto_vk_{time_requests}'}}
    res = requests.get('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=parameters_catalog,
                       timeout=5)
    return(res.status_code)