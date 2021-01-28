# Copyright https://www.globaletraining.com/
# Decorators

from functools import wraps


def hello_message_new(func):
    """ This is hello message decorator"""
    @wraps(func)
    def wrapper():
        """This is wrapper inside hello message decorator"""
        return ">>>>> Wrapper: Hello! <<<<<"
    return wrapper


@hello_message_new
def hello_message():
    """ This is hello message function"""
    return 'hello'


print(hello_message())

# message = hello_message_decorator(hello_message())
# print(message())

# print(hello_message_decorator(hello_message)())
