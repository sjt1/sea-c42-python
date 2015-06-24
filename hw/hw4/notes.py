x = 0

def runneth_over():
    global x
    x = x + 1
    print(x)
    runneth_over()  # Recursive function.  Calls itself.
    # Things that happen within the statement will only exist in the
    # statement untill called upon

runneth_over()