# This is a code written by Asikpo Collins Ekpenyong.

import math
import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Formula for volume of a tire: V = π * width * aspect_ratio * (width + (aspect_ratio * diameter)) / 1000
    volume = math.pi * width * aspect_ratio * (width + (aspect_ratio * diameter)) / 1000
    return volume

def main():
    # Get user input for tire specifications
    width = float(input("Enter the width of the tire: "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
    diameter = float(input("Enter the diameter of the wheel: "))

    # Calculate tire volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"Approximate volume of the tire: {volume:.2f} cubic centimeters")

    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Append data to volumes.txt
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date} {width} {aspect_ratio} {diameter} {volume:.2f}\n")

if __name__ == "__main__":
    main()
