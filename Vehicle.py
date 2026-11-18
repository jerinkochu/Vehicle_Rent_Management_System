from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,vehicle_name,days,rent_price):
        self.vehicle_name=vehicle_name
        self.__rent_price=rent_price
        self.days=days

    @abstractmethod
    def calculate_rent(self):
        pass
    @property
    def rent_price(self):
        return self.__rent_price
    
    @rent_price.setter
    def rent_price(self,charge):
        if charge<=0:
             raise"Charge should be Positive"
        self.__rent_price=charge


    def display_vehicle_detail(self):
         print(f"{self.vehicle_name},{self.days},{self.rent_price}")