"""
We decide to accept only accept product_id, phone_number and zip_code in
"""
from uc3m_logistics import OrderRequest
from uc3m_logistics import OrderManagementException
from uc3m_logistics import OrderManager
import os
from freezegun import freeze_time

def register_order(product_id: str, order_type: str, address: str, phone_number: str, zip_code: str) -> str:
    # Check all attributes have the correct datatype
    if not isinstance(product_id, str) or not isinstance(order_type, str) or not isinstance(address, str) or\
       not isinstance(phone_number, str) or not isinstance(zip_code, str):
        raise OrderManagementException("Attributes must be string datatype")

    # Check product_id:
    if not product_id.isnumeric():
        raise OrderManagementException("Product id wrong format")
    if len(product_id) != 13 or not OrderManager.validate_ean13(product_id):
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
    try:
        """ If we don't want to remove the order_requests file:
        while os.path.exists(full_path + ".json"):
            last = full_path[-1]
            if last.isnumeric():
                full_path = full_path[:-1] + str(int(last)+1)
            else:
                full_path = full_path + "_1"""

        with open(full_path + ".json", "w", encoding="utf-8") as order_request_file:
            order_request_file.write(request.to_json())
    except:
        raise OrderManagementException("Error with the output file")

    return request.order_id

# TODO

#o = register_order("8421691423220",
#                  "PREMIUM",
#                  "C/LISBOA,4, MADRID, SPAIN",
#                  "123456789",
#                  "01000")
#print(o)