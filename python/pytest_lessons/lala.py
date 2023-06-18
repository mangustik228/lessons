

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'name is {self.name}'


a = User('hello world')

print(f'{a = }')
