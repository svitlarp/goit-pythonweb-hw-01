from abc import ABC, abstractmethod

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model}: Двигун запущено")

# class Motorcycle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model}: Мотор заведено")

# # Використання
# vehicle1 = Car("Toyota", "Corolla")
# vehicle1.start_engine()

# vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
# vehicle2.start_engine()


# Abstract Product
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

#  Concrete products
class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Двигун запущено")
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Мотор заведено") 


# Abstract Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

# Concrete Factories
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        spec = "US Spec"
        return Car(make, model, spec)
    
    def create_motorcycle(self, make, model):
        spec = "US Spec"
        return Motorcycle(make, model, spec)
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        spec ="EU Spec"
        return Car(make, model, spec)
    
    def create_motorcycle(self, make, model):
        spec = "EU Spec"
        return Motorcycle(make, model, spec)

#  Client COde
us_vehicle_factory = USVehicleFactory()
eu_vehicle_factory = EUVehicleFactory()

us_car = us_vehicle_factory.create_car("Toyota", "Corolla")
us_moto = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_car.start_engine()
us_moto.start_engine()

eu_car = eu_vehicle_factory.create_car("Toyota", "Corolla")
eu_moto = eu_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
eu_car.start_engine()
eu_moto.start_engine()
