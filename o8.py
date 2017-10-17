def quadratic(x):
    """The function we wish to find the roots of. This equation is
    just an alternative version of expressing the third root of 7."""
    return x ** 3 - 7

def derivative(x):
    """The derivative of the function we with to find the zeroes of."""
    return 3 * x ** 2

def newtons_method(current=2, digits=3):
    """Run Newtons method with the provided initial guess
    and run enough iterations to get the provided amount
    of significant digits."""

    # We initially set the previous value to a value which
    # is guaranteed to kickstart the while loop.
    previous = False

    while str(previous)[:digits] != str(current)[:digits]:
        previous, current = current, current - quadratic(current) / derivative(current)

    # Return the final value for the root.
    return current

print(newtons_method())

