import unittest
from unittest.mock import patch
import main


class TestFunctions(unittest.TestCase):

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_get_doc_owner_name(self):
        self.assertEqual(main.get_doc_owner_name(), 'Василий Гупкин')

    @patch('builtins.input', side_effect=['8425 746987', 'passport', 'Ivan Ivanov', 3])
    def test_add_new_doc(self, mock_inputs):
        new_doc_shelf_number = main.add_new_doc()
        self.assertEqual(new_doc_shelf_number, 3)

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc(self):
        doc_number, res_del = main.delete_doc()
        self.assertEqual(res_del, True)

