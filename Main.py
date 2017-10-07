import numpy as np
import Reader as reader
import Reshaper as rs
import Normalizer as normalizer
import Classificator as cls

base1, base2, training_set_ids, training_set, test_set_ids = reader.read()

y = rs.reshape_logistic(training_set, 4)

T1 = rs.reshape_logistic(base2[:, 0], 25)
T2 = rs.reshape_logistic(base2[:, 1], 7)
T3 = rs.reshape_logistic(base2[:, 2], 152)
T4 = rs.reshape_logistic(base2[:, 3], 1394)

base1_normalized = normalizer.normalize(base1)

print(base1_normalized.shape)
print(T1.shape)
print(T2.shape)
print(T3.shape)
print(T4.shape)

features = np.concatenate((base1_normalized, T1, T2, T3, T4), axis=1)

training_features = features[training_set_ids, :]
training_labels = y[training_set_ids, :]

cls.learn(training_features, training_labels)

#train_features = training_features[0:4500, :]
#validation_features = training_features[4500:, :]
#train_labels = training_labels[0:4500, :]
#validation_labels = training_labels[4500:, :]


