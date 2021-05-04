from abc import ABC

class Vehicle(ABC):
    def __init__(self, registration_no, vehicle_type, colour):   # can also subclass into specific vehicle types and make this abstract
        self.registration_no = registration_no
        self.vehicle_type = vehicle_type
        self.colour = colour
