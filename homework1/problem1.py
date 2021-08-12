# #!/usr/bin/env python3

# Write a script that will accept a list of items separated by a space from user input.
# Have your script then loop through that list and print each item with
# the phrase "was found at the dog park" appended to it.


user_input = input("List some stuff: ").split()

for x in user_input:
    print(f'{x} was found at the dog park')
