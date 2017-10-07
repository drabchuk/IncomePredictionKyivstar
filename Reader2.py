import numpy as np
import csv

TRAINING_SET_LENGTH = 6229
TEST_SET_LENGTH = 3038
ALL_USERS_NUMBER = TRAINING_SET_LENGTH + TEST_SET_LENGTH

base2 = np.zeros((ALL_USERS_NUMBER, 4), dtype=int)
# factors =

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

print('f1', len(factors1))
print(factors1)

print(len(factors2))
print(factors2)

print(len(factors3))
print(factors3)

print(len(factors4))
print(factors4)

print(base2[0:50, 0])
print(base2[0:50, 1])
print(base2[0:50, 2])
print(base2[0:50, 3])
