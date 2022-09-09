import  unittest
from parameterized import parameterized
import lession_2_1

"""
Тестирование кода из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» 
"""

def doc():
    document = []
    for i in lession_2_1.documents:
        a = (i["number"], i["name"])
        document.append(a)
    return document

def direct():
    directori = []
    for num_shelf, num_doc in lession_2_1.directories.items():
        if len(num_doc) == 0:
            continue
        else:
            if len(num_doc) >= 1:
                for i in num_doc:
                    a = (num_shelf, i)
                    directori.append(a)
                continue
        a = (num_shelf, num_doc)
        directori.append(a)
    return (directori)

shelf = [(5, 5, True), (1, 1, True)]

class testfunctions(unittest.TestCase):
    def setUp(selfself) -> None:
        print('setUp => START TEST')

    def test_1_all_people(self):
        result=lession_2_1.get_all_doc_owners_names()
        self.assertEqual(result, {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'})

    @parameterized.expand(doc())
    def test_2_people(self, number, name):
        name_result = lession_2_1.get_doc_owner_name(number)
        self.assertEqual(name_result, name)

    @parameterized.expand(direct())
    def test_3_shelf(self, shelf, number):
        number_result = lession_2_1.get_doc_shelf(number)
        self.assertEqual(number_result, shelf)

    def test_5_del(self):
        resul1, resul2 = lession_2_1.delete_doc('2207 876234')
        self.assertEqual((resul1, resul2), ('2207 876234', True))

    def test_6_move_shelf(self):
        result1, result2 = lession_2_1.move_doc_to_shelf('10006', '1')
        self.assertEqual((result1, result2), ('10006', '1'))

    @parameterized.expand(shelf)
    def test_4_add_shelf(self, number_shelf_new, number_shelf_created, confirm):
        result1, result2 = lession_2_1.add_new_shelf(number_shelf_new)
        self.assertEqual((result1, result2), (number_shelf_created, confirm))
    #
    def test_7_add(self):
        result = lession_2_1.add_new_doc('1090', 'паспорт', 'Иванов Валерий', '1')
        self.assertEqual(result, '1')

    def tearDown(self) -> None:
        print('tearDown => END TEST')

