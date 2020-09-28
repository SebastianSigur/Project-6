def sequence_variations(sequence):
    variations = [sequence]
    cum_sum = [sequence[0]]
    sequence_sorted = sorted(sequence)
    median = 0

    print(sequence)
    print (sequence_sorted)

    next_num = sequence[0]

    for num in range(1, len(sequence)):
        next_num += sequence[num]
        cum_sum.append(next_num)
    
    if len(sequence) % 2 == 0:
        first_middle = sequence_sorted[(len(sequence_sorted) // 2) - 1]
        second_middle = sequence_sorted[(len(sequence_sorted) // 2)]

        median = (first_middle + second_middle) / 2
    
    else:
        median = sequence_sorted[(len(sequence_sorted) // 2)]

    variations.append(cum_sum)
    variations.append(sequence_sorted)
    variations.append(median)

    return variations
x = [1,-2,6,4]

print(sequence_variations(x))