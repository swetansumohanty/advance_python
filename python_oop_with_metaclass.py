"""
what is metalcass ?
==================

- metaclass is a class whose instance are classes, like an ordinary class defines the behavior of the instances of the class same way 
  metaclass defines behavior of the class and their instances.

- via metaprogramming we can impose custom rules while creating classes with metaclass.

"""

try:
    import os
    import sys
    import datetime
    import logging
except Exception as e:
    print("something went wrong while importing modules {}".format(e))


class Metaclass(type):

    """Meta class"""

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """Implement Singleton Design Pattern"""

        name = kwargs.get("name")
        if not name.__str__:
            raise TypeError("name must be string")

        if cls not in cls._instance:
            cls._instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs)

            return cls._instance[cls]

    def __init__(cls, name, base, attr):

        """Define your own rules"""

        if not cls.__name__[0].isupper():
            raise ValueError(
                "class {} first character should be uppercase".format(cls.__name__)
            )

        for k, v in attr.items():

            # check the value is callable
            if hasattr(v, "__call__"):

                if not (v.__name__[0].islower() or v.__name__[0] == "_"):
                    raise ValueError(
                        "method first character can be `_` or `lowercase` {} ".format(
                            v.__name__
                        )
                    )

                if not v.__doc__:
                    raise ValueError(
                        "Require documentation string {}".format(v.__name__)
                    )


class Log(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        """wrapper function"""
        start = datetime.datetime.now()
        res = self.func(self, *args, **kwargs)
        end = datetime.datetime.now()

        message = """
            Function: {}
            Execution-time: {}
            Address: {}
            Memory: {}
            Date: {}""".format(
            self.func.__name__,
            end - start,
            "--",
            sys.getsizeof(self.func),
            datetime.datetime.now(),
        )

        # sepcify dir for looging
        cwd = os.getcwd()
        folder = "Log"
        new_path = os.path.join(cwd, folder)

        try:
            os.mkdir(new_path)
        except Exception as e:
            print("dir already exist {}".format(e))

        logging.basicConfig(
            filename="{}/meta_test.log".format(new_path),
            encoding="utf-8",
            level=logging.DEBUG,
        )

        logging.debug(message)

        return res


class Test(metaclass=Metaclass):

    __slots__ = ["name"]  # restricts new attributes to be added during runtime.

    def __init__(self, name):
        """constructor"""

        self.name = name
        super(Test, self).__init__()

    def test_method(self):
        """test method"""

        print("Welcome {} :)".format(self.name))


if __name__ == "__main__":
    test_obj: Test = Test(name="swetansu")
    test_obj.test_method()
