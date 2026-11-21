from abc import ABC,abstractmethod                      #import Abstraction method
class Vehicle(ABC):
    def __init__(self,vehicle_name,days,rent_price):        # Initiating Vehicle Characteristics
        self.vehicle_name=vehicle_name
        self.__rent_price=rent_price
        self.days=days

    @abstractmethod                                         #Abstractionmethod is neccessery for defining calculate the rent
    def calculate_rent(self):
        pass
    @property                                               #rent price is an private attribute.
    def rent_price(self):
        return self.__rent_price
    
    @rent_price.setter                                      #prrivate attribute can be set before it changes we are using setter
    def rent_price(self,charge):                            #charge is a new character which depends in rent calculation
        if charge<=0:                                       #we are applying conditions 
             raise"Charge should be Positive"               #raise can be mention error without program interruption
        self.__rent_price=charge


    def display_vehicle_detail(self):
         print(f"{self.vehicle_name},{self.days},{self.rent_price}")