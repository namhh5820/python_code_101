#This allows to specify a statement to execute in case of the full loop has been executed. Only useful when a break condition can occur in the loop:

for i in [1, 2, 6, 4, 5]:
    if i == 3:
        break
else:
    print("only executed when no item of the list is equal to 3")