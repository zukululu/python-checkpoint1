# #1: Define a Vehicle class with the following attributes and methods: 
# - `vehicle_type` 'str'
# - `wheel_count` 'int'
# - `name` 'str'
# - `cost` 'int'
# - `colors` 'str'
# - `vehicle_brand` 'str'
# - `mpg` 'dict', with the following properties:
#     - `city` 'int'
#     - `highway` 'int'
#     - `combined` 'int'
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_drive` for that class is "no wheels!" then it
#     should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_drive  + " wheel drive"

# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `can_pop_wheelie` 'bool', if `wheel_count` is not equal to 2 then it should be
#   False

# #3: Define a Car class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `can_drive` that should return 'Vrrooooom Vroooom"'

# #4: Define a Truck class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `rev_engine` that should return 'revvvvvreeeev'

# Commit when you finish working on these questions!