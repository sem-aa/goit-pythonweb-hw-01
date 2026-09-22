from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


US_SPEC = "US Spec"
EU_SPEC = "EU Spec"


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({US_SPEC})")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({US_SPEC})")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} ({EU_SPEC})")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} ({EU_SPEC})")


usCar = USVehicleFactory().create_car("Toyota", "Camry")
usMotorcycle = USVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
euCar = EUVehicleFactory().create_car("Volkswagen", "Golf")
euMotorcycle = EUVehicleFactory().create_motorcycle("BMW", "R1200GS")

usCar.start_engine()
usMotorcycle.start_engine()
euCar.start_engine()
euMotorcycle.start_engine()
