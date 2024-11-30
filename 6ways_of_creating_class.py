"""
you can create class in multiple ways in python.

1. __init__
2. __call__
3. __new__ & __init__
"""


# method 1


class Mone:
    def __init__(self):
        pass


obj1: Mone = Mone()
print(f"i am obj1 at {obj1}")

# method 2


class Mtwo(object):

    # behind the scene invoke dunder method '__new__' and '__init__'
    def __call__(cls, *args, **kwargs):
        return super(Mtwo, cls).__call__(cls, *args, **kwargs)


obj2: Mtwo = Mtwo()
print("i am obj2 at {}".format(obj2))

# method3


class Mthree(object):

    # allocating memory
    def __new__(cls, *args, **kwargs):
        return super(Mthree, cls).__new__(cls, *args, **kwargs)

    # creating instance
    def __init__(self, *args, **kwargs):
        return super(Mthree, self).__init__(*args, **kwargs)


obj3: Mthree = Mthree()
print("i am obj3 at {l}".format(l=obj3))
