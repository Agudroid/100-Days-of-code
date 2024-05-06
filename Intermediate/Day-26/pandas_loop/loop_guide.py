import pandas as pd
import random

student_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = [random.randint(0, 100) for item in student_names]
student_dict = {
    'student': student_names,
    'scores': student_scores
}
print(student_dict)

student_data = pd.DataFrame(student_dict)
print(student_data)

# Loop through rows of a dataframe
for (index, row) in student_data.iterrows():
    print(f'Number: {index}')
    print(f'Data: \n{row}')
    print(f'Student: {row.student}')
    print(f'Score: {row.scores}')
    print('\n')
