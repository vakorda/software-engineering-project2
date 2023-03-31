"""Contains the class OrderShipping"""
import datetime


class OrderDelivery:
    """Class representing the information required for shipping of an order"""

    def __init__(self, tracking_code: str, delivery_day: datetime.datetime):
        self.__tracking_code = tracking_code
        self.__delivery_day = delivery_day

    def to_json_dict(self):
        """returns a dictionary with the correct json format"""
        return {
                "tracking_code": self.tracking_code,
                "delivery_day": self.__delivery_day
                }

    @property
    def tracking_code(self):
        """Returns the sha256 signature of the date"""
        return self.__tracking_code

    @tracking_code.setter
    def tracking_code(self, value):
        self.__tracking_code = value

    @property
    def delivery_day(self):
        """Returns the delivery day for the order"""
        return self.__delivery_day
