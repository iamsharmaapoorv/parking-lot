from parking_lot import ParkingLot
from vehicles.car import Car
from vehicles.bike import Bike

lot = ParkingLot(6, 6)
bike = Bike("111", "red")
print("created bike")

lot.park(bike, 1)

print(lot.parked_vehicles)
print(lot.colour_slots)

car = Car("222", "red")
lot.park(car, 0)
print("created car")

print(lot.parked_vehicles)
print(lot.colour_slots)

lot.vacate((0, 0))

print(lot.parked_vehicles)
print(lot.colour_slots)
