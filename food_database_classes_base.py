# later add other types of servings besides grams, price per package, and servings per package

class Food:
    def __init__(self, serving_size_grams, fat=0.0, saturated_fat=0.0, trans_fat=0.0,
                 polyunsaturated_fat=None, monounsaturated_fat=None, cholesterol=0.0, sodium=0.0, carbohydrates=0.0,
                 fiber=0.0, soluble_fiber=None, insoluble_fiber=None, sugars=0.0, added_sugars=0.0, sugar_alcohol=None,
                 protein=0.0, calcium=0.0, iron=0.0, potassium=0.0, phosphorous=0.0, magnesium=0.0, flouride=0.0):

        def calculate_calories(fat, protein, net_carbohydrates, sugar_alcohol, fiber, insoluble_fiber):
            return 9*fat + 4*(protein + net_carbohydrates) + 2.6*sugar_alcohol + 2*(fiber - insoluble_fiber)

        def calculate_net_carbohydrates(carbohydrates, fiber, sugar_alcohol):
            return carbohydrates - fiber - sugar_alcohol

        self.serving_size_grams = serving_size_grams

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
        self.flouride_per_serving = flouride

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
            'flouride_per_serving': self.flouride_per_serving,
            'net_carbohydrates_per_serving': self.net_carbohydrates_per_serving,
            'calories_per_serving': self.calories_per_serving}

    def eat_food(self, grams_eaten):
        return EatFood(self, grams_eaten)


class EatFood(Food):
    def __init__(self, food_object, grams_eaten):
        Food.__init__(self, food_object.serving_size_grams,
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
                      food_object.flouride_per_serving)

        self.servings = grams_eaten / food_object.serving_size_grams

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
        self.flouride = food_object.flouride_per_serving * self.servings

        self.net_carbohydrates = food_object.net_carbohydrates_per_serving * self.servings
        self.calories = food_object.calories_per_serving * self.servings

        self.nutrition_facts = {}
        for key, value in food_object.nutrition_facts_per_serving.items():
            self.nutrition_facts[key.replace('_per_serving', '')] = value * self.servings


class Meal:
    def __init__(self, *args):
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
        self.flouride = 0
        self.net_carbohydrates = 0
        self.calories = 0
        for arg in args:
            self.fat += arg.fat
            self.saturated_fat += arg.saturated_fat
            self.trans_fat += arg.trans_fat
            self.polyunsaturated_fat += arg.polyunsaturated_fat
            self.monounsaturated_fat += arg.monounsaturated_fat
            self.cholesterol += arg.cholesterol
            self.sodium += arg.sodium
            self.carbohydrates += arg.carbohydrates
            self.fiber += arg.fiber
            self.soluble_fiber += arg.soluble_fiber
            self.insoluble_fiber += arg.insoluble_fiber
            self.sugars += arg.sugars
            self.added_sugars += arg.added_sugars
            self.sugar_alcohol += arg.sugar_alcohol
            self.protein += arg.protein
            self.calcium += arg.calcium
            self.iron += arg.iron
            self.potassium += arg.potassium
            self.phosphorous += arg.phosphorous
            self.magnesium += arg.magnesium
            self.flouride += arg.flouride
            self.net_carbohydrates += arg.net_carbohydrates
            self.calories += arg.calories
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
            'flouride': self.flouride,
            'net_carbohydrates': self.net_carbohydrates,
            'calories': self.calories}
