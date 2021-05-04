from vehicles.vehicle_type import VehicleType
from vehicles.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, registration_number, colour):
        super().__init__(registration_number, VehicleType.CAR, colour)
