# define functions

def double(x):
    doubled_x = x * 2
    return doubled_x

four_doubled = double(4)
print(four_doubled)

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}.{last}.'

a = initials('Ex Ample')
print(a)
initials('Bob Cat')
initials('Function Nice')

def multiply(a, b):
    return a * b

one = multiply(2, 2)
print(one)

# multiply(9, 2.3)
# print(multiply)
# multiply(29, 'Hey! ')
# print(multiply)

# def func_with_multiple_args(arg_0, arg_1):
#     print('I received the arguments:', arg_0, arg_1)


###############################################################

# (1) Python takes note of this function
def main():
    # (5) At this point greet() is known and we can run it.
    print(greet('Bob'))

# (2) Then this one
def greet(name):
    return f'Hi, {name}!'

# (3) Now this statement is read
if __name__ == '__main__':
    # (4) main is run
    main()

###############################################################
