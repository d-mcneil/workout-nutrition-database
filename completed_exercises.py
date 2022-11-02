import exercise_classes

db_decline_bench_press = exercise_classes.BenchPress('dumbbell', incline_or_decline='decline')
# exercise_classes.test(db_decline_bench_press)

class ExerciseSet:
    def __init__(self, repetitions, weight_amount, weight_unit='pounds'):
        self.repetitions = repetitions
        self.weight_amount = weight_amount
        self.weight_unit = weight_unit

class CompletedExercise:
    def __init__(self, exercise, sets=1):
        self.exercise = exercise
        self.sets = sets
        exercise_data = {}
        print(exercise.exercise_label)
        for series in range(1, self.sets + 1):
            repetitions = int(input(f'Enter repetitions in set {series}: '))
            weight_amount = int(input(f'Enter weight at which set {series} was performed: '))
            weight_type = input('Enter unit of measurement of weight: ')
            exercise_data[{series}] = [repetitions, weight_amount, weight_type]
        self.exercise_data = exercise_data


exercise1 = CompletedExercise(db_decline_bench_press, 3)
print(exercise1.exercise_data)


    # setf'{set}'.repetitions =
    # set{set}.weight =

