#!/usr/bin/python

import math

# Problem: We want to see how many batches of the recipe we can make with the ingredients provided

def recipe_batches(recipe, ingredients):
  # Variable for total batches
  batches = 0
  # Stores list of maximum amount of batches per ingredient
  batch_quotient = []
  # Uses to test which is the smallest quotient amongst batch quotient
  smallest_quotient = float("inf")

  # if the len(recipe) != len(ingredients)
  if len(ingredients) != len(recipe):
    batches = 0
    return batches
    # return 0

  #  Loop through recipe & items
  for (recipe_key,recipe_value), (ingredients_key, ingredients_value) in zip(recipe.items(), ingredients.items()):
    #  Round down the quotient of required ingredients vs ingredients on hand
    print(f"recipe {recipe_value}, ingredients {ingredients_value}")
    # append quotients to new array
    batch_quotient.append(ingredients_value //  recipe_value) 
    #  else we need to loop through recipe 

# Loop through to check which is the smallest quotient
  for i in range(len(batch_quotient)):
    print(smallest_quotient)
    if batch_quotient[i] < smallest_quotient:
      smallest_quotient = batch_quotient[i]
    
    # set batches to smallest quotient. You can only make as many recipes as the least amount of ingredients you have
    batches = smallest_quotient
  print(f"quotient {batch_quotient}")
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 200, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))