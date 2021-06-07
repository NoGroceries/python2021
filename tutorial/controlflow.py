def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


print(fib(10))  # In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called None

# keyword argument
# position argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=1000, action='V0000M')
# parrot(action='V0000M', voltage=10000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')