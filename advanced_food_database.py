from advanced_food_database_classes import Food, Meal
from pprint import pprint

greek_yogurt = Food(170, 'greek yogurt', 'dairy', 'chobani', .75, 'cups', 5, 5.49, 0, 0, 0, 0, 0, 10, 65, 6, 0, 0, 0, 4,
                    0, 0, 16, 187, 0, 250)
almond_milk = Food(240, 'almond milk', 'dairy(vegan)', 'almond breeze', 1, 'cup', 8, 3.69, 2.5, 0, 0, .5, 1.5, 0, 170,
                   1, .5, 0, 0, 0, 0, 0, 1, 450, .7, 160, 20, 15, 0)
old_fashioned_oats = Food(40, 'old fashioned oats', 'grain', 'quaker', .5, 'cups', 30, 2.39, 2.5, .5, 0, 1, 1, 0, 0, 27,
                          4, 1, 2, 0, 0, 0, 5, 0, 1.6, 150, 164, 55.2, 0)

plan_greek_yogurt = greek_yogurt.eat(150)
plan_almond_milk = almond_milk.eat(45)
plan_old_fashioned_oats = old_fashioned_oats.eat(35)
pprint(plan_old_fashioned_oats.nutrition_facts, sort_dicts=False)

breakfast = Meal(plan_old_fashioned_oats, plan_almond_milk, plan_greek_yogurt)
# pprint(breakfast.nutrition_facts, sort_dicts=False)
# print(breakfast.cost)
