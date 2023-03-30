"""class for testing the regsiter_order method"""
import os
import json
from unittest import TestCase
import unittest
from uc3m_logistics import OrderManager
from freezegun import freeze_time
from uc3m_logistics import OrderRequest
from uc3m_logistics import OrderManagementException

class MyTestCase(TestCase):
    """class for testing the register_order method"""

    __file_path: str

    @classmethod
    def setUpClass(cls) -> None:
        """Executed before all tests"""
        current_path = os.path.dirname(__file__)
        cls.__file_path = os.path.join(current_path, "../../main/python/stores/order_requests.json")

    def setUp(self) -> None:
        """Executed before each test"""
        self.__order_manager = OrderManager()
        # Empty output file
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write("[]")  # the .json file needs to have something, else it could raise a JSONDecodeError

    # FIRST WE DO ALL THE CORRECT TESTS
    @freeze_time("2023-03-17")
    def test_01(self):
        """V-1-EC) (ALL VALID"""
        product_id = "8421691423220"
        order_type = "REGULAR"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)

        # check order_id
        self.assertEqual("93ad8ecd0fc177ae373e3bbd3212b5c5", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("2023-03-17")
    def test_06(self):
        """V-6-EC) (ALL VALID | order_type=PREMIUM"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("bd0e6e2b623b130048b77c98689933aa", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("2023-03-17")
    def test_08(self):
        """V-8-EC) (ALL VALID | order_type=Premium"""
        product_id = "8421691423220"
        order_type = "Premium"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("5849a0f1531650992b9ea9de80286720", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("2023-03-17")
    def test_12(self):
        """V-12-BV) (ALL VALID | address[lower bound] length=20"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/RUS, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("8e589ebb30161f23d13af400303e46a2", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("2023-03-17")
    def test_13(self):
        """V-13-BV) (ALL VALID | address[upper bound] length=100"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "CJ/ LA SARGENTO PEPA, 2468, GARGANTILLA DEL LOZOYA Y PINILLA DE BUITRAGO, COMUNIDAD DE MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("96be4e6047c4cd506faf7f6c0c02b527", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("17-03-2023")
    def test_24(self):
        """V-24-BV) (ALL VALID | zip_code[upper bound]=52999"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "52999"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("3a1557c18bc194cd906fd6762cfd04f8", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("17-03-2023")
    def test_25(self):
        """V-25-BV) (ALL VALID | zip_code[lower bound]=01000"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "01000"

        # run the function
        order_id = self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)

        # open the file and check the parameters
        with open(self.__file_path, "r", encoding="utf-8") as file:
            order_requests = json.load(file)[-1]
            self.assertDictEqual({
                "order_id": order_id,
                "product_id": product_id,
                "order_type": order_type,
                "delivery_address": delivery_address,
                "phone_number": phone_number,
                "zip_code": zip_code,
                "time_stamp": 1679011200.0
            }, order_requests)
        # check order_id
        self.assertEqual("97f100660b53883f0a002cc6e50941c0", OrderRequest(product_id, order_type, delivery_address, phone_number, zip_code).order_id)

    @freeze_time("17-03-2023")
    def test_02(self):
        """NV-2-EC) (NOT VALID | product_id not number"""
        product_id = "842169142322A"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Product id wrong format", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_03(self):
        """NV-3-EC) (NOT VALID | product_id not check sum"""
        product_id = "8421691423225"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Product id not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_04(self):
        """NV-4-BV) (NOT VALID | product_id[shorter] length=12"""
        product_id = "842169142326"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Product id not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_05(self):
        """NV-5-BV) (NOT VALID | product_id[longer] length=14"""
        product_id = "84216914232200"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Product id not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_07(self):
        """NV-7-EC) (NOT VALID | order_type=PRE"""
        product_id = "8421691423220"
        order_type = "PRE"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Order type not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_09(self):
        """NV-9-EC) (NOT VALID | order_type not string"""
        product_id = "8421691423220"
        order_type = "22608455739725133"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Order type wrong format", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_10(self):
        """NV-10-EC)  (NOT VALID | address 0 spaces"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4,MADRID,SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Address not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_11(self):
        """NV-11-BV)  (NOT VALID | address[shorter] length=19"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/FA, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Address not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_14(self):
        """NV-14-BV)  (NOT VALID | address[longer] length=101"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "CJ/ LA SARGENTO PEPA, 24680, GARGANTILLA DEL LOZOYA Y PINILLA DE BUITRAGO, COMUNIDAD DE MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Address not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_15(self):
        """NV-15-EC) (NOT VALID | address has 1 space and 1 word"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4,MADRID,SPAIN "
        phone_number = "123456789"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Address not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_16(self):
        """NV-16-BV) (NOT VALID | phone_number[longer] length=10"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "1234567898"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Phone number not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_17(self):
        """NV-17-BV) (NOT VALID | phone_number[shorter] length=9"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "12345678"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Phone number not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_18(self):
        """NV-18-EC) (NOT VALID | phone_number not number"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456A89"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Phone number wrong format", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_19(self):
        """NV-19-EC) (NOT VALID | phone_number is string"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "JUANSELMO"
        zip_code = "28005"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Phone number wrong format", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_20(self):
        """NV-20-BV) (NOT VALID | zip_code[longer] length=6"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "034222"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_21(self):
        """NV-21-BV) (NOT VALID | zip_code[shorter] length=4"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "2500"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_22(self):
        """NV-22-EC) (NOT VALID | zip_code not number"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "123A4"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code wrong format", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_23(self):
        """NV-23-BV) (NOT VALID | zip_code[upper_bound]=53000"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "53000"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_26(self):
        """NV-26-BV) (NOT VALID | zip_code[lower_bound]=00999"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "00999"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code not valid", str(ome.exception))

    @freeze_time("17-03-2023")
    def test_27(self):
        """NV-27-EC) (NOT VALID | zip_code not number"""
        product_id = "8421691423220"
        order_type = "PREMIUM"
        delivery_address = "C/LISBOA,4, MADRID, SPAIN"
        phone_number = "123456789"
        zip_code = "03A66"

        # run the function
        with self.assertRaises(OrderManagementException) as ome:
            self.__order_manager.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
        self.assertEqual("Zip code wrong format", str(ome.exception))


if __name__ == '__main__':
    unittest.main()
