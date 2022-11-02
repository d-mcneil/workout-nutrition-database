class Food:
    def __init__(self, serving_grams_size, food_name='', food_classification='', food_brand='',
                 serving_other_size=None, serving_other_unit=None, per_package_servings=None,
                 per_package_price=None, fat=0.0, saturated_fat=0.0, trans_fat=0.0,
                 polyunsaturated_fat=None, monounsaturated_fat=None, cholesterol=0.0, sodium=0.0, carbohydrates=0.0,
                 fiber=0.0, soluble_fiber=None, insoluble_fiber=None, sugars=0.0, added_sugars=0.0, sugar_alcohol=None,
                 protein=0.0, calcium=0.0, iron=0.0, potassium=0.0, phosphorous=0.0, magnesium=0.0, fluoride=0.0):
        def calculate_calories(fat, protein, net_carbohydrates, sugar_alcohol, fiber, insoluble_fiber):
            return 9 * fat + 4 * (protein + net_carbohydrates) + 2.6 * sugar_alcohol + 2 * (fiber - insoluble_fiber)

        def calculate_net_carbohydrates(carbohydrates, fiber, sugar_alcohol):
            return carbohydrates - fiber - sugar_alcohol

        self.food_name = food_name
        self.food_classification = food_classification
        self.food_brand = food_brand
        self.serving_grams_size = serving_grams_size
        self.serving_other_size = serving_other_size
        self.serving_other_unit = serving_other_unit
        self.per_package_servings = per_package_servings
        self.per_package_price = per_package_price

        self.fat_per_serving = fat
        self.saturated_fat_per_serving = saturated_fat
        self.trans_fat_per_serving = trans_fat
        self.polyunsaturated_fat_per_serving = polyunsaturated_fat
        self.monounsaturated_fat_per_serving = monounsaturated_fat
        self.cholesterol_per_serving = cholesterol
        self.sodium_per_serving = sodium
        self.carbohydrates_per_serving = carbohydrates
        self.fiber_per_serving = fiber
        self.soluble_fiber_per_serving = soluble_fiber
        self.insoluble_fiber_per_serving = insoluble_fiber
        self.sugars_per_serving = sugars
        self.added_sugars_per_serving = added_sugars
        self.sugar_alcohol_per_serving = sugar_alcohol
        self.protein_per_serving = protein
        self.calcium_per_serving = calcium
        self.iron_per_serving = iron
        self.potassium_per_serving = potassium
        self.phosphorous_per_serving = phosphorous
        self.magnesium_per_serving = magnesium
        self.fluoride_per_serving = fluoride

        self.net_carbohydrates_per_serving = calculate_net_carbohydrates(self.carbohydrates_per_serving,
                                                                         self.fiber_per_serving,
                                                                         self.sugar_alcohol_per_serving)
        self.calories_per_serving = calculate_calories(self.fat_per_serving, self.protein_per_serving,
                                                       self.net_carbohydrates_per_serving,
                                                       self.sugar_alcohol_per_serving, self.fiber_per_serving,
                                                       self.insoluble_fiber_per_serving)

        self.nutrition_facts_per_serving = {
            'fat_per_serving': self.fat_per_serving,
            'saturated_fat_per_serving': self.saturated_fat_per_serving,
            'trans_fat_per_serving': self.trans_fat_per_serving,
            'polyunsaturated_fat_per_serving': self.polyunsaturated_fat_per_serving,
            'monounsaturated_fat_per_serving': self.monounsaturated_fat_per_serving,
            'cholesterol_per_serving': self.cholesterol_per_serving,
            'sodium_per_serving': self.sodium_per_serving,
            'carbohydrates_per_serving': self.carbohydrates_per_serving,
            'fiber_per_serving': self.fiber_per_serving,
            'soluble_fiber_per_serving': self.soluble_fiber_per_serving,
            'insoluble_fiber_per_serving': self.insoluble_fiber_per_serving,
            'sugars_per_serving': self.sugars_per_serving,
            'added_sugars_per_serving': self.added_sugars_per_serving,
            'sugar_alcohol_per_serving': self.sugar_alcohol_per_serving,
            'protein_per_serving': self.protein_per_serving,
            'calcium_per_serving': self.calcium_per_serving,
            'iron_per_serving': self.iron_per_serving,
            'potassium_per_serving': self.potassium_per_serving,
            'phosphorous_per_serving': self.phosphorous_per_serving,
            'magnesium_per_serving': self.magnesium_per_serving,
            'fluoride_per_serving': self.fluoride_per_serving,
            'net_carbohydrates_per_serving': self.net_carbohydrates_per_serving,
            'calories_per_serving': self.calories_per_serving}

    def eat(self, portion_size, portion_unit='grams'):
        return EatFood(self, portion_size, portion_unit)


class EatFood(Food):
    def __init__(self, food_object, portion_size, portion_unit='grams'):
        Food.__init__(self, food_object.serving_grams_size,
                      food_object.fat_per_serving,
                      food_object.saturated_fat_per_serving,
                      food_object.trans_fat_per_serving,
                      food_object.polyunsaturated_fat_per_serving,
                      food_object.monounsaturated_fat_per_serving,
                      food_object.cholesterol_per_serving,
                      food_object.sodium_per_serving,
                      food_object.carbohydrates_per_serving,
                      food_object.fiber_per_serving,
                      food_object.soluble_fiber_per_serving,
                      food_object.insoluble_fiber_per_serving,
                      food_object.sugars_per_serving,
                      food_object.added_sugars_per_serving,
                      food_object.sugar_alcohol_per_serving,
                      food_object.protein_per_serving,
                      food_object.calcium_per_serving,
                      food_object.iron_per_serving,
                      food_object.potassium_per_serving,
                      food_object.phosphorous_per_serving,
                      food_object.magnesium_per_serving,
                      food_object.fluoride_per_serving)
        self.portion_size = portion_size
        self.portion_unit = portion_unit
        if self.portion_unit == 'grams':
            self.servings = self.portion_size / food_object.serving_grams_size
        elif self.portion_unit == food_object.serving_other_unit:
            self.servings = self.portion_size / food_object.serving_other_size
        elif self.portion_unit == 'packages':
            self.servings = self.portion_size * food_object.per_package_servings
        elif self.portion_unit == 'servings':
            self.servings = self.portion_size
        else:
            print('Error: serving unit incorrect.')
            raise ValueError
        self.packages = self.servings / food_object.per_package_servings   # potential zero division error
        self.cost = self.packages * food_object.per_package_price

        self.fat = food_object.fat_per_serving * self.servings
        self.saturated_fat = food_object.saturated_fat_per_serving * self.servings
        self.trans_fat = food_object.trans_fat_per_serving * self.servings
        self.polyunsaturated_fat = food_object.polyunsaturated_fat_per_serving * self.servings
        self.monounsaturated_fat = food_object.monounsaturated_fat_per_serving * self.servings
        self.cholesterol = food_object.cholesterol_per_serving * self.servings
        self.sodium = food_object.sodium_per_serving * self.servings
        self.carbohydrates = food_object.carbohydrates_per_serving * self.servings
        self.fiber = food_object.fiber_per_serving * self.servings
        self.soluble_fiber = food_object.soluble_fiber_per_serving * self.servings
        self.insoluble_fiber = food_object.insoluble_fiber_per_serving * self.servings
        self.sugars = food_object.sugars_per_serving * self.servings
        self.added_sugars = food_object.added_sugars_per_serving * self.servings
        self.sugar_alcohol = food_object.sugar_alcohol_per_serving * self.servings
        self.protein = food_object.protein_per_serving * self.servings
        self.calcium = food_object.calcium_per_serving * self.servings
        self.iron = food_object.iron_per_serving * self.servings
        self.potassium = food_object.potassium_per_serving * self.servings
        self.phosphorous = food_object.phosphorous_per_serving * self.servings
        self.magnesium = food_object.magnesium_per_serving * self.servings
        self.fluoride = food_object.fluoride_per_serving * self.servings

        self.net_carbohydrates = food_object.net_carbohydrates_per_serving * self.servings
        self.calories = food_object.calories_per_serving * self.servings

        self.nutrition_facts = {}
        for key, value in food_object.nutrition_facts_per_serving.items():
            self.nutrition_facts[key.replace('_per_serving', '')] = value * self.servings


class Meal:
    def __init__(self, *eaten_food_objects):
        self.fat = 0
        self.saturated_fat = 0
        self.trans_fat = 0
        self.polyunsaturated_fat = 0
        self.monounsaturated_fat = 0
        self.cholesterol = 0
        self.sodium = 0
        self.carbohydrates = 0
        self.fiber = 0
        self.soluble_fiber = 0
        self.insoluble_fiber = 0
        self.sugars = 0
        self.added_sugars = 0
        self.sugar_alcohol = 0
        self.protein = 0
        self.calcium = 0
        self.iron = 0
        self.potassium = 0
        self.phosphorous = 0
        self.magnesium = 0
        self.fluoride = 0
        self.net_carbohydrates = 0
        self.calories = 0
        self.cost = 0
        for eaten_food_object in eaten_food_objects:
            self.fat += eaten_food_object.fat
            self.saturated_fat += eaten_food_object.saturated_fat
            self.trans_fat += eaten_food_object.trans_fat
            self.polyunsaturated_fat += eaten_food_object.polyunsaturated_fat
            self.monounsaturated_fat += eaten_food_object.monounsaturated_fat
            self.cholesterol += eaten_food_object.cholesterol
            self.sodium += eaten_food_object.sodium
            self.carbohydrates += eaten_food_object.carbohydrates
            self.fiber += eaten_food_object.fiber
            self.soluble_fiber += eaten_food_object.soluble_fiber
            self.insoluble_fiber += eaten_food_object.insoluble_fiber
            self.sugars += eaten_food_object.sugars
            self.added_sugars += eaten_food_object.added_sugars
            self.sugar_alcohol += eaten_food_object.sugar_alcohol
            self.protein += eaten_food_object.protein
            self.calcium += eaten_food_object.calcium
            self.iron += eaten_food_object.iron
            self.potassium += eaten_food_object.potassium
            self.phosphorous += eaten_food_object.phosphorous
            self.magnesium += eaten_food_object.magnesium
            self.fluoride += eaten_food_object.fluoride
            self.net_carbohydrates += eaten_food_object.net_carbohydrates
            self.calories += eaten_food_object.calories
            self.cost += eaten_food_object.cost

        # self.fat = round(self.fat, 1)
        # self.saturated_fat = round(self.saturated_fat, 1)
        # self.trans_fat = round(self.trans_fat, 1)
        # self.polyunsaturated_fat = round(self.polyunsaturated_fat, 1)
        # self.monounsaturated_fat = round(self.monounsaturated_fat, 1)
        # self.cholesterol = round(self.cholesterol)
        # self.sodium = round(self.sodium)
        # self.carbohydrates = round(self.carbohydrates, 1)
        # self.fiber = round(self.fiber, 1)
        # self.soluble_fiber = round(self.soluble_fiber, 1)
        # self.insoluble_fiber = round(self.insoluble_fiber, 1)
        # self.sugars = round(self.sugars, 1)
        # self.added_sugars = round(self.added_sugars, 1)
        # self.sugar_alcohol = round(self.sugar_alcohol, 1)
        # self.protein = round(self.protein, 1)
        # self.calcium = round(self.calcium)
        # self.iron = round(self.iron, 1)
        # self.potassium = round(self.potassium)
        # self.phosphorous = round(self.phosphorous)
        # self.magnesium = round(self.magnesium)
        # self.fluoride = round(self.fluoride, 1)
        # self.net_carbohydrates = round(self.net_carbohydrates, 1)
        # self.calories = round(self.calories)
        # self.cost = round(self.cost, 2)

        self.nutrition_facts = {
            'fat': self.fat,
            'saturated_fat': self.saturated_fat,
            'trans_fat': self.trans_fat,
            'polyunsaturated_fat': self.polyunsaturated_fat,
            'monounsaturated_fat': self.monounsaturated_fat,
            'cholesterol': self.cholesterol,
            'sodium': self.sodium,
            'carbohydrates': self.carbohydrates,
            'fiber': self.fiber,
            'soluble_fiber': self.soluble_fiber,
            'insoluble_fiber': self.insoluble_fiber,
            'sugars': self.sugars,
            'added_sugars': self.added_sugars,
            'sugar_alcohol': self.sugar_alcohol,
            'protein': self.protein,
            'calcium': self.calcium,
            'iron': self.iron,
            'potassium': self.potassium,
            'phosphorous': self.phosphorous,
            'magnesium': self.magnesium,
            'fluoride': self.fluoride,
            'net_carbohydrates': self.net_carbohydrates,
            'calories': self.calories}
