def sum_for_in(args, sum = 0):
    for i in args:
        sum += i
    return sum

def sum_recursion(args):
    if len(args) == 1:
        return args[0]
    return args[0] + sum_recursion(args[1:])

sum_lambda = lambda x: x[0] + sum_lambda(x[1:]) if x!=[] else 0


args = [23, 451, 78, 13, 896, 102, 2, 741, 236, 562, 85, 4, 96]
print('args >>', args)
print('4 options for summing:')
print('built-in function sum() >>', sum(args))
print('using for..in >>',sum_for_in(args))
print('recursion >>', sum_recursion(args))
print('lambda >>', sum_lambda(args))
