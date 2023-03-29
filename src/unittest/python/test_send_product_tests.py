from unittest import TestCase
import os
import json
import unittest
from uc3m_logistics import OrderManager
from freezegun import freeze_time
from uc3m_logistics import OrderRequest
from uc3m_logistics import OrderManagementException


# Forma para crear algunos tests
def create_tests():
    # Numbers are inserted inbetween the elements of the array
    # take thing for the asser
    # sheet_name = 1 significa que coge los datos de la segunda hoja

    tests_con_plantilla1 = [2, 5, 4, 6, 9, 23, 65, 84]
    out = ""
    plantilla_1 = [
        "def test", "(self):\n"
                    "\"\"\"este es el test numero ",
        "\"\"\"\n"
        "   file_path = os.path.join(self.__folder_path, \"test", ".json\")\n"
        "   self.assertEqual(\"jdfhjkhgjfgjkshdjkhfdhfask, self.__order_manager.send_product(file_path)\n\n"
    ]
    for i in tests_con_plantilla1:
        out += plantilla_1[0]
        for j in range(len(plantilla_1) - 1):
            out += str(i)
            out += plantilla_1[j + 1]
    print(out)


create_tests()

class TestSendProduct(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Executed before all tests"""
        current_path = os.path.dirname(__file__)
        cls.__folder_path = os.path.join(current_path, "../../main/python/shippings/")

    def setUp(self) -> None:
        """Executed before each test"""
        self.__order_manager = OrderManager()
    def test1(self):




if __name__ == '__main__':
    unittest.main()
