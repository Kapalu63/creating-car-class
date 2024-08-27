class Car:
  """
  This class represents a car with attributes and methods.
  """
  def __init__(self, make, model, year, color):
    """
    Initializes the car object with the provided details.
    """
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def display_details(self):
    """
    Prints the details of the car in a formatted way.
    """
    print(f"Make: {self.make}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")
    print(f"Color: {self.color}")

  def update_color(self, new_color):
    """
    Updates the color of the car.
    """
    self.color = new_color

def main():
  """
  Main program that demonstrates the Car class functionality.
  """

  # Create car objects with different details
  car1 = Car("Toyota", "Corolla", 2020, "Red")
  car2 = Car("Honda", "Civic", 2022, "Blue")
  car3 = Car("Ford", "Mustang", 2018, "Black")

  # Display details of each car
  print("Car Details:")
  car1.display_details()
  car2.display_details()
  car3.display_details()

  # Update color of car2 and display again
  car2.update_color("Green")
  print("\nCar 2 Updated Details:")
  car2.display_details()

  # User input for a new car
  make = input("Enter car make: ")
  model = input("Enter car model: ")
  year = int(input("Enter car year: "))
  color = input("Enter car color: ")

  # Create a new car object with user input
  new_car = Car(make, model, year, color)

  # Display details of the new car
  print("\nNew Car Details:")
  new_car.display_details()

if __name__ == "__main__":
  main()


"""   CODE EXPLANATION

The code utilizes the core concepts of OOP:
Class: Car defines the blueprint for car objects.

Attributes: make, model, year, color store data about a specific car.

Constructor (init method): __init__(self, make, model, year, color) 
initializes the object's attributes with user-provided values.
Methods:
display_details(self): Prints car information in a formatted way.

update_color(self, new_color): Updates the car's color attribute.

Objects: We create instances (objects) of the Car class with varying attributes.

User Input: The program prompts the user to enter details for a new car
 and creates an object with those details.  """