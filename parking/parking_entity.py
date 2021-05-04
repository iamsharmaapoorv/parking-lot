from abc import ABC, abstractmethod


class ParkingEntity(ABC):

    @abstractmethod
    def park(self):
        pass

    @abstractmethod
    def vacate(self):
        pass

    @abstractmethod
    def is_full(self):
        pass
