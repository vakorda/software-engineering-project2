"""Module """
import json
import re
from datetime import datetime, date
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_delivery import OrderDelivery
import os
import hashlib

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):  # TODO
        store_path = "../stores/"
        current_path = os.path.dirname(__file__)

        self.__order_request_json_store = os.path.join(current_path, store_path, "order_requests.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path, "order_shipping.json")
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

    def register_order(self, product_id: str, order_type: str, address: str, phone_number: str, zip_code: str) -> str:
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
        try:  # TODO
            with open(self.__order_request_json_store, "r", encoding="utf-8") as order_request_file:
                data = json.load(order_request_file)
            data.append(request.to_json_dict())
            with open(self.__order_request_json_store, "w", encoding="utf-8") as order_request_file:
                json.dump(data, order_request_file, indent=2)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError:
            raise OrderManagementException("Output file does not exist")

        return request.order_id

    def send_product(self, input_file: str) -> str:
        try:
            with open(input_file, "r", encoding="utf-8") as order_shipping_file:
                order_shipping = json.load(order_shipping_file)
        except FileNotFoundError as ex:
            raise OrderManagementException("File provided does not exist") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("File provided not valid format") from ex

        try:
            delivery_email = order_shipping["ContactEmail"]
            order_id = order_shipping["OrderID"]
        except KeyError:
            raise OrderManagementException("Input file incorrect format")

        if re.match(r'^[a-z0-9]{32}$', order_id) is None:
            raise OrderManagementException("Order id wrong format")
        if re.match(r'^[a-zA-Z0-9-_.]+@([a-zA-Z0-9-_]+\.)+[a-zA-Z0-9-_]{2,4}$', delivery_email) is None:
            raise OrderManagementException("Delivery email wrong format")
        try:
            with open(self.__order_request_json_store, "r", encoding="utf-8") as order_request_file:
                order_request = json.load(order_request_file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Order Request file not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("Reading Order Request file failed") from ex

        i = 1
        for i in range(len(order_request)):
            if order_request[i]["order_id"] == order_id:
                product_id = order_request[i]["product_id"]
                delivery_address = order_request[i]["delivery_address"]
                order_type = order_request[i]["order_type"]
                phone_number = order_request[i]["phone_number"]
                zip_code = order_request[i]["zip_code"]
                time_stamp = str(order_request[i]["time_stamp"])
                signature = ('{"_OrderRequest__product_id": "' + product_id +
                                '", "_OrderRequest__delivery_address": "' + delivery_address +
                                '", "_OrderRequest__order_type": "' + order_type +
                                '", "_OrderRequest__phone_number": "' + phone_number +
                                '", "_OrderRequest__zip_code": "' + zip_code +
                                '", "_OrderRequest__time_stamp": ' + time_stamp + '}')

                if hashlib.md5(signature.encode()).hexdigest() != order_id:
                    raise OrderManagementException("File does not correspond to order id")

                shipping = OrderShipping(product_id, order_id, delivery_email, order_type)

                with open(self.__order_shipping_json_store, "r", encoding="utf-8") as f:
                    data = list(json.load(f))

                data.append(shipping.to_json_dict())

                with open(self.__order_shipping_json_store, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                return shipping.tracking_code

        raise OrderManagementException("OrderID not found in order requests")


    def deliver_product(self, tracking_code: str) -> bool:
        if re.match(r'^[a-f0-9]{64}$', tracking_code) is None:
            raise OrderManagementException("Tracking code invalid format")
        try:
            with open(self.__order_shipping_json_store, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise OrderManagementException('Shippings file not found')
        except json.JSONDecodeError:
            raise OrderManagementException('Shippings file invalid format')

        for elem in data:
            if tracking_code == elem["tracking_code"]:
                delivery_day = elem["delivery_day"]

                signature = json.dumps({"alg": elem["alg"],
                                        "typ": elem["typ"],
                                        "order_id": elem["order_id"],
                                        "issued_at": elem["issued_at"],
                                        "delivery_day": elem["delivery_day"]
                                        }, separators=(',', ':'))

                if hashlib.sha256(signature.encode()).hexdigest() != elem["tracking_code"]:
                    raise OrderManagementException("Order registered does not match tracking code")
                if date.fromtimestamp(delivery_day) != date.fromtimestamp(datetime.timestamp(datetime.utcnow())):
                    raise OrderManagementException("Delivery date not correct")
                else:
                    delivery = OrderDelivery(tracking_code, delivery_day)
                    try:
                        with open(self.__order_delivery_json_store, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        data.append(delivery.to_json_dict())
                        with open(self.__order_delivery_json_store, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2)
                        return True
                    except FileNotFoundError:
                        raise OrderManagementException('Delivery file not found')
                    except json.JSONDecodeError:
                        raise OrderManagementException('Delivery file invalid format')
        raise OrderManagementException('Shipping not found')
