#If you need to modify a global variable from within a function, use the global statement:

def spam():
     global eggs
     eggs = 'spam'

eggs = 'global'
spam()
print(eggs)