#!/usr/bin/env python3

import csv
# import hashlib
# import os.path as path
# import random
import sys
# import unittest

# DIR = path.abspath(path.dirname(__file__))
# FILES = {
#     'clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
#     'accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
#     'household_cleaners.csv': ('Kitchen Cleaner', 'Bathroom Cleaner',),
# }


# def write_file(writer, length, categories):
#     writer.writerow(['email_hash', 'category'])
#     for i in range(0, length):
#         writer.writerow([
#             hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
#             random.choice(categories),
#         ])
def validate_input(csv_files):
    column_set = None
    for csv_file in csv_files:
        pathname = 'fixtures/' + csv_file
        try:
            file = open(pathname, 'r')
            file.close()
        except:
            print('Error: One or more files not found in the fixtures folder.')
            exit(3)
        with open(pathname, 'r') as current_file:
            # if i == 0:
            file_reader = csv.reader(current_file)
            # print('before')
            temp = None
            try:
                temp = next(current_file)
            except:
                print('Error: One or more empty files found.')
                exit(4)
            # print(pathname)
            # print(temp)
            column_labels = temp.replace('\"', ' ').replace(',', ' ').split()
            # print(column_labels)
            if column_set == None:
                column_set = column_labels
            else:
                for i in range(len(column_labels)):
                    if column_labels[i] != column_set[i]:
                # for label in column_labels:
                #     if label not in column_set:
                        print('Error: Different column labels found.')
                        exit(5)
            num_rows = 0
            for row in file_reader:
                # print(len(row))
                # print(len(column_set))
                if len(row) == len(column_set):
                    num_rows = num_rows + 1
            if num_rows == 0 or len(column_set) == 0:
                print('Error: Not enough row data in one of the files found.')
                exit(6)
                # header_row = '|  '
                # for label in column_labels:
                #     header_row += label
                #     # if (i != len(fields) - 1):
                #     header_row += '  |  '
                # header_row += 'filename'
                # header_row += '  |'
                # print(header_row)
# class CSV_Combiner:
#     def __init__(self, csv_files):
#         self.csv_files = csv_files
    

def main(csv_files):
    validate_input(csv_files)
    # for fn, categories in FILES.items():
    #     with open(path.join(DIR, 'fixtures', fn), 'w', encoding='utf-8') as fh:
    #         write_file(
    #             csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
    #             random.randint(100, 1000),
    #             categories
    #         )
    # common_labels = []
    # for i in range(len(csv_files)):

    for i in range(len(csv_files)):
        pathname = 'fixtures/' + csv_files[i]
        with open(pathname, 'r') as current_file:
            # print(i)
            file_reader = csv.reader(current_file)
            # if i == 0:
            # print(i)
            column_labels = next(current_file).replace('\"', ' ').replace(',', ' ').split()
            # print(column_labels)
            if i == 0:
                header_row = '|  '
                for label in column_labels:
                    header_row += label
                    # if (i != len(fields) - 1):
                    header_row += '  |  '
                header_row += 'filename'
                header_row += '  |'
                print(header_row)
            # iteration = 0
            for row in file_reader:
                # print(row)
                # print(iteration)
                # print(len(row))
                if len(row) > 0:
                    current_row = '|  '
                    for entry in row:
                        current_row += entry
                        current_row += '  |  '
                    current_row += csv_files[i]
                    current_row += '  |'
                    print(current_row)
                # iteration = iteration + 1
                # disregard empty rows
                # if len(row) > 0:
# class TestCSV_Combiner(unittest.TestCase):
#     def test_valid(self):
#         print('testing...')
#         self.assertEqual(main(['hello']), 1)
        

if __name__ == '__main__':
    # unittest.main()
    argv_len = len(sys.argv)
    if (argv_len < 2):
        print("Please specify the csv file names.")
        exit(1)
    csv_files = []
    for i in range(1, argv_len):
        if '.csv' not in sys.argv[i]:
            print("Invalid csv file(s).")
            exit(2)
        csv_files.append(sys.argv[i])
    # print(csv_files)
    main(csv_files)
