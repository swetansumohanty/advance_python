"""let see how we can impose logging with metaclass"""

import os
import sys
import datetime
import logging


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
            filename="{}/test.log".format(new_path),
            encoding="utf-8",
            level=logging.DEBUG,
        )

        logging.debug(message)

        return res


class Test(object):
    def __init__(self):
        pass

    @Log
    def test(self):
        return "this is test function"

    @Log
    def test2(self):
        return "this is test2 function"


if __name__ == "__main__":
    test_obj = Test()

    test_obj.test()
    test_obj.test2()
