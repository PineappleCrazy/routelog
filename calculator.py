import clr
import os

dll_path = os.path.join(os.path.dirname(__file__), 'MathLibProject.dll')
clr.AddReference(dll_path)

from MathLib import Calculator

num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))

result = Calculator.Add(num1, num2)
print(result)