def fibonacci_function(to_step):
    f1 = f2 = 1
    count = 2
    while count < to_step:
        f2 = f1 + f2
        f1 = f2 -f1
        count += 1
    return f2


def fibonacci_sequence(to_step):
    sequence = [1, 1]
    if to_step == 1:
        return 1
    else:
        for i in range(to_step - 2):
            sequence.append(sequence[i] + sequence[i + 1])
    return sequence

