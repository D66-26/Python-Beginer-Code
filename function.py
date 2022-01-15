def function1(a, b):
    sum1 = a + b
    print(sum1)


def function2(a, b):
    """THis function is used to find average"""  # This is docstring
    average = (a + b) / 2
    print(average)
    return average


function1(5, 2)
function2(5, 5)
print("this is used to print function1", function1(5,2))
print('this is used to print function2', function2(5,5))
print("docstring of function2 is", function2.__doc__)
