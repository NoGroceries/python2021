#  A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
# The module's name (as a strng) is available as the value of the global variable __name__
# The __init__.py files are required to make Python treat directories containing the file as packages.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    fib(10)
