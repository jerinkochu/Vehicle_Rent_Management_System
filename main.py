from Vehicle import Vehicle
from Car import Car
from Bike import Bike

car=Car('Toyota',3,2000)
bike=Bike('Fz',3,1000)

print('\n')
print('-------- Car --------')
print(f" Vehicle Name = {car.vehicle_name} " )
print(f" Rental Days = {car.days} ")
print(f" Rental Price = {car.rent_price} /Day")
car.calculate_rent(500)
print('\n')
print('-------- Bike --------')
print(f" Vehicle Name = {bike.vehicle_name}" )
print(f" Rental Days = {bike.days}")
print(f" Rental Price = {bike.rent_price} /Day")
bike.calculate_rent(100)