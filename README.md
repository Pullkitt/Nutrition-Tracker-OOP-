# Nutrition-Tracker-OOP
The Nutrition Tracker is an interactive application designed to help users manage and track their daily nutritional intake using Object-Oriented Programming (OOP) principles. 

This code defines a UserProfile class that represents a user's nutritional profile, including their name, height, weight, dietary preferences, and daily caloric goal. The class also includes methods for calculating the user's BMI, printing nutrient information, and getting food data.

The code imports the math module for mathematical functions and the pandas module for reading and manipulating CSV files.

The UserProfile class has the following methods:

# __init__(self, name, height, weight, dietary_preferences):
Initializes a new UserProfile instance with the given name, height, weight, and dietary preferences. It also loads a food database from a CSV file and converts it to a dictionary for easy lookup.
# calculate_bmi(self):
Calculates the user's BMI based on their height and weight.
# print_recommendations(self, bmi):
Prints dietary recommendations based on the user's BMI.
# print_nutrient_info(self, calories, protein, carbs, fat): 
Prints nutrient information for the given caloric, protein, carbohydrate, and fat values.
# get_food_data(self): 
Gets food data from the user by prompting them to enter foods they ate today and their weights in grams. It calculates the total calories, protein, carbohydrates, and fat based on the food database and prints the nutrient information.
# run(self):
Runs the nutrition tracker by displaying a menu of options and prompting the user to select an option. The available options are to calculate BMI, calculate caloric intake, print recommendations, and exit.
# The main() 
function prompts the user to enter their profile information, dietary preferences, and daily caloric goal. It then creates a new UserProfile instance with the given information and calls its run() method to start the nutrition tracker.

# The code uses several concepts, including:
# Classes and objects: 
The UserProfile class defines a template for creating user profile objects.
Methods: The UserProfile class includes several methods that perform specific tasks, such as calculating BMI or getting food data.
# Exceptions: 
The code uses exceptions to handle invalid input, such as non-numeric values for height or weight.
# Dictionaries:
The code uses a dictionary to store the food database for easy lookup.
# Modules:
The code imports the math and pandas modules to perform mathematical functions and read CSV files, respectively.
# Input/output: 
The code prompts the user to enter information and prints nutrient information and recommendations based on their input.
# Conditional statements: 
The code uses conditional statements to check for valid input and to determine which recommendations to print based on the user's BMI.
# Loops: 
The code uses loops to repeatedly prompt the user for food data until they enter "done".
