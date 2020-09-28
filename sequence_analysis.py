def open_file(file_name):
    try:
        file  = open(file_name)
        return file
    except FileExistsError:
        return None

def get_sequence(file_names):
    list_of_sequences = []
    for file_name in file_names:
        sequence = []
        file = open_file(file_name)

        if file == None:
            return None
        else:
            for line in file:
                number = line.split('\n')[0]
                # check if only digit
                if number.replace('-', '').isdigit():
                    sequence.append(int(number))
                # check if float
                elif number.replace('-', '').replace('.', '').isdigit():
                    sequence.append(float(number))
        list_of_sequences.append(sequence)
    return list_of_sequences

def sequence_variations(sequence):
    variations = [sequence]
    cum_sum = [sequence[0]]
    sequence_sorted = sorted(sequence)
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


def process_all_files(files_names):
    sequencees = get_sequence(files_names)
    for n, sequence in enumerate(sequencees):
        variations = sequence_variations(sequence)
        print('File {}'.format(files_names[n]))
        print('         Sequence: {}'.format(variations[0]))
        print('         Cumulative sum: '.format(variations[1]))
        print('         Sorted sequence: '.format(variations[2]))
        print('         Medianm: '.format(variations[3]))

# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
