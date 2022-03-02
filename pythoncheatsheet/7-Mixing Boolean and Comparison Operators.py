>>> (4 < 5) and (5 < 6)
True

>>> (4 < 5) and (9 < 6)
False

>>> (1 == 2) or (2 == 2)
True

You can also use multiple Boolean operators in an expression, along with the comparison operators:

>>> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
True