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
    out = ""
    plantilla_1 = [
        "def test", "(self):\n"
                    "\"\"\"este es el test numero ",
        "\"\"\"\n"
        "   file_path = os.path.join(self.__folder_path, \"test", ".json\")\n"
        "   self.assertEqual(\"jdfhjkhgjfgjkshdjkhfdhfask, self.__order_manager.send_product(file_path)\n\n"
    ]
    plantilla_2 = [
                    '   @freeze_time("2023-03-17")\n'
                    '   def test', '(self):\n'
                    '        test_name = "test', '.json"\n'
                    '        test_path = os.path.join(self.__test_folder, test_name)\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            initial_shipings = list(json.load(f))\n'
                    '\n'
                    '        with self.assertRaises(OrderManagementException) as ome:\n'
                    '            tracking_code = self.__order_manager.send_product(test_path)\n'
                    '        self.assertEqual("File provided not valid format", str(ome.exception))\n'
                    '\n'
                    '        with open(self.__shipping_path, "r", encoding="utf-8") as f:\n'
                    '            final_shipings = list(json.load(f))\n'
                    '\n'
                    '        self.assertListEqual(initial_shipings, final_shipings)\n']

    tests_con_plantilla2 = [2, 3, 5, 6, 7, 8, 9, 10, 11,12, 13,14,15,16,17,18,19,20,21,22,23,24,25]
    for i in tests_con_plantilla2:
        out += plantilla_2[0]
        for j in range(len(plantilla_2) - 1):
            out += str(i)
            out += plantilla_2[j + 1]
    print(out)


create_tests()

class TestSendProduct(TestCase):

    @classmethod
    @freeze_time("2023-03-17")
    def setUpClass(cls) -> None:
        """Executed before all tests"""
        current_path = os.path.dirname(__file__)
        cls.__test_folder = os.path.join(current_path, "../../unittest/python/shippings")
        cls.__requests_path = os.path.join(current_path, "../../main/python/stores/order_requests.json")
        cls.__shipping_path = os.path.join(current_path, "../../main/python/stores/order_shipping.json")

        with open(cls.__requests_path, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(cls.__shipping_path, "w", encoding="utf-8") as file:
            file.write("[]")

        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        OrderManager().register_order(*arguments)

    def setUp(self) -> None:
        """Executed before each test"""
        self.__order_manager = OrderManager()

    @freeze_time("2023-03-17")
    def testgen(self):
        om = OrderManager()

        product_id = "8421691423220"
        order_type = "REGULAR"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = om.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        print(order_id)
        path = os.path.join(os.path.dirname(__file__), os.path.join(self.__test_folder, "test1.json"))
        tracking_code = om.send_product(path)

        print(order_id, tracking_code)

    @freeze_time("2023-03-17")
    def test1(self):
        test_name = "test1.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = json.load(f)

        tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd", tracking_code)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = json.load(f)

        self.assertNotEqual(initial_shipings, final_shipings)

        valid_data = {
            "alg": "SHA-256",
            "typ": "DS",
            "tracking_code": "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
            "order_id": "93ad8ecd0fc177ae373e3bbd3212b5c5",
            "issued_at": 1679011200.0,
            "delivery_day": 1679616000.0
            }

        self.assertDictEqual(valid_data, final_shipings[-1])

    @freeze_time("2023-03-17")
    def test2(self):
        test_name = "test2.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test2(self):
        test_name = "test2.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test3(self):
        test_name = "test3.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test5(self):
        test_name = "test5.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test6(self):
        test_name = "test6.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test7(self):
        test_name = "test7.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test8(self):
        test_name = "test8.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test9(self):
        test_name = "test9.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test10(self):
        test_name = "test10.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test11(self):
        test_name = "test11.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test12(self):
        test_name = "test12.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test13(self):
        test_name = "test13.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test14(self):
        test_name = "test14.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test15(self):
        test_name = "test15.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test16(self):
        test_name = "test16.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test17(self):
        test_name = "test17.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test18(self):
        test_name = "test18.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test19(self):
        test_name = "test19.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test20(self):
        test_name = "test20.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test21(self):
        test_name = "test21.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test22(self):
        test_name = "test22.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test23(self):
        test_name = "test23.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test24(self):
        test_name = "test24.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test25(self):
        test_name = "test25.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            initial_shipings = list(json.load(f))

        with self.assertRaises(OrderManagementException) as ome:
            tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as f:
            final_shipings = list(json.load(f))

        self.assertListEqual(initial_shipings, final_shipings)




###############################3

if __name__ == '__main__':
    unittest.main()
