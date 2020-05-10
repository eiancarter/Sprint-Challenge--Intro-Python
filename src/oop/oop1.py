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
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
    pass

class GroundVehicle(Vehicle):
    # def __init__(self, vehicle, ground_vehicle):
    #     super().__init__(vehicle)
    #     self.ground_vehicle = ground_vehicle
    pass

class FlightVehicle(Vehicle):
    # def __init__(self, vehicle, flight_vehicle):
    #     super().__init__(vehicle)
    #     self.flight_vehicle = flight_vehicle
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
    
    
