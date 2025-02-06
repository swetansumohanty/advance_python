"""
:partial:
=========
- partial is a function from functools module.
- with partial you can create partial functions.
- partial fuction takes callable (another function) and fixed arguments of that callable.
- parital() : it allows to self document exactly what's going on.
- partial keep all the type hints and original function.
- partial can be really helpfull when you don't want to send tons/multiple params (same repeating arguments) when calling a function.
"""

from functools import partial

# Example 1


def send_email(to, subject, body, priority, retry):
    """sending email"""
    return "email send to {}".format(to)


def send_email_urgent(to, subject, body):
    """sending email urgent"""
    return send_email(to, subject, body, priority="high", retry=True)


def send_email_markeging(to, subject, body):
    """sending email marketing"""
    return send_email(to, subject, body, priority="medium", retry=False)


#  after applying partial to the above example

send_email_urgent = partial(send_email, priority="high", retry=True)
send_email_markeging = partial(send_email, priority="medium", retry=True)

print(send_email_urgent("hello@gmail.com", "system alert", "testing partial"))
