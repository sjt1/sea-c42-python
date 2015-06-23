def fibonacci(n):
    '''Determine the nth value of the Fibonnachi Sequence.'''
    if (n == 0):
        return(0)

    elif (n == 1):
        return(1)

    elif (n > 1):
        return(fibonacci(n - 1) + fibonacci(n - 2))


print(fibonacci())

def lucas(n):
    '''Determine the nth value of the Lucas Numbers sequence.'''
    if (n == 0):
        return(2)

    elif (n == 1):
        return(1)

    elif (n > 1):
        return(lucas(n - 1) + lucas(n - 2))

print(lucas())
    '''Determine the nth value of Fibonnachi Sequence if a value is
passed in for only the required parameter.  Determine the nth value of
the Lucas Number Sequence a value is passed in for the required parameter
x is passed in as 2 and y is passed in as 1.'''

def sum_series(n, x=0, y=1):
    if (x == 0 and y == 1):
        return(fibonacci(n))
    if (x == 2 and y == 1):
        return(lucas(n))

print(sum_series(3, x=2, y=1))
print(sum_series(3))
