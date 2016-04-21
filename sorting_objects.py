# sorting custom objects

from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)


users = [
    User('Cyrus', 43),
    User('Kate', 5),
    User('Jess', 61),
    User('Sarah', 2),
    User('Tina', 77),
    User('Mila', 9)
]

for user in users:
    print(user)

print('-----------------')

for user in sorted(users, key=attrgetter('name')):
    print(user)

print('-----------------')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)
