# Copyright https://www.globaletraining.com/
# Decorators


def hello_message_new(func):
    """ This is hello message decorator"""
    def wrapper():
        """This is wrapper inside hello message decorator"""
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
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
