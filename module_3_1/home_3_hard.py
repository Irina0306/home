def calculate_structure_sum(data_structure):
    calculator = 0
    for i in data_structure:

        if isinstance(i, str):
            for j in i:
                if isinstance(j,str):
                    calculator += len(j)
                elif isinstance(j,int):
                    calculator += j
                elif isinstance(j, dict):
                    for k in j.keys():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                    for k in j.values():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                elif isinstance(j,tuple):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k
                elif isinstance(j, set):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)

                        elif isinstance(k, int):
                            calculator += k
                if isinstance(j, list):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k
        elif isinstance(i, tuple):
            for j in i:
                if isinstance(j,str):
                    calculator += len(j)
                elif isinstance(j, int):
                    calculator += j
                elif isinstance(j,list):
                    for k in j:
                        if isinstance(k,str):
                            calculator += len(k)
                        elif isinstance(k,int):
                            calculator += k
                elif isinstance(j, dict):
                    for k in j.keys():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                    for k in j.values():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                elif isinstance(j, set):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)

                        elif isinstance(k, int):
                            calculator += k
        elif isinstance(i, set):
            for j in i:
                if isinstance(j, str):
                    calculator += len(j)

                elif isinstance(j, int):
                    calculator += j
                elif isinstance(j, dict):
                    for k in j.keys():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                    for k in j.values():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                elif isinstance(j,tuple):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k
                        elif isinstance(j, dict):
                            for k in j.keys():
                                if isinstance(k, int):
                                    calculator += k
                                elif isinstance(k, str):
                                    calculator += len(k)
                            for k in j.values():
                                if isinstance(k, int):
                                    calculator += k
                                elif isinstance(k, str):
                                    calculator += len(k)
                elif isinstance(j,tuple):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k
                if isinstance(j, list):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k
        if isinstance(i, list):
            for j in i:
                if isinstance(j,str):
                    calculator+= len(i)
                elif isinstance(j,int):
                    calculator += j

                elif isinstance(j, dict):
                    for k in j.keys():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                    for k in j.values():
                        if isinstance(k, int):
                            calculator += k
                        elif isinstance(k, str):
                            calculator += len(k)
                elif isinstance(j,tuple):
                    for k in j:
                        if isinstance(k, str):
                            calculator += len(k)
                        elif isinstance(k, int):
                            calculator += k

        elif isinstance(i, dict):
            for j in i.keys():
                if isinstance(j, int):
                    calculator += j
                elif isinstance(j, str):
                    calculator += len(j)
            for j in i.values():
                if isinstance(j, int):
                    calculator += j
                elif isinstance(j, str):
                    calculator += len(j)

        if isinstance(i, int):
            calculator += i


    #return calculate_structure_sum()
    return calculator
data_structure=[
    [1, 2, 3], {'a': 4,'b':5}, (6, {'cube': 7,'drum': 8}),
    'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)