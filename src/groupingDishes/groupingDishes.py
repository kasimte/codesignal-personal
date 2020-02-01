'''You are given a list dishes, where each element consists of a list of
strings beginning with the name of the dish, followed by all the
ingredients used in preparing it. You want to group the dishes by
ingredients, so that for each ingredient you'll be able to find all
the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the
ingredient name, followed by the names of all the dishes that contain
this ingredient. The dishes inside each list should be sorted
lexicographically, and the result array should be sorted
lexicographically by the names of the ingredients.

Example

For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
For
  dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Chicken", "Chicken Curry", "Quesadilla"],
                            ["Nuts", "Fried Rice", "Salad"],
                            ["Onions", "Fried Rice", "Pasta"]]
'''

def groupingDishes(dishes):
    '''
    Approach:
    - establish hash
    - iterate over each dish
    - for each dish:
      - grab the name of the dish
      - for each ingredient, store in a hash: ingredient -> [array of dishes]
    - sort they keys of the hash
    - iterate over the sorted keys and add to an output results array
      - [ingredient, sorted list of dishes]
    - return
    '''

    hash = {}
    
    for dish in dishes:
        dish_name = dish[0] # assumes at least dish name and ingredient
        for i in dish[1:]:
            if i in hash:
                hash[i].append(dish_name)
            else:
                hash[i] = [dish_name]
    
    ingredients = list(hash)
    ingredients.sort()
    
    result = []
    for i in ingredients:
        dishes = hash[i]
        if len(dishes) > 1:
            dishes.sort()
            result.append([i] + dishes)

    return result

'''
Log: Solved in 19 minutes on first try.
'''
