# water_flow.py by Collins Ekpenyong ASikpo

# Constants
GRAVITY_ACCELERATION = 9.80665  # m/s^2
DENSITY_OF_WATER = 998.2  # kg/m^3

# Task 1: Water Column Height Calculation
def water_column_height(tower_height, tank_height):
    h = tower_height + 3 * tank_height / 4
    return h

# Task 2: Pressure Gain from Water Height Calculation
def pressure_gain_from_water_height(height):
    # Pressure calculation
    pressure = (DENSITY_OF_WATER * GRAVITY_ACCELERATION * height) / 1000  # in kilopascals
    return pressure

# Task 3: Pressure Loss from Pipe Calculation
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Pressure loss calculation
    pressure_loss = -(friction_factor * pipe_length * DENSITY_OF_WATER * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

# Task 4: Pressure Loss from Fittings Calculation
def pressure_loss_from_fittings(fitting_loss_coefficient, fluid_velocity):
    # Pressure loss from fittings calculation
    pressure_loss = 0.5 * fitting_loss_coefficient * DENSITY_OF_WATER * fluid_velocity**2
    return pressure_loss

# Task 5: Reynolds Number Calculation
def reynolds_number(pipe_diameter, fluid_velocity, dynamic_viscosity):
    # Reynolds number calculation
    reynolds = (DENSITY_OF_WATER * fluid_velocity * pipe_diameter) / dynamic_viscosity
    return reynolds

# Task 6: Pressure Loss from Pipe Reduction Calculation
def pressure_loss_from_pipe_reduction(original_diameter, new_diameter, pipe_length, fluid_velocity):
    # Pressure loss from pipe reduction calculation
    pressure_loss = (0.5 * DENSITY_OF_WATER * fluid_velocity**2 * (original_diameter**2 - new_diameter**2)) / original_diameter**2
    return pressure_loss

# Task 7: Main Function
def main():
    # Get user input
    tower_height = float(input("Enter tower height: "))
    tank_height = float(input("Enter tank height: "))
    water_height = water_column_height(tower_height, tank_height)

    # Call other functions
    water_pressure = pressure_gain_from_water_height(water_height)
    print(f"Water Pressure: {water_pressure} kPa")

    pipe_diameter = float(input("Enter pipe diameter: "))
    pipe_length = float(input("Enter pipe length: "))
    friction_factor = float(input("Enter friction factor: "))
    fluid_velocity = float(input("Enter fluid velocity: "))
    
    pipe_loss = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    print(f"Pressure Loss from Pipe: {pipe_loss} kPa")

