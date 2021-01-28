# Copyright 2020 https://www.globaletraining.com/
# Nested Functions


def hello_message_decorator(func):
    """ This is hello message decorator"""
    def wrapper():
        """This is wrapper inside hello message decorator"""
        msg = func()
        print("Called from another function:", msg)
        return ">>>>> Wrapper: Hello! <<<<<"
    return wrapper


def hello_message():
    """ This is hello message function"""
    return 'hello'


message = hello_message_decorator(hello_message)
print(message())

# print(hello_message_decorator(hello_message)())
