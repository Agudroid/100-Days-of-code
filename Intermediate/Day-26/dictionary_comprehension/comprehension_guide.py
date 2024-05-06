import random

student_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Generate random scores for each student

# Little formula: dict_name = new_key: new_value for item in item_list if condition
student_scores = {item: random.randint(0, 100) for item in student_names}

print(student_scores)

# Create a dictionary with the pass students

# Little formula: dict_name = new_key:new_value for (key, value) in dict.items() if condition
pass_students = {student: grade for (student, grade) in student_scores.items() if grade >= 50}

print(pass_students)
