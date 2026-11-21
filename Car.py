from Vehicle import Vehicle                       #importing Parent class Vehicle from File
class Car(Vehicle):                               #Car is a subclass and Vehicle be the Inhheritance
     def calculate_rent(self,charge):                                 #defining Calculate rent from parent class
          price=(self.rent_price*self.days)+charge                    #Equation for Bike rent 
          print(f" Car Rent = {price} for 3 days (+500)")

     def display_vehicle_detail(self):                                #Vehicle detail definition from parent class
          print(f"{self.vehicle_name},{self.days},{self.rent_price}")