"""
solid is a abbreviation stands for five design principles.
- single responsibility
- open-closed principle
- liskov substitute
- interface seggregation
- dependency inversion
"""


#  single responsibility
"""A class or a method should have only one job or one reason to change,
 this means that a class/function should have only one responsibility"""


# before single responsibility
class UserManager:
    def authenticate_user(self, username, password):
        pass

    def update_user_profile(self, user_id, update_profile_data):
        pass

    def email_notification(self, email, message):
        pass


# after applying single responsiblity
class UserAuthenticator:
    def authenticate_user(self, username, password):
        pass


class UserProfileManager:
    def update_user_profile(self, user_id, update_profile_data):
        pass


class EmailNotifier:
    def email_notification(self, email, message):
        pass


# open-closed principle

"""
software entities (class, functions & module) open for extension, but closed for modification.
"""

# before open-closed principle
class Shape:
    def __init__(self, width, height, type):
        self.width = width
        self.height = height
        self.type = type


class ShapeCalculator:
    def calculate_area(self, shape):
        if shape == "rectangle":
            return shape.width * shape.height
        elif shape == "circle":
            pass

    def calculate_perimeter(self, shape):

        if shape == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape == "circle":
            pass


# after applying open-closed principle

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):

    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.PI * (self.radius**2)

    def calculate_perimeter(self):
        return 2 * self.PI * self.radius


#  Liskov-substitution
"""
object of superclass should be replaceable for the object of its child class without affecting the correctness of the programm.
"""

#  before applying the liskov-substitution principle

class Vehicle:
    def start_engine(self):
        print("starting vehicle engine")


class Car(Vehicle):
    def start_engine(self):
        print("starting car engine")


class Bycycle(Vehicle):
    def start_engine(self):
        print("starting Bycycle engine")


#  after applying liskov substitution principle

class Vehicle:
    def start(self):
        print("starting vehicle engine")


class Car(Vehicle):
    def start(self):
        print("starting car engine")


class Bycycle(Vehicle):
    def start(self):
        print("pedaling Bycycle")


#  Interface-segregation
"""
client should not forced to use the method they don't use.
or 
we should segregate interfaces into smaller or more specific ones , 
clients only depend on the method they actually need.
"""

#  before interface segregation

class MultimediaPlayer:

    def start_audio(self, file):
        pass

    def start_video(self, file):
        pass

    def adjust_audio_volume(self, file):
        pass

    def stop_audio(self, file):
        pass

    def stop_video(self, file):
        pass

#  after segregating interface
class AudioPlayer:
    def start_audio(self, file):
        pass

    def start_video(self, file):
        pass

    def adjust_audio_volume(self, file):
        pass


class VideoPlayer:
    def stop_audio(self, file):
        pass

    def stop_video(self, file):
        pass


# Dependency Inversion

"""
High-level-module should not depend upon low-level-module both should depend on abstractions.
"""

#  before dependency inversion

class GmailClient:
    def send_mail(self, receipent, subject, body):
        pass


class EmailService:
    def __init__(self)
        self.gmail_client = GmailClient()

    def send_mail(self, receipent, subject, body):
        self.gmail_client.send_mail(receipent=receipent, subject=subject, body=body)


#  after dependency inversion

class EmailClient:
    def send_mail(self, receipent, subject, body):
        pass


class GmailClient(EmailClient):
    def send_mail(self, receipent, subject, body):
        pass


class OutlooklClient(EmailClient):
    def send_mail(self, receipent, subject, body):
        pass


class EmailService:

    def __init__(self, email_client):
        self.email_client = email_client()

    def send_mail(self, receipent, subject, body):
        self.email_client.send_mail(receipent=receipent, subject=subject, body=body)
