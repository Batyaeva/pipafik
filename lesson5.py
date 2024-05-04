import requests

def test_funk():
    pass

print(requests.__name__)
print(requests.__cake__)
print(__name__)
x = 10
print(type(x))
print(type(requests))

for m in dir():
    print(m)

print(callable(x))
print(callable(test_funk))

class A:
    pass

class B(A):
    pass

print(issubclass(A,B))
print(issubclass(B,A))


namber = 100
text = 'asd'
print(isinstance(namber,int))
print(isinstance(namber,str))
print(isinstance(text,str))
print(isinstance(text,float))
print(isinstance(text,B))

import inspect

print(inspect.ismodule(requests))
print(inspect.isclass(A))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))


import  sys

print(sys.version)
print(sys.executable)

import colorama

from colorama import just_fix_windows_console
just_fix_windows_console() # Ця строка коду змушує екранування ANSI працювати в Windows.

from colorama import init
init() # Це робить те саме, що й just_fix_windows_console, за винятком таких відмінностей: Небезпечно дзвонити initкілька разів; ви можете отримати кілька шарів обгортки та непрацюючу підтримку ANSI.
# Colorama застосує евристику, щоб здогадатися, чи підтримують stdout/stderr ANSI, і якщо він вважає, що вони не підтримують, тоді він загорнеться sys.stdoutв sys.stderrчарівний файловий об’єкт, який видаляє escape-послідовності ANSI перед їх друкуванням. Це відбувається на всіх платформах і може бути зручним, якщо ви хочете написати свій код, щоб безумовно видавати escape-послідовності ANSI, а Colorama вирішувати, чи потрібно їх виводити. Але зауважте, що евристика Colorama не дуже розумна.
# initтакож приймає явні аргументи ключових слів, щоб увімкнути/вимкнути різні функції

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now') #Дозволяє  виконати міжплатформний друк кольорового тексту за допомогою постійного скорочення Colorama для керуючих послідовностей ANSI.