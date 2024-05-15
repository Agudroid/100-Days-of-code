#
# # Something that might cause an exception
# try:
#     # File Not Found
#     file = open('data.txt', mode='r')
#     a_dictionary = {}
#     print(a_dictionary['non_existent_key'])
#
# # Do this if there was an exception
# except FileNotFoundError:
#     file = open('data.txt', mode='w')
#     file.write('hi!!')
# except KeyError as error_message:
#     print(f'The key: {error_message} does not exists')
# # Do this if there were no exception
# else:
#     content = file.read()
#     print(content)
# # Do this no matter what happens
# finally:
#     file.close()
#     raise KeyError('Key not found')

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")


bmi = weight / height ** 2
print(bmi)
