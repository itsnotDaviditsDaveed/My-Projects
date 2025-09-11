import matplotlib.pyplot as plt
import numpy as np


# I will be creating a program where i will have users
#input their age, height, and weight.
def find_average():
    user_One_average = (user_One.first_testscore + user_One.sec_testscore +
                        user_One.third_testscore) / 3
    user_Two_average = (user_Two.first_testscore + user_Two.sec_testscore +
                        user_Two.third_testscore) / 3
    user_one_average_integer = int(user_One_average)
    user_two_average_integer = int(user_Two_average)
    if user_one_average_integer > user_two_average_integer:
        print(f"{user_One.name} has a higher score than {user_Two.name}")
    elif user_one_average_integer < user_two_average_integer:
        print(f"{user_Two.name} has a higher average than {user_One.name}")


#first let's make the user-class object first.
class User:

    def __init__(self, name):
        self.name = name

    def ask(self):
        self.first_testscore = int(
            input(
                f'Hello {self.name}, please enter a recent test you score you liked. '
            ))
        self.sec_testscore = int(
            input(
                'Great! Now enter a recent test you score you did not like. '))
        self.third_testscore = int(
            input(
                'Last, enter a recent test you score you did not care about. ')
        )
        self.total_testscores = [
            self.first_testscore, self.sec_testscore, self.third_testscore
        ]
        return f"Okay {self.name}, your data is {self.total_testscores}"


first = str(input('User-One, enter your name:  '))
second = str(input('User-Two, enter your name: '))

user_One = User(first.capitalize())
user_Two = User(second.capitalize())

user_One_data = user_One.ask()
print(user_One_data)

user_Two_data = user_Two.ask()
print(user_Two_data)

find_average()

user_One_dataList = user_One.total_testscores
user_Two_dataList = user_Two.total_testscores

x1points = np.array([50, 90, 100])
user_One_plotPoints = np.array(user_One_dataList)
x2poinnts = np.array([50, 90, 100])
user_Two_plotPoints = np.array(user_Two_dataList)

plt.plot(x1points[:3], user_One_plotPoints, x2poinnts[:3], user_Two_plotPoints)
plt.show()


#so this is something different.
