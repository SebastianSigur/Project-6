def open_file(file_name):
    try:
        file  = open(file_name)
        return file
    except FileExistsError:
        return None

def process_all_files(files_names):
    list_of_sequences = []
    for file_name in files_names:
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


# Main program starts here
#filename_list = input("Enter filenames: ").split()
process_all_files(['data1.txt', 'data2.txt'])
