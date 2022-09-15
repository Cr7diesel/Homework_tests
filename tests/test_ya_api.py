import unittest
import yan_disk


class TestRequest(unittest.TestCase):

    # проверка на успешное создание папки
    def test_create_folder(self):
        self.assertEqual(yan_disk.create_folder().status_code, 201)

    # проверка попытки создания папки с одинаковым именем
    def test_double_name_folder(self):
        self.assertEqual(yan_disk.create_folder().status_code, 409)

    #проверка удаления папки
    def test_delete_folder(self):
        self.assertEqual(yan_disk.delete_folder().status_code, 204)
