"""Module """
import json
import os
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
import os

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):  # TODO
        store_path = "../stores/"
        current_path = os.path.dirname(__file__)

        self.__order_request_json_store = os.path.join(current_path, store_path, "order_requests.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path, "order_requests.json")
        self.__order_delivery_json_store = os.path.join(current_path, store_path, "order_delivery.json")

        """Create file if it does not exist and initialize it with an empty list"""
        try:
            if not os.path.exists(self.__order_request_json_store):
                with open(self.__order_request_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")
            if not os.path.exists(self.__order_shipping_json_store):
                with open(self.__order_shipping_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")
            if not os.path.exists(self.__order_delivery_json_store):
                with open(self.__order_delivery_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")
        except Exception as exception:
            raise OrderManagementException("Error initializing the stores") from exception

    @staticmethod
    def validate_ean13(ean13_code:str):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        if len(ean13_code) != 13:
            return 0
        number = ean13_code[:-1]
        check = (10 - int(ean13_code[-1])) % 10
        count = 0
        mult = 1
        for i in number:
            count += int(i)*mult
            mult = 1 if mult == 3 else 3
        return count % 10 == check

    @staticmethod
    def register_order(product_id:str, order_type: str, address: str, phone_number: str, zip_code: str) -> str:
        # Check all attributes have the correct datatype
        if not isinstance(product_id, str) or not isinstance(order_type, str) or not isinstance(address, str) or \
                not isinstance(phone_number, str) or not isinstance(zip_code, str):
            raise OrderManagementException("Attributes must be string datatype")

        # Check product_id:
        if not product_id.isnumeric():
            raise OrderManagementException("Product id wrong format")
        if len(product_id) != 13 or not self.validate_ean13(product_id):
            raise OrderManagementException("Product id not valid")

        # Check order_type:
        if order_type.isnumeric():
            raise OrderManagementException("Order type wrong format")
        if order_type.upper() not in ["PREMIUM", "REGULAR"]:
            raise OrderManagementException("Order type not valid")

        # Check address:
        # Checks range and that there is at least two words separated by a space
        if not 20 <= len(address) <= 100 or len(address.split()) < 2:
            raise OrderManagementException("Address not valid")

        # Check phone_number:
        if not phone_number.isnumeric():
            raise OrderManagementException("Phone number wrong format")
        if len(phone_number) != 9:
            raise OrderManagementException("Phone number not valid")

        # Check zip_code:
        if not zip_code.isnumeric():
            raise OrderManagementException("Zip code wrong format")
        if len(zip_code) != 5 or not 0 < int(zip_code[:2]) < 53:
            raise OrderManagementException("Zip code not valid")

        # ALL CORRECT:
        request = OrderRequest(product_id, order_type, address, phone_number, zip_code)

        # Create file:
        file_path = "../stores/order_requests"
        current_path = os.path.dirname(__file__)
        full_path = os.path.join(current_path, file_path)
        try:  # TODO
            """ If we don't want to remove the order_requests file:
            while os.path.exists(full_path + ".json"):
                last = full_path[-1]
                if last.isnumeric():
                    full_path = full_path[:-1] + str(int(last)+1)
                else:
                    full_path = full_path + "_1"""

            with open(full_path + ".json", "w", encoding="utf-8") as order_request_file:
                order_request_file.write(request.to_json())
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except:
            raise OrderManagementException("Error with the output file")

        return request.order_id

    @staticmethod
    def send_product(input_file):

        with open(input_file, "r", encoding="utf-8") as order_shipping_file:
            order_shipping = json.load(order_shipping_file)


        delivery_email = order_shipping["ContactEmail"]
        order_id = order_shipping["OrderID"]

        # change input_file TODO
        with open("../stores/order_requests.json", "r", encoding="utf-8") as order_request_file:
            order_request = json.load(order_request_file)

        # We assume the order_id in the order_requests.json file always corresponds to the data
        # provided, ensuring that this is true is the job of the registe_order funtion TODO
        if order_request["order_id"] == order_id:
            product_id = order_request["product_id"]
            order_type = order_request["order_type"]
        else:
            raise OrderManagementException("File provided not correct")

        shiping = OrderShipping(product_id, order_id, delivery_email, order_type)

        return shiping.order_id

