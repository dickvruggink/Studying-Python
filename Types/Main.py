type(3)
type(3.14)
type('Pi')
type("I am a string.")

some_number = 5
print (type(some_number))
another_number = 9.81
print (type(another_number))
some_string = 'Hello world'
print (type(some_string))

# If you try to assign the following: 'I like ' + 3.14 or 42 + ' is the answer'
# TypeError: can only concatenate str (not "float") to str

#  What you can do is "cast" the value to another type
# for example: print ('I like ' + str(3.14))

# Using backslash to Suppressing Special Character Meaning
print('I\'m a\nstring.')
print("I'm a string")
print('He said: "I\'m a string"')

print('foo\\bar')

print('I like ' + str(3.14))