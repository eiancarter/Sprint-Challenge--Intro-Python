# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the base class -

class Vehicle:
    def __init__(self, type):
        self.type = type

class GroundVehicle(Vehicle):
    def __init__(self, type, ground_type):
        super().__init__(type)
        self.ground_type = ground_type

class FlightVehicle(Vehicle):
    def __init__(self, type, air_type):
        super().__init__(type)
        self.air_type = air_type

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class StarShip(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
    
    
