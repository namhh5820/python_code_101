#python3
#When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop.

while True:
    print('Who are you?')
    name = input()
    if name != 'namhh':
        continue
    print('Hello, Namhh. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
