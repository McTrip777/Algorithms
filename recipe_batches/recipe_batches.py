#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipeItem = list(recipe.keys())
  recipeValue = list(recipe.values())
  ingredientsItem = list(ingredients.keys())
  ingredientsQuantity = list(ingredients.values())
  newValues = []
  if len(recipeItem) > len(ingredientsItem):
    batches = 0
    return batches
  else:
    for i in range(0, len(recipeItem)-1):
      if recipeValue[i] <= ingredientsQuantity[i]:
        while ingredientsQuantity[i] >= recipeValue[i]:
          x = ingredientsQuantity[i]/recipeValue[i]
          newValues.append(x)
      else:
        batches = 0
      

  return batches


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

print(recipe_batches(recipe, ingredients))