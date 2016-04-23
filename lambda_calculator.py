operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': pow
}

try:    
    first = float(input('First number: '))
    operation = input('Operation: ')
    second = float(input('Second number: '))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result: ', result)
