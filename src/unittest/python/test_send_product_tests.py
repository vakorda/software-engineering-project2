"""class for testing the send_product method"""
from unittest import TestCase
import os
import json
import unittest
from uc3m_logistics import OrderManager, OrderManagementException
from freezegun import freeze_time


class TestSendProduct(TestCase):
    """class for testing the send_product method"""
    @classmethod
    @freeze_time("2023-03-17")
    def setUpClass(cls) -> None:
        """Executed before all tests"""
        current_path = os.path.dirname(__file__)
        cls.__test_folder = os.path.join(current_path
                                         , "../../unittest/python/shippings")
        cls.__requests_path = os.path.join(current_path
                                           , "../../main/python/stores/order_requests.json")
        cls.__shipping_path = os.path.join(current_path
                                           , "../../main/python/stores/order_shipping.json")

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
    def test1(self):
        """ This test ends with no exceptions"""
        test_name = "test1.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = json.load(file)

        tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
                         tracking_code)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = json.load(file)

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
    def test56(self):
        """This test ends with no exceptions"""
        test_name = "test56.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = json.load(file)

        tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
                         tracking_code)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = json.load(file)

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
    def test58(self):
        """This test ends with no exceptions"""
        test_name = "test58.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = json.load(file)

        tracking_code = self.__order_manager.send_product(test_path)
        self.assertEqual("d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
                         tracking_code)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = json.load(file)

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
        """This raises File provided not valid format"""
        test_name = "test2.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test3(self):
        """This raises File provided not valid format"""
        test_name = "test3.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test5(self):
        """This raises File provided not valid format"""
        test_name = "test5.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test6(self):
        """This raises File provided not valid format"""
        test_name = "test6.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test7(self):
        """This raises File provided not valid format"""
        test_name = "test7.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test8(self):
        """This raises File provided not valid format"""
        test_name = "test8.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test9(self):
        """This raises File provided not valid format"""
        test_name = "test9.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test10(self):
        """This raises File provided not valid format"""
        test_name = "test10.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test11(self):
        """This raises File provided not valid format"""
        test_name = "test11.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test12(self):
        """This raises File provided not valid format"""
        test_name = "test12.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test13(self):
        """This raises File provided not valid format"""
        test_name = "test13.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test14(self):
        """This raises File provided not valid format"""
        test_name = "test14.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test15(self):
        """This raises File provided not valid format"""
        test_name = "test15.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test16(self):
        """This raises File provided not valid format"""
        test_name = "test16.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test17(self):
        """This raises File provided not valid format"""
        test_name = "test17.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test18(self):
        """This raises File provided not valid format"""
        test_name = "test18.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test19(self):
        """This raises File provided not valid format"""
        test_name = "test19.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test20(self):
        """This raises File provided not valid format"""
        test_name = "test20.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test21(self):
        """This raises File provided not valid format"""
        test_name = "test21.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test22(self):
        """This raises File provided not valid format"""
        test_name = "test22.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test31(self):
        """This raises File provided not valid format"""
        test_name = "test31.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test32(self):
        """This raises File provided not valid format"""
        test_name = "test32.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test33(self):
        """This raises File provided not valid format"""
        test_name = "test33.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test34(self):
        """This raises File provided not valid format"""
        test_name = "test34.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test35(self):
        """This raises File provided not valid format"""
        test_name = "test35.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test36(self):
        """This raises File provided not valid format"""
        test_name = "test36.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test37(self):
        """This raises File provided not valid format"""
        test_name = "test37.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test38(self):
        """This raises File provided not valid format"""
        test_name = "test38.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test39(self):
        """This raises File provided not valid format"""
        test_name = "test39.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test40(self):
        """This raises File provided not valid format"""
        test_name = "test40.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test41(self):
        """This raises File provided not valid format"""
        test_name = "test41.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test42(self):
        """This raises File provided not valid format"""
        test_name = "test42.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test43(self):
        """This raises File provided not valid format"""
        test_name = "test43.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test44(self):
        """This raises File provided not valid format"""
        test_name = "test44.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test45(self):
        """This raises File provided not valid format"""
        test_name = "test45.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test46(self):
        """This raises File provided not valid format"""
        test_name = "test46.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test47(self):
        """This raises File provided not valid format"""
        test_name = "test47.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test48(self):
        """This raises File provided not valid format"""
        test_name = "test48.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test49(self):
        """This raises File provided not valid format"""
        test_name = "test49.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test50(self):
        """This raises File provided not valid format"""
        test_name = "test50.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test51(self):
        """This raises File provided not valid format"""
        test_name = "test51.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test61(self):
        """This raises File provided not valid format"""
        test_name = "test61.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test62(self):
        """This raises File provided not valid format"""
        test_name = "test62.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test63(self):
        """This raises File provided not valid format"""
        test_name = "test63.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test64(self):
        """This raises File provided not valid format"""
        test_name = "test64.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test65(self):
        """This raises File provided not valid format"""
        test_name = "test65.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test66(self):
        """This raises File provided not valid format"""
        test_name = "test66.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test67(self):
        """This raises File provided not valid format"""
        test_name = "test67.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test68(self):
        """This raises File provided not valid format"""
        test_name = "test68.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test69(self):
        """This raises File provided not valid format"""
        test_name = "test69.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test70(self):
        """This raises File provided not valid format"""
        test_name = "test70.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test71(self):
        """This raises File provided not valid format"""
        test_name = "test71.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test72(self):
        """This raises File provided not valid format"""
        test_name = "test72.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test73(self):
        """This raises File provided not valid format"""
        test_name = "test73.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("File provided not valid format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test4(self):
        """This raises Input file incorrect format format"""
        test_name = "test4.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test23(self):
        """This raises Input file incorrect format format"""
        test_name = "test23.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test25(self):
        """This raises Input file incorrect format format"""
        test_name = "test25.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test52(self):
        """This raises Input file incorrect format format"""
        test_name = "test52.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test54(self):
        """This raises Input file incorrect format format"""
        test_name = "test54.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test74(self):
        """This raises Input file incorrect format format"""
        test_name = "test74.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test78(self):
        """This raises Input file incorrect format format"""
        test_name = "test78.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Input file incorrect format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test26(self):
        """This raises Delivery email wrong format"""
        test_name = "test26.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test27(self):
        """This raises Delivery email wrong format"""
        test_name = "test27.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test28(self):
        """This raises Delivery email wrong format"""
        test_name = "test28.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test29(self):
        """This raises Delivery email wrong format"""
        test_name = "test29.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test30(self):
        """This raises Delivery email wrong format"""
        test_name = "test30.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test55(self):
        """This raises Delivery email wrong format"""
        test_name = "test55.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test57(self):
        """This raises Delivery email wrong format"""
        test_name = "test57.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test59(self):
        """This raises Delivery email wrong format"""
        test_name = "test59.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test79(self):
        """This raises Delivery email wrong format"""
        test_name = "test79.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test80(self):
        """This raises Delivery email wrong format"""
        test_name = "test80.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test81(self):
        """This raises Delivery email wrong format"""
        test_name = "test81.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test82(self):
        """This raises Delivery email wrong format"""
        test_name = "test82.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test83(self):
        """This raises Delivery email wrong format"""
        test_name = "test83.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Delivery email wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test24(self):
        """This raises Order id wrong format"""
        test_name = "test24.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Order id wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test53(self):
        """This raises Order id wrong format"""
        test_name = "test53.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Order id wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test75(self):
        """This raises Order id wrong format"""
        test_name = "test75.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Order id wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test76(self):
        """This raises Order id wrong format"""
        test_name = "test76.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Order id wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)

    @freeze_time("2023-03-17")
    def test77(self):
        """This raises Order id wrong format"""
        test_name = "test77.json"
        test_path = os.path.join(self.__test_folder, test_name)

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            initial_shipings = list(json.load(file))

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.send_product(test_path)
        self.assertEqual("Order id wrong format", str(ome.exception))

        with open(self.__shipping_path, "r", encoding="utf-8") as file:
            final_shipings = list(json.load(file))

        self.assertListEqual(initial_shipings, final_shipings)



###############################3

if __name__ == '__main__':
    unittest.main()
