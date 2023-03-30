"""Contains the class OrderShipping"""
import datetime
import hashlib
import json

class OrderDelivery():
    """Class representing the information required for shipping of an order"""

    def __init__(self, tracking_code: str, delivery_day: datetime.datetime):
        self.__tracking_code = tracking_code
        self.__delivery_day = delivery_day

    def to_json_dict(self):
        return {
                "tracking_code": self.tracking_code,
                "delivery_day": self.__delivery_day
                }

    def __signature_string(self):  # TODO
        """Composes the string to be used for generating the key for the date"""
        return json.dumps({
                           "tracking_code": self.tracking_code,
                           "delivery_day": self.__delivery_day
                          }, separators=(',', ':'))

    @property
    def tracking_code(self):
        """Returns the sha256 signature of the date"""
        return self.__tracking_code

    @tracking_code.setter
    def tracking_code(self, value):
        self.__tracking_code = value

    @property
    def issued_at(self):
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value

    @property
    def delivery_day(self):
        """Returns the delivery day for the order"""
        return self.__delivery_day