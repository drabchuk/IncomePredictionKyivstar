import numpy as np


def reshape_logistic(types_values, types_count):
    types_values = types_values.reshape((types_values.shape[0], 1))
    y = np.zeros((types_values.shape[0], types_count))
    for i in range(types_values.shape[0]):
        y[i, types_values[i, 0]] = 1
    return y
