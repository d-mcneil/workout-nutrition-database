from food_database_classes_base import Food, Meal
from pprint import pprint

greek_yogurt = Food(170,0,0,0,0,0,10,65,6,0,0,0,4,0,0,16,187,0,250)
almond_milk = Food(240,2.5,0,0,.5,1.5,0,170,1,.5,0,0,0,0,0,1,450,.7,160,20,15,0)
old_fashioned_oats = Food(40,2.5,.5,0,1,1,0,0,27,4,1,2,0,0,0,5,0,1.6,150,164,55.2,0)

plan_greek_yogurt = greek_yogurt.eat_food(150)
plan_almond_milk = almond_milk.eat_food(45)
plan_old_fashioned_oats = old_fashioned_oats.eat_food(35)

breakfast = Meal(plan_old_fashioned_oats, plan_almond_milk, plan_greek_yogurt)
# pprint(breakfast.nutrition_facts, sort_dicts=False)
print(plan_greek_yogurt.calories)

