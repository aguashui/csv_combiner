import csv
import sys

def validate_input(csv_files):
    column_set = None
    for csv_file in csv_files:
        pathname = 'fixtures/' + csv_file
        try:
            file = open(pathname, 'r')
            file.close()
        except:
            print('Error: \"' + pathname + '\" was not found.')
            exit(3)
        with open(pathname, 'r') as current_file:
            file_reader = csv.reader(current_file)
            temp = None
            try:
                temp = next(current_file)
            except:
                print('Error: \"' + csv_file +'\" is empty.')
                exit(4)
            column_labels = temp.replace('\"', ' ').replace(',', ' ').split()
            if column_set == None:
                column_set = column_labels
            else:
                for i in range(len(column_labels)):
                    if column_labels[i] != column_set[i]:
                        print('Error: Column labels differ between files.')
                        exit(5)
            num_rows = 0
            for row in file_reader:
                if len(row) == len(column_set):
                    num_rows = num_rows + 1
            if num_rows == 0 or len(column_set) == 0:
                print('Error: Not enough row data in file \"' + csv_file + '\"')
                exit(6)

def main(csv_files):
    validate_input(csv_files)
    for i in range(len(csv_files)):
        pathname = 'fixtures/' + csv_files[i]
        with open(pathname, 'r') as current_file:
            file_reader = csv.reader(current_file)
            column_labels = next(current_file).replace('\"', ' ').replace(',', ' ').split()
            if i == 0:
                header_row = '|  '
                for label in column_labels:
                    header_row += label
                    header_row += '  |  '
                header_row += 'filename'
                header_row += '  |'
                print(header_row)
            for row in file_reader:
                if len(row) > 0:
                    current_row = '|  '
                    for entry in row:
                        current_row += entry
                        current_row += '  |  '
                    current_row += csv_files[i]
                    current_row += '  |'
                    print(current_row)

if __name__ == '__main__':
    argv_len = len(sys.argv)
    if (argv_len < 2):
        print("Please specify the csv file names.")
        exit(1)
    csv_files = []
    for i in range(1, argv_len):
        if '.csv' not in sys.argv[i]:
            print('File \"' + sys.argv[i] + '\" is an invalid csv file name.')
            exit(2)
        csv_files.append(sys.argv[i])
    main(csv_files)