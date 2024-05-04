# print ("gjhjy")
#
# print("sdfh")
#
# class Student:
#     amount_of_students = 1
#
#     def __init__(self, height, name):
#         self.height = height
#         self.name = name
#         Student.amount_of_students += 1

#     def grow(self, value=1):
#         self.height += value
#
#     def __str__(self):
#         return f'I`m a student. My name is {self.name}'
#
#
# john = Student(height = 180, name='john')
# print(f'Johns height {john.height}')
# john.grow(20)
# print(f'Johns height after grow {john.height}')
# print('john')
#
# Hary = Student(height = 150, name='Hary')
# print(f'Harys height {Hary.height}')
# Hary.grow(10)
# print(f'Johns height after grow {Hary.height}')
# print('Hary')
#
#
# Costya = Student(height = 160, name='Costya')
# print(f'Costyas height {Costya.height}')
# Costya.grow(7)
# print(f'Johns height after grow {Costya.height}')
# print('Costya')
#
#
# print(f'We`ve {Student.amount_of_students} students')
# Add comment ctrl + /
#
# import random
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print('Time to study...')
#         self.progress += 0.15
#         self.gladness -= 3
#
#     def to_sleep(self):
#         print('Time to sleep...')
#         self.gladness += 3
#
#     def to_chill(self):
#         print('Rest time...')
#         self.progress -= 0.1
#         self.gladness += 5
#
#     def is_alive(self):
#         if self.gladness <= 0:
#             print('Depression...')
#             self.alive = False
#         elif self.progress < -0.5:
#             print('Failed...')
#             self.alive = False
#         elif self.progress > 5:
#             print('Passed!')
#             self.alive = False
#
#     def end_of_day(self):
#         print(f'Gladness - {self.gladness}')
#         print(f'Progress - {self.progress}')
#
#     def live(self, day):
#         day = f'Day {day} of {self.name} life'
#         print(f'{day:=^50}')
#         cube = random.randint(1, 3)
#         if cube == 1:
#             self.to_study()
#         elif cube == 2:
#             self.to_sleep()
#         elif cube == 3:
#             self.to_chill()
#
#         self.end_of_day()
#         self.is_alive()
#
# deive = Student(name='Deive')
# for day in range(1,365):
#     if not deive.alive:
#         break
#     deive.live(day)
