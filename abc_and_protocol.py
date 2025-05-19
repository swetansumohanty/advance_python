"""
protocols: 
- protocols don't enforce method implementation at runtime
- protocols are primarily used for static type checking
"""


from typing import Protocol


class Writable(Protocol):
    def write(self, data: dict) -> None:
        """this method write dictionary data"""


class Readable(Protocol):
    def read(self) -> dict:
        """method return a dictionary"""


def do_write(writer: Writable, data: dict) -> None:
    writer.write(data)


def do_read(reader: Readable) -> dict:
    return reader.read()


class Author:
    def __init__(self, name):
        self.name = name

    def write(self, data: dict) -> None:
        print(f"{self.name} is writing data : {data}")


def main():
    data = {"name": "john doe", "age": 54}
    author1: Author = Author("test")
    do_write(author1, data)


main()
