import time
from random import randint


def function(one, two, three):
    if one == 1:
        counter = 0
        while counter < 10:
            random_integer = randint(0, 10)
            if random_integer < 5:
                output = f"The random integer is {random_integer} and it is below 5"
            else:
                output = f"The random integer is {random_integer} and it is above 5"
            print(output)
            counter +=1
        return True
    return 'This function did not return True'

if __name__ == '__main__':
    function(1, 0, 0)
