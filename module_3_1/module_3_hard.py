

def calculate_nested_sum(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            total_sum += calculate_nested_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_nested_sum(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif arg is None:
            pass
    return total_sum
#print(calculate_nested_sum(nested_sum())
def calculate_structure_sum(data_structure):
    calculator = 0
    for i in data_structure:

        calculator+= calculate_nested_sum(i)
    #return calculate_structure_sum()
    #return calculator
data_structure=[
    [1, 2, 3], {'a': 4,'b':5}, (6, {'cube': 7,'drum': 8}),
    'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_nested_sum(data_structure)
print(result)