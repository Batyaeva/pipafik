# try:
#     print('start code')
#     print(10 / 0)
#     print(name)
# except NameError:
#        print('We have an error')
#
# except ZeroDivisionError:
#        print('You can`t divide by 0')
#
# print('Code after try-except')



# try:
#     print('start code')
#     print(10 / 0)
#     print(name)
# except (NameError,ZeroDivisionError):
#        print('We have an error')
#
# except ZeroDivisionError:
#        print('You can`t divide by 0')
# else:
#     print('All is ok!')
# finally:
#     print('I work if we have error or not')
#
# print('Code after try-except')


# def checker(value):
#     if type(value) != str:# != --- ne dorivniue
#         raise TypeError(f'Sorry, we can`t work with this type - {type(value)}.'
#                         f'We need STR')
#     else:
#         return value
# try:
#     checker(10)
# except TypeError as error:
#     print(error)
#     print('Try again!')
#
#
# class BuildingError(Exception):
#     def __str__(self):
#         return 'With this materials we can`t build the house'
#
# def check_material(amount, limit):
#     if amount >= limit:
#         return "Enough materials"
#     else:
#         raise BuildingError()
#
# limit = 100
# print(
#     check_material(80,limit)
# )

import warnings

warnings.simplefilter('always', SyntaxWarning)
warnings.simplefilter('error', ImportWarning)

warnings.warn('Warnind, no code where', SyntaxWarning)
warnings.warn('Warnind, wrong module', ImportWarning)

print(1000)