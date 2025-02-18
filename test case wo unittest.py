"""
# TITLE: Test Case w/o unittet

# Created by: Kena D
# Created on: 2025-02-17 
# Last editted on: 2025-02-17

Description:
    Let’s look at a test case example where the Python code simulates a cake factory and performs different functions. 
    These include choosing different sizes and flavors of a cake, including small, medium, and large, and chocolate or vanilla. 
    In addition, the simple class allows developers to add sprinkles or cherries to the cake, return a list of ingredients, 
    and return the price of the cake based on size and toppings. Run the following code: 

"""

from typing import List


class CakeFactory:
 def __init__(self, cake_type: str, size: str):
   self.cake_type = cake_type
   self.size = size
   self.toppings = []

   # Price based on cake type and size
   self.price = 10 if self.cake_type == "chocolate" else 8
   self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

 def add_topping(self, topping: str):
     self.toppings.append(topping)
     # Adding 1 to the price for each topping
     self.price += 1

 def check_ingredients(self) -> List[str]:
     ingredients = ['flour', 'sugar', 'eggs']
     ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
     ingredients += self.toppings
     return ingredients

 def check_price(self) -> float:
     return self.price

# Example of creating a cake and adding toppings
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()


cake_ingredients, cake_price