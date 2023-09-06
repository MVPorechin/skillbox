n, m = list(map(int, input().split()))
nominal_value = list(map(int, input().split()))
sum_nominals = dict()

while len(sum_nominals.keys()) < 6:
    for nominal_val in nominal_value:
        for s in list(sum_nominals.keys()):
            if (s + nominal_val) not in sum_nominals:
                sum_nominals[s + nominal_val] = [nominal_val] + sum_nominals[s]
        if nominal_val not in sum_nominals:
            sum_nominals[nominal_val] = [nominal_val]

if n in sum_nominals:
    print(len(sum_nominals[n]))
    print(*sum_nominals[n])
else:
    print('-1')




