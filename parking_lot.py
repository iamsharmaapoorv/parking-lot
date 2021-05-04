from collections import deque, defaultdict
from parking.parking_entity import ParkingEntity
from parking.slot import Slot
from parking.directions import Directions


class ParkingLot(ParkingEntity):

    def __init__(self, length, breadth):  # following 0 index approach for now
        self.length = length
        self.breadth = breadth
        self.entrypoints = {0: (0, 0),
                            1: (0, breadth-1),
                            2: (length-1, breadth-1),
                            3: (length-1, 0)}
        self.parked_vehicles = {}
        self.colour_slots = defaultdict(set)
        self.slots = [[Slot() for vertical in range(breadth)]
                      for horizontal in range(length)]
        self.capacity = length * breadth
        print("created lot")

    def park(self, vehicle, entrypoint):
        if self.is_full():
            # ideal way would be to raise a custom exception
            print("Parking Lot is full.")
            return

        if vehicle.registration_no in self.parked_vehicles:
            # ideal way would be to raise a custom exception
            print("This vehicle is already parked.")
            return

        space = vehicle.vehicle_type.value  # create func in vehicle.py that returns space
        queue = deque()
        queue.append(self.entrypoints[entrypoint])

        while queue:
            cur_location = queue.pop()
            print(cur_location)
            cur_slot = self.slots[cur_location[0]][cur_location[1]]
            if cur_slot.has_space(space):
                cur_slot.park(vehicle)
                self.colour_slots[vehicle.colour].add(cur_location)
                self.parked_vehicles[vehicle.registration_no] = cur_location
                if cur_slot.is_full:
                    self.capacity -= 1
                print("parked succesfully")
                return

            for direction in Directions:
                new_location = (
                    cur_location[0]+direction.value[0], cur_location[1]+direction.value[1])
                if self.check_in_bounds(new_location):
                    queue.append(new_location)

        print("Unable to park")

    def vacate(self, slot):
        # PDF asks to vacate slot wise, better way would be to vacate vehicle wise
        if not self.check_in_bounds(slot):
            print("Invalid slot")
            return

        cur_slot = self.slots[slot[0]][slot[1]]
        if cur_slot.is_empty():
            print("Slot is already vacant")
            return

        self.capacity += 1

        for vehicle in cur_slot.parked_vehicles:
            del self.parked_vehicles[vehicle.registration_no]
            self.colour_slots[vehicle.colour].remove(slot)

        cur_slot.parked_vehicles = set()

        print("vacated successfully")

    def is_full(self):
        return True if self.capacity == 0 else False

    def get_colour_slots(self):
        pass

    def get_vehicle_slot(self):
        pass

    def check_in_bounds(self, location):  # static method
        if location[0] >= self.length or location[0] < 0:
            return False
        if location[1] >= self.breadth or location[1] < 0:
            return False
        return True
