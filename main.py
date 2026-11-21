from Vehicle import Vehicle
from Car import Car                 #for Importing module from file :Car
from Bike import Bike               #for Importing module from file :Bike

car=Car('Toyota',3,2000)            #We are Car giving Details into Sublass 
bike=Bike('Fz',3,1000)

print('\n')
print('-------- Car --------')
print(f" Vehicle Name = {car.vehicle_name} " )
print(f" Rental Days = {car.days} ")
print(f" Rental Price = {car.rent_price} /Day")
car.calculate_rent(500)                         #Calling Caalculate Rent 500 be the charge as we defined in Equation
print('\n')
print('-------- Bike --------')
print(f" Vehicle Name = {bike.vehicle_name}" )
print(f" Rental Days = {bike.days}")
print(f" Rental Price = {bike.rent_price} /Day")
bike.calculate_rent(100)



#-----------------------------------------------------
#--------------O U T P U T----------------------------
#-----------------------------------------------------

#File Path :
#(.venv) jerinkjohn@Jerins-MacBook-Air Project_Vehicle % /Users/jerinkjohn/Desktop/PGP_Data_Science_AIML/Project_Vehicle/.venv/bin/python /Users
# /jerinkjohn/Desktop/PGP_Data_Science_AIML/Project_Vehicle/main.py

# Result :

# -------- Car --------
#  Vehicle Name = Toyota 
#  Rental Days = 3 
#  Rental Price = 2000 /Day
#  Car Rent = 6500 for 3 days (+500)


# -------- Bike --------
#  Vehicle Name = Fz
#  Rental Days = 3
#  Rental Price = 1000 /Day
#  Bike Rent = 3100 for 3 days (+100)