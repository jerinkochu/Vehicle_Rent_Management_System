from Vehicle import Vehicle

class Bike(Vehicle):
     def calculate_rent(self,charge):
          price=(self.rent_price*self.days)+charge
          print(f" Bike Rent = {price} for 3 days (+100)")

     def display_vehicle_detail(self):
          print(f"{self.vehicle_name},{self.days},{self.rent_price}")