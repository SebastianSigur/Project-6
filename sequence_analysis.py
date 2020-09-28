def open_file(file_name):
    try:
        file = open(file_name)
        return file
    except FileNotFoundError:
        return None


def get_sequence(file_names):
    list_of_sequences = []
    for file_name in file_names:
        sequence = []
        file = open_file(file_name)

        if file == None:
            list_of_sequences.append(None)
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


def change_float_list(int_list):
    float_list = []
    for n in int_list:
        float_list.append(round(float(n), ndigits=4))
    return float_list


def sequence_variations(sequence):
    variations = [change_float_list(sequence)]
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

    variations.append(change_float_list(cum_sum))
    variations.append(change_float_list(sequence_sorted))
    variations.append(round(float(median), ndigits=4))

    return variations


def process_all_files(files_names):

    print()
    sequences = get_sequence(files_names)
    for n, sequence in enumerate(sequences):
        if sequence == None:
            print('File {} not found'.format(files_names[n]))
            break
        if len(sequence) == 0:
            print('File {}'.format(files_names[n]))
            print('\tSequence:\n\t\t')
            print('\tCumulative sum:\n\t\t')
            print('\tSorted sequence:\n\t\t')
            print('\tMedian:\n\t\t')
            print()
            continue
        variations = sequence_variations(sequence)
        print('File {}'.format(files_names[n]))
        print('\tSequence:\n\t\t' + str(variations[0])[1:-1].replace(',', '') + ' ')
        print('\tCumulative sum:\n\t\t' + str(variations[1])[1:-1].replace(',', '') + ' ')
        print('\tSorted sequence:\n\t\t' + str(variations[2])[1:-1].replace(',', '') + ' ')
        print('\tMedian:\n\t\t' + str(variations[3]))
        print()

# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)
