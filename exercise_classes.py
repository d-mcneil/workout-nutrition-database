def capitalize_decorator(fn):
    def wrapper(*args, **kwargs):
        capitalized_list_of_words = []
        for word in fn(*args, **kwargs).split():
            capitalized_list_of_words.append(word.capitalize())
        return ' '.join(capitalized_list_of_words)
    return wrapper


class Exercise:
    def __init__(self, exercise_name, weight_type='Body-Weight',
                 primary_muscle_group='Full-Body', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        self.exercise_name = exercise_name.lower()
        self.weight_type = weight_type.lower()
        self.primary_muscle_group = primary_muscle_group.lower()
        self.secondary_muscle_groups = secondary_muscle_groups.lower()
        self.grip_width = grip_width.lower()
        self.incline_or_decline = incline_or_decline.lower()
        self.grip_type = grip_type.lower()
        self.exercise_label = self.completely_label_exercise()

    @capitalize_decorator
    def completely_label_exercise(self):
        label = f'{self.weight_type} '
        if self.grip_type:
            label = label + f'{self.grip_type} '
        if self.grip_width:
            label = label + f'{self.grip_width} '
        if self.incline_or_decline:
            label = label + f'{self.incline_or_decline} '
        label = label + f'{self.exercise_name}'
        return label


class ChestExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'chest'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class TricepExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'triceps'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class ShoulderExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'shoulders'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class BicepExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'biceps'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class BackExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'back'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class LegExercise(Exercise):
    def __init__(self, exercise_name, weight_type='body-weight', secondary_muscle_groups='',
                 grip_width='', incline_or_decline='', grip_type=''):
        primary_muscle_group = 'legs'
        Exercise.__init__(self, exercise_name, weight_type,
                          primary_muscle_group, secondary_muscle_groups,
                          grip_width, incline_or_decline, grip_type)


class BenchPress(ChestExercise):
    def __init__(self, weight_type,
                 grip_width='', incline_or_decline='', grip_type=''):
        exercise_name = 'bench press'
        secondary_muscle_groups = 'triceps'
        ChestExercise.__init__(self, exercise_name, weight_type,
                               secondary_muscle_groups, grip_width, incline_or_decline, grip_type)


def test(x):
    print('exercise name input: ' + x.exercise_name)
    print('exercise label: ' + x.exercise_label)
    print('primary muscle group: ' + x.primary_muscle_group)
    print('secondary muscle groups: ' + x.secondary_muscle_groups)
    print('weight type: ' + x.weight_type)
    print('grip width: ' + x.grip_width)
    print('grip type: ' + x.grip_type)
    print('incline or decline: ' + x.incline_or_decline)


# bb_narrow_grip_incline_bench_press = BenchPress('barbell', 'narrow grip', incline_or_decline='incline')
# db_reverse_fly = BackExercise('reverse fly', 'dumbbell')
# print('\n')
# test(bb_narrow_grip_incline_bench_press)
# print('\n')
# test(db_reverse_fly)

# primary muscle groups
#     back
#     chest
#     shoulders
#     legs
#     triceps
#     biceps
#     cardio

# weight types
#     barbell
#     EZ bar
#     dumbbell
#     kettle bell
#     body-weight
#     machine
#     cable
#     assisted
#

# grip types
#     rope
#
#
#
#
#
#

# grip widths
#     narrow
#     wide
#
#
#
#
