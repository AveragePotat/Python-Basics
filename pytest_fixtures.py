"""
# TITLE: pytest fixtures

# Created by: Kena D
# Created on: 2025-02-17 
# Last editted on: 2025-02-17

Description:
   Now it’s time to define the unittest methods to test the different functions of the code. 
   The test suite includes tests for the cake’s flavor, size, toppings, ingredients, and price. 
   The first test case in the suite will intentionally provide the wrong value—and that’s what we want! 
   Create specific statements to make sure the program is behaving as it should. 
   That includes providing incorrect data to determine if the program will provide failed results. 
   Because unittest is class-based,  encapsulate these statements into test methods. 

"""

import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)