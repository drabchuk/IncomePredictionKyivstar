import numpy as np
import csv

TRAINING_SET_LENGTH = 6229
TEST_SET_LENGTH = 3038
ALL_USERS_NUMBER = TRAINING_SET_LENGTH + TEST_SET_LENGTH


def read_base1():
    base1 = np.zeros((ALL_USERS_NUMBER, 6, 42))

    with open('data/Base1.txt', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = file.readline()
        for row in reader:
            id = int(row[0])
            month = int(row[1])
            for i in range(42):
                num_str = row[i + 2]
                if num_str == '':
                    num_str = '0'
                val = float(num_str)
                base1[id - 1, month - 1, i] = val
    return base1


def read_base2():
    base2 = np.zeros((ALL_USERS_NUMBER, 4), dtype=int)

    factors1 = set()
    factors2 = set()
    factors3 = set()
    factors4 = set()

    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    dict1_counter = 0
    dict2_counter = 0
    dict3_counter = 0
    dict4_counter = 0

    with open('data/Base2.txt', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = file.readline()
        for row in reader:
            id = int(row[0])
            factor1 = row[1]
            val = 0
            if factor1 in dict1:
                val = dict1.get(factor1)
            else:
                val = dict1_counter
                dict1[factor1] = val
                dict1_counter += 1

            base2[id - 1, 0] = val

            factor2 = row[2]

            if factor2 in dict2:
                val = dict2.get(factor2)
            else:
                val = dict2_counter
                dict2[factor2] = val
                dict2_counter += 1

            base2[id - 1, 1] = val

            factor3 = row[3]

            if factor3 in dict3:
                val = dict3.get(factor3)
            else:
                val = dict3_counter
                dict3[factor3] = val
                dict3_counter += 1

            base2[id - 1, 2] = val

            factor4 = row[4]

            if factor4 in dict4:
                val = dict4.get(factor4)
            else:
                val = dict4_counter
                dict4[factor4] = val
                dict4_counter += 1
            base2[id - 1, 3] = val
    return base2


def read_training_set():
    training_set = np.zeros((ALL_USERS_NUMBER, 1), dtype=int)
    training_set_ids = set()
    with open('data/train.txt', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = file.readline()
        for row in reader:
            id = int(row[0])
            training_set_ids.add(id - 1)
            target = int(row[1])
            training_set[id - 1, 0] = target
    training_set_ids_list = list(training_set_ids)
    return training_set_ids_list, training_set


def read_test_set():
    test_set_ids = set()
    with open('data/test.txt', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = file.readline()
        for row in reader:
            id = int(row[0])
            test_set_ids.add(id - 1)
    test_set_ids_list = list(test_set_ids)
    return test_set_ids_list


def read():
    base1 = read_base1()
    base2 = read_base2()
    training_set_ids, training_set = read_training_set()
    test_set_ids = read_test_set()
    return base1, base2, training_set_ids, training_set, test_set_ids
