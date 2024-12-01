"""
you can create class in multiple ways in python.

1. __init__
2. __call__
3. __new__ & __init__
4. metaclass
5. Metaclass with __new__ & __init__
6. metclass with __init__
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
        print("allocating memory for Mthree")
        return super(Mthree, cls).__new__(cls, *args, **kwargs)

    # creating instance
    def __init__(self, *args, **kwargs):
        print("creating instance for Mthree")
        return super(Mthree, self).__init__(*args, **kwargs)


obj3: Mthree = Mthree()
print("i am obj3 at {l}".format(l=obj3))

# method4

"""Everything in python is an object i.e means everything is derived from class 'type'."""
print(type(int))  # o/p  :<class 'type'>


class Method(type):
    def __call__(cls, *args, **kwargs):
        print("allocating memory")
        return super(Method, cls).__call__(*args, **kwargs)

    def __init__(self, name, base, attr):
        print("creating instance")
        return super(Method, self).__init__(name, base, attr)


class MethodFour(metaclass=Method):
    pass


obj4: MethodFour = MethodFour()
print(f"i am obj4 at {obj4}")


# method5


class Meta(type):
    """
    metaclass
    """

    def __call__(cls, *args, **kwargs):
        print("inside __call__")
        return super(Meta, cls).__call__(*args, **kwargs)

    def __init__(self, name, base, attr):
        print("inside __init__")
        super(Meta, self).__init__(name, base, attr)


class MethodFive(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("assigning memory into heap")
        return super(MethodFive, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("creating instance")
        super(MethodFive, self).__init__(*args, **kwargs)


obj5: MethodFive = MethodFive()
print("i am obj5 at {}".format(obj5))


# method 6


class NewMethod(type):
    def __new__(cls, *args, **kwargs):
        return super(NewMethod, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        return super(NewMethod, self).__init__(*args, **kwargs)


class MethodSix(metaclass=NewMethod):
    def __init__(self):
        pass


obj6: MethodSix = MethodSix()
print("i am obj6 at {}".format(obj6))
