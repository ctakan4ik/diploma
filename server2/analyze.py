def analyze(cases):
    plus = 0
    minus = 0
    for i in range(1,len(cases)-1):
        if cases[i] > cases[i+1]:
            minus += 1
        elif cases[i] < cases[i+1]:
            plus += 1
        else:
            continue
    if plus > minus:
        return 1
    elif plus < minus:
        return 0
    else:
        return 2