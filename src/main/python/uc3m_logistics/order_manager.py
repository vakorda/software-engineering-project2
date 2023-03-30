"""Module """
import json
import os
import re
from datetime import datetime, date
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_delivery import OrderDelivery
import os

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

    def register_order(self, product_id:str, order_type: str, address: str, phone_number: str, zip_code: str) -> str:
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

        # TODO: check that ContactEmail and OrderID exist in the file

        delivery_email = order_shipping["ContactEmail"]
        order_id = order_shipping["OrderID"]

        # Check product_id:
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
                # We assume the product_id and order_type have correct formats
                # since it is the job of the register order function to do so
                # if there was a case when they were not we should see that in the tests of the function
                product_id = order_request[i]["product_id"]
                order_type = order_request[i]["order_type"]
                i = -1  # i becomes negative when the request is found
                break
        if i > -1:
            raise OrderManagementException("OrderID not found in order requests")
        shipping = OrderShipping(product_id, order_id, delivery_email, order_type)

        with open(self.__order_shipping_json_store, "r", encoding="utf-8") as f:
            data = list(json.load(f))

        data.append(shipping.to_json_dict())

        with open(self.__order_shipping_json_store, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return shipping.tracking_code

    def deliver_product(self, tracking_code): #TODO actualizar codigo en la foto
        if re.match(r'^[a-z0-9]{64}$', tracking_code) is None:
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
                if date.fromtimestamp(delivery_day) != date.fromtimestamp(datetime.timestamp(datetime.utcnow())):
                    return False
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
        return False


        #f = os.path.join(current_path, store_path, "order_requests.json")

        #if shiping.

        #try:
        #    with open(f, "r", encoding="utf-8", newline=""):
        #        data = json.load(f)
        #except:

        #return data



#om = OrderManager()
#
#product_id = "8421691423220"
#order_type = "REGULAR"
#delivery_address = "C/LISBOA,4, MADRID, SPAIN"
#phone_number = "123456789"
#zip_code = "28005"
#
## run the function
#order_id = om.register_order(product_id, order_type, delivery_address, phone_number, zip_code)
#tracking_code = om.send_product('../stores/order_shipping.json')
#
#print(order_id, tracking_code)
#


#om = OrderManager()

#a = o#m.deliver_product("201b992c72aaed218a37b2ef392eb3ce58edef85553fada83e3666f05139949e")
#print#(a)

