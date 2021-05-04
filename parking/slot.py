from parking.parking_entity import ParkingEntity


class Slot(ParkingEntity):
    def __init__(self):
        self.capacity = 4
        self.parked_vehicles = set()

    def park(self, vehicle):
        space = vehicle.vehicle_type.value
        if self.capacity < space:
            # ideal way would be to raise a custom exception
            print("Not enough space remaining in this slot")
            return

        self.parked_vehicles.add(vehicle)
        self.capacity -= space

    def has_space(self, space):
        return self.capacity >= space

    def is_full(self):
        return True if self.capacity == 0 else False

    def is_empty(self):
        return self.capacity == 4

    def vacate(self, vehicle):
        space = vehicle.vehicle_type.value
        self.parked_vehicles.remove(vehicle)
        self.capacity += space
