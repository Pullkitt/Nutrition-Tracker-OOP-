import pandas as pd
from datetime import date

class UserProfile:
    def __init__(self, name, height, weight, dietary_preferences):
        self.name = self.validate_name(name)
        self.height = self.validate_height(height)
        self.weight = self.validate_weight(weight)
        self.dietary_preferences = self.validate_dietary_preferences(dietary_preferences)
        self.daily_goal = None
        self.food_dict = pd.read_csv('food_data.csv').set_index('food').to_dict(orient='index')

    def validate_name(self, name):
        if not name.isalpha():
            raise ValueError("Name must only contain letters.")
        return name

    def validate_height(self, height):
        if not 100 <= height <= 220:
            raise ValueError("Height must be between 100 and 220 cm.")
        return height

    def validate_weight(self, weight):
        if not 20 <= weight <= 200:
            raise ValueError("Weight must be between 20 and 200 kg.")
        return weight

    def validate_dietary_preferences(self, dietary_preferences):
        if not dietary_preferences.isalpha():
            raise ValueError("Dietary preferences must only contain letters.")
        return dietary_preferences

    def calculate_bmi(self):
        """Calculate the user's BMI"""
        bmi = self.weight / (self.height ** 2)
        return bmi

    def print_recommendations(self, bmi):
        """Print dietary recommendations based on the user's BMI"""
        if bmi < 18.5:
            print("Your BMI is below normal. Consider increasing your caloric intake and eating more protein-rich foods.")
        elif bmi >= 18.5 and bmi < 24.9:
            print("Your BMI is normal. Keep up the good work!")
        elif bmi >= 25 and bmi < 29.9:
            print("Your BMI is above normal. Consider reducing your caloric intake and eating more fruits, vegetables, and whole grains.")
        else:
            print("Your BMI is in the obese range. Consider consulting a dietitian or healthcare professional for personalized advice.")

    def print_nutrient_info(self, calories, protein, carbs, fat):
        """Print the nutrient information for the user"""
        print(f"Calories: {calories:.2f}")
        print(f"Protein: {protein:.2f}g")
        print(f"Carbohydrates: {carbs:.2f}g")
        print(f"Fat: {fat:.2f}g")

    def get_food_data(self):
        """Get the nutrient information for the user's daily food intake"""
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0

        while True:
            food = input("Enter a food you ate today (or 'done' to finish): ").lower()
            if food == "done":
                break
            if food in self.food_dict:
                weight = float(input(f"How much {food} did you eat (in grams): "))
                # Calculate the nutrient information based on the weight
                food_info = self.food_dict[food]
                ratio = weight / 100 # Assuming the food_dict values are per 100 grams
                total_calories += food_info["calories"] * ratio
                total_protein += float(food_info["protein"]) * ratio
                total_carbs += float(food_info["carbs"]) * ratio
                total_fat += float(food_info["fat"]) * ratio
            else:
                print(f"Sorry, {food} is not in our database.")
        # Print the total nutrient information
        self.print_nutrient_info(total_calories, total_protein, total_carbs, total_fat)

    def set_daily_goal(self):
        """Set a daily calorie goal for the user"""
        goal = float(input("Enter your daily calorie goal: "))
        self.daily_goal = goal
        print(f"Daily calorie goal set to {goal} for {self.name}.")

    def get_food_data(self):
        """Get the nutrient information for the user's daily food intake"""
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0

        while True:
            food = input("Enter a food you ate today (or 'done' to finish): ").lower()
            if food == "done":
                break
            if food in self.food_dict:
                weight = float(input(f"How much {food} did you eat (in grams): "))
                # Calculate the nutrient information based on the weight
                food_info = self.food_dict[food]
                ratio = weight / 100 # Assuming the food_dict values are per 100 grams
                total_calories += food_info["calories"] * ratio
                total_protein += food_info["protein"] * ratio
                total_carbs += food_info["carbs"] * ratio
                total_fat += food_info["fat"] * ratio
            else:
                print(f"Sorry, {food} is not in our database.")
        # Print the total nutrient information
        self.print_nutrient_info(total_calories, total_protein, total_carbs, total_fat)

    def set_daily_goal(self):
        """Set a daily calorie goal for the user"""
        goal = float(input("Enter your daily calorie goal: "))
        self.daily_goal = goal
        print(f"Daily calorie goal set to {goal} for {self.name}.")

def main():
    user_data = {}
    while True:
        print("\nWelcome to the Nutrition Tracker!")
        print("1. Create a new profile")
        print("2. Load an existing profile")
        print("3. Calculate BMI")
        print("4. Get nutrient information")
        print("5. Set daily calorie goal")
        print("6. Exit")
        choice = int(input("Enter the number of the option you want to select: "))
        if choice == 1:
            name = input("Enter your name: ")
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))
            dietary_preferences = input("Enter any dietary preferences (e.g., vegetarian, vegan): ")
            user_data[name] = UserProfile(name, height, weight, dietary_preferences)
            print(f"Profile created for {name}!")
        elif choice == 2:
            name = input("Enter the name of the profile you want to load: ")
            if name in user_data:
                profile = user_data[name]
                print(f"Profile loaded for {name}!")
                print(f"Height: {profile.height}m")
                print(f"Weight: {profile.weight}kg")
                print(f"Dietary preferences: {profile.dietary_preferences}")
                if profile.daily_goal:
                    print(f"Daily calorie goal: {profile.daily_goal}")
            else:
                print("Profile not found. Please create a new profile.")
        elif choice == 3:
            name = input("Enter the name of the profile you want to calculate BMI for: ")
            if name in user_data:
                profile = user_data[name]
                bmi = profile.calculate_bmi()
                print(f"BMI for {name}: {bmi}")
                profile.print_recommendations(bmi)
            else:
                print("Profile not found. Please create a new profile.")
        elif choice == 4:
            name = input("Enter the name of the profile you want to get nutrient information for: ")
            if name in user_data:
                profile = user_data[name]
                profile.get_food_data()
            else:
                print("Profile not found. Please create a new profile.")
        elif choice == 5:
            name = input("Enter the name of the profile you want to set a daily calorie goal for: ")
            if name in user_data:
                profile = user_data[name]
                profile.set_daily_goal()
            else:
                print("Profile not found. Please create a new profile.")
        elif choice == 6:
            break

if __name__ == "__main__":
    main()
