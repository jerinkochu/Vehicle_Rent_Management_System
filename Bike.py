from Vehicle import Vehicle                  #importing Parent class Vehicle from File

class Bike(Vehicle):                         #Bike be the Subclass and Vehicle is the Inheritance
     def calculate_rent(self,charge):
          price=(self.rent_price*self.days)+charge
          print(f" Bike Rent = {price} for 3 days (+100)")

     def display_vehicle_detail(self):                                #calling Display vehicle detail from Class
          print(f"{self.vehicle_name},{self.days},{self.rent_price}")