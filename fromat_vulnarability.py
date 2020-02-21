SECRET = 'это - секрет'
class Error:
    def __init__(self):
        pass

err = Error()

user_input = '{error.__init__.__globals__[SECRET]}'

print(user_input.format(error=err))