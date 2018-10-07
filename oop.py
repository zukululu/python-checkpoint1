# oop.py
# Create 4 classes
# - vehicle
# - car
# - motorcycle
# - truck

# All other classes (car, motorcycle, truck) should inherit vehicle

# Vehicle
# should have the following attributes with the associated data types (these should be inherited  in to its child classes)
# - vehicle_type 'str'
# - wheel_count 'int'
# - name 'str'
# - cost 'int'
# - colors 'str'
# - vehicle_brand 'str'
# - mpg 'dict' with the following properties:
#     - city 'int'
#     - highway 'int'
#     - combined 'int'
# should have the following methods
# - get_vehicle_type
#     should return the classes vehicle_type
# - get_vehicle_brand
#     should return the classes vehicle_brand
# - get_vehicle_drive
#     if the wheel_drive for that class is "no wheels!" then it should return
#         "no wheels send it back to the shop"
#     otherwise it should return 
#         "I have "  + self.wheel_drive  + " wheel drive"

# The Motorcycle class
# should have the following attributes and associatied data types
# - wheel_drive 'str', defaults to "no wheels!"
# - can_pop_wheelie 'bool', if wheel_count is not equal to 2 then it should be False

# The Car  class
# should have the following attributes and associatied data types
# - wheel_drive 'str', defaults to "no wheels!"
# should have the following methods
# - can_drive that should return 'Vrrooooom Vroooom"'

# The Truck class
# should have the following attributes and associatied data types
# - wheel_drive 'str', defaults to "no wheels!"
# should have the following methods
# - rev_engine that should return 'revvvvvreeeev'