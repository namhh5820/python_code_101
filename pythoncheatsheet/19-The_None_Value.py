#python3
#Note: never compare to None with the == operator. Always use is.
spam = print('Hello!')

if spam is None:
    print('True')
else:
    print('False')