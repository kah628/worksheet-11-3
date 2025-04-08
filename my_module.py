import matplotlib.pyplot as plt
import random

# Function that generates a plot
def plot(func, x_values):
   y_values = [func(x) for x in x_values]
   plt.plot(x_values, y_values)
   plt.xlabel('X-Values')
   plt.ylabel('Y-Values')
   plt.title('Function of X')
   plt.show()
   return True

# Chooser Class
class Chooser:
    def __init__(self, list = [1, 2, 3, 4, 5, 6]):
        self.list = list
    def get_value(self):
        print(self.list)
    def select(self):
        self.value1 = random.choice(self.list)
        self.value2 = self.value1
        print(self.value2)
        return True

# Solution to a Leetcode Problem (Palindrome Number)
def palindrome_num(num):
    if str(num) == str(num)[::-1]:
        print(True)
    else:
        print(False)
    return True

def fav_nums():
    fav_nums = [0, 5, 7, 10, 25, 45, 345]
    print(fav_nums)
    return True