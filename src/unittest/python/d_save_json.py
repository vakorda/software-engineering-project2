"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime
from freezegun import freeze_time


class OrderRequest:
    """Class representing one order for a product"""
    @freeze_time("17-03-2023")
    def __init__(self, product_id, order_type, delivery_address, phone_number, zip_code):
        self.__product_id = product_id
        self.__delivery_address = delivery_address
        self.__order_type = order_type
        self.__phone_number = phone_number
        self.__zip_code = zip_code
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def to_json(self):
        return {
         "order_id": self.__order_type,
         "product_id": self.__product_id,
         "delivery_address": self.__delivery_address,
         "order_type": self.__order_type,
         "zip_code": self.__zip_code,
         "time_stamp": self.__time_stamp
        }

    def __str__(self):
        #return str(self.to_json())
        return json.dumps(self.__dict__)

    @property
    def delivery_address(self):
        """Property representing the address where the product
        must be delivered"""
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self.__delivery_address = value

    @property
    def order_type(self):
        """Property representing the type of order: REGULAR or PREMIUM"""
        return self.__order_type

    @order_type.setter
    def order_type(self, value):
        self.__order_type = value

    @property
    def phone_number(self):
        """Property representing the clients's phone number"""
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def product_id(self):
        """Property representing the products  EAN13 code"""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def order_id(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()

    @property
    def zip_code(self):
        """Returns the patient's zip_code"""
        return self.__zip_code

    def save_json(self):
        """Saves the object as json"""
        with open("prueba.json", "w", encoding="utf-8") as file:
            file.write(str(self))


# 1
om = OrderRequest("8421691423220",
                  "REGULAR",
                  "C/LISBOA,4, MADRID, SPAIN",
                  "123456789",
                  "28005")
print("01: " + om.order_id)

# 6
om = OrderRequest("8421691423220",
                  "PREMIUM",
                  "C/LISBOA,4, MADRID, SPAIN",
                  "123456789",
                  "28005")
print("06: " + om.order_id)

# 8
om = OrderRequest("8421691423220",
                  "Premium",
                  "C/LISBOA,4, MADRID, SPAIN",
                  "123456789",
                  "28005")
print("08: " + om.order_id)

# 13

om = OrderRequest("8421691423220",
                  "PREMIUM",
                  "C/RUS, MADRID, SPAIN",
                  "123456789",
                  "28005")
print("13: " + om.order_id)

# 14

om = OrderRequest("8421691423220",
                  "PREMIUM",
                  "CJ/ LA SARGENTO PEPA, 2468, GARGANTILLA DEL LOZOYA Y PINILLA DE BUITRAGO, COMUNIDAD DE MADRID, SPAIN",
                  "123456789",
                  "28005")

print("14: " + om.order_id)

# 25

om = OrderRequest("8421691423220",
                  "PREMIUM",
                  "C/LISBOA,4, MADRID, SPAIN",
                  "123456789",
                  "52999")
print("25: " + om.order_id)

# 26

om = OrderRequest("8421691423220",
                  "PREMIUM",
                  "C/LISBOA,4, MADRID, SPAIN",
                  "123456789",
                  "01000")

print("26: " + om.order_id)