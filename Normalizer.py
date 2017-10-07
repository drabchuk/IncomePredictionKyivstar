import numpy as np



def normalize(base1):
    #base1_reduced = np.sum(base1, axis=1)
    base1_reduced = np.zeros((base1.shape[0], base1.shape[2]))
    for i in range(base1.shape[0]):
        for j in range(base1.shape[2]):
            count = 0
            sum = 0
            for k in range(6):
                if base1[i][k][j] != 0:
                    count += 1
                    sum += base1[i][k][j]
            if count != 0:
                base1_reduced[i][j] = sum / count
                    
    print('base reduced')
    print('base red shape', base1_reduced.shape)
    
    base1_avg = np.average(base1_reduced, axis=0)
    base1_avg = base1_avg.reshape((1, base1_avg.shape[0]))

    base1_centered = base1_reduced - base1_avg

    base1_max = base1_centered.max(axis=0)
    for i in range(len(base1_max)):
        print(base1_max[i])
        if base1_max[i] == 0:
            print('change')
            base1_max[i] = 1
    base1_max = base1_max.reshape((1, base1_max.shape[0]))
    
    base1_normalized = base1_centered / base1_max

    return base1_normalized