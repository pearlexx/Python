from operator import itemgetter

users = [
    {'fname': 'Cyrus', 'lname': 'Vence'},
    {'fname': 'Jessica', 'lname': 'Parker'},
    {'fname': 'Kate', 'lname': 'Winslet'},
    {'fname': 'Kristina', 'lname': 'Zauber'},
    {'fname': 'Kate', 'lname': 'Cairo'},
    {'fname': 'Paris', 'lname': 'Hilton'},
    {'fname': 'Angelina', 'lname': 'Jolie'},
    {'fname': 'Mila', 'lname': 'Jovovic'},
    {'fname': 'Paris', 'lname': 'Grace'},
    {'fname': 'Angelina', 'lname': 'Sanders'},
    {'fname': 'Mila', 'lname': 'Clinton'},
    {'fname': 'Kate', 'lname': 'Trump'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-------------------------------------------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
