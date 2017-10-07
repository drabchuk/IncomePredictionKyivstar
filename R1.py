import numpy as np
import csv

TRAINING_SET_LENGTH = 6229
TEST_SET_LENGTH = 3038
ALL_USERS_NUMBER = TRAINING_SET_LENGTH + TEST_SET_LENGTH

base1 = np.zeros((ALL_USERS_NUMBER, 6, 42))
print(base1.shape)


with open('data/Base1.txt', 'r') as csvfile:
     reader = csv.reader(csvfile, delimiter='\t')
     i = 1
     for row in reader:
         l = len(row)
         i += 1
         if(l != 44):
             print(i)
             print(l)