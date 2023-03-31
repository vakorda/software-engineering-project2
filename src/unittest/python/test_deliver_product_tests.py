"""class for testing the regsiter_order method"""
import os
import json
from unittest import TestCase
import unittest
from uc3m_logistics import OrderManager
from freezegun import freeze_time
from uc3m_logistics import OrderManagementException

class MyTestCase(TestCase):
    """class for testing the register_order method"""

    __file_path: str

    @classmethod
    @freeze_time("2023-03-17")
    def setUpClass(cls) -> None:
        """Executed before all tests"""
        cls.__order_manager = OrderManager()
        current_path = os.path.dirname(__file__)
        cls.__test_folder = os.path.join(current_path, "../../unittest/python/shippings")
        cls.__requests_path = os.path.join(current_path, "../../main/python/stores/order_requests.json")
        cls.__shipping_path = os.path.join(current_path, "../../main/python/stores/order_shipping.json")
        cls.__deliver_path = os.path.join(current_path, "../../main/python/stores/order_delivery.json")

    def setUp(self) -> None:
        with open(self.__requests_path, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(self.__shipping_path, "w", encoding="utf-8") as file:
            file.write("[]")
        with open(self.__deliver_path, "w", encoding="utf-8") as file:
            file.write("[]")

    @freeze_time("2023-03-24")
    def test_01(self):
        """1-3-4-7-8-9-11-13-14-15-E
        Most common execution path
        """

        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        self.assertEqual(True, self.__order_manager.deliver_product(tracking_code))
        # Check that the contents of the file have changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertNotEqual(initial_data, final_data)

        # open the file and check the parameters
        with open(self.__deliver_path, "r", encoding="utf-8") as file:
            order_delivery = json.load(file)[-1]
            self.assertDictEqual({
                "tracking_code": "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
                "delivery_day": 1679616000.0
            }, order_delivery)

    def test_02(self):
        """1-2-E
        Tracking code has invalid format
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cde"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Tracking code invalid format", str(ome.exception))
        # Check that the contents of the file are the same as before
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertEqual(initial_data, final_data)

    @freeze_time("2023-03-24")
    def test_03(self):
        """1-3-5-E
        deletes shippings file
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"
        os.remove(self.__shipping_path)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Shippings file not found", str(ome.exception))

    @freeze_time("2023-03-24")
    def test_04(self):
        """1-3-4-6-E
        Shippings file invalid format
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)

        with open(self.__shipping_path, "w", encoding="utf-8") as f:
            f.write("sfjhd]")

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Shippings file invalid format", str(ome.exception))

    @freeze_time("2023-03-24")
    def test_05(self):
        """1-3-4-7-18-E
        Loop executed 0 times since shippings file is empty
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)

        tracking_code = "4485748578976883968438984357457459739579487598345738467897468967"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Shipping not found", str(ome.exception))
        # Check that the contents of the file have not changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertEqual(initial_data, final_data)

    @freeze_time("2023-03-24")
    def test_06(self):
        """1-3-4-7-18-E
        Loop executed 1 time since tracking code not in shippings file
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        tracking_code = "4485748578976883968438984357457459739579487598345738467897468967"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Shipping not found", str(ome.exception))
        # Check that the contents of the file have not changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertEqual(initial_data, final_data)

    @freeze_time("2023-03-24")
    def test_07(self):
        """1-3-4-7-8-7-8-9-11-13-14-15-E
        loop executed 2 times, second shipping is the one that we look for
        """

        with open(self.__shipping_path, "w", encoding="utf-8") as f:
            f.write("[{\"alg\": \"SHA-256\","
                    "\"typ\": \"DS\","
                    "\"tracking_code\": \"d1c866b1e6d8c1e9823c8bed8909dbbb2e12345673e7687fa70c7ed7eee2d8cd\","
                    "\"order_id\": \"93ad8ecd0fc177ae376e3b4d3212b5c5\","
                    "\"issued_at\": 1679011200.0,"
                    "\"delivery_day\": 1679616000.0}]")

        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        self.assertEqual(True, self.__order_manager.deliver_product(tracking_code))
        # Check that the contents of the file have changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertNotEqual(initial_data, final_data)

        # open the file and check the parameters
        with open(self.__deliver_path, "r", encoding="utf-8") as file:
            order_delivery = json.load(file)[-1]
            self.assertDictEqual({
                "tracking_code": "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd",
                "delivery_day": 1679616000.0
            }, order_delivery)

    @freeze_time("2023-03-17")
    def test_08(self):
        """1-3-4-7-8-9-10-E
        The order in shipping order has the correct tracking_code but the arguments do not correspond to it
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # write in the file the correct tracking code but other arguments changed
        with open(self.__shipping_path, "w", encoding="utf-8") as f:
            f.write("[{\"alg\": \"SHA-365\","
                    "\"typ\": \"PA\","
                    "\"tracking_code\": \"d1c866b1e6d8c1e9823c8bed8909dbbb2e12345673e7687fa70c7ed7eee2d8cd\","
                    "\"order_id\": \"93ad8ecd0fc177ae376e3b4d3212b5c5\","
                    "\"issued_at\": 1679011200.0,"
                    "\"delivery_day\": 1679616000.0}]")

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e12345673e7687fa70c7ed7eee2d8cd"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Order registered does not match tracking code", str(ome.exception))
        # Check that the contents of the file have not changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertEqual(initial_data, final_data)

    @freeze_time("2023-03-17")
    def test_09(self):
        """1-3-4-7-8-9-11-12-E
        Delivery day is not correct
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)

        tracking_code = "4485748578976883968438984357457459739579487598345738467897468967"
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            initial_data = json.load(f)
        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Shipping not found", str(ome.exception))
        # Check that the contents of the file have not changed
        with open(self.__deliver_path, "r", encoding="utf-8") as f:
            final_data = json.load(f)
        self.assertEqual(initial_data, final_data)
    @freeze_time("2023-03-24")
    def test_10(self):
        """1-3-4-7-8-9-11-13-16-E
        Delivery file not found
        """
        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        os.remove(self.__deliver_path)

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Delivery file not found", str(ome.exception))

    @freeze_time("2023-03-24")
    def test_11(self):
        """1-3-4-7-8-9-11-13-14-17-E
        Delivery file has invalid format
        """

        # Initializes the requests file with the ones that lead to the corresponding order_id
        arguments = ["8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005"]
        # run the function
        with freeze_time("2023-03-17"):
            OrderManager().register_order(*arguments)
            OrderManager().send_product(os.path.join(self.__test_folder, "test1.json"))

        tracking_code = "d1c866b1e6d8c1e9823c8bed8909dbbb2e96bc4a73e7687fa70c7ed7eee2d8cd"

        with open(self.__deliver_path, "w", encoding="utf-8") as f:
            f.write("hjkfd]")

        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.deliver_product(tracking_code)
        self.assertEqual("Delivery file invalid format", str(ome.exception))


if __name__ == '__main__':
    unittest.main()
