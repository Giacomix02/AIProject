import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def RegressioneLineareTrain():
    df = pd.read_csv('Dataset/archive/train.csv', skipinitialspace=True, usecols=['topic'])
    numberOfEntriesPerTopic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in df.values:
        numberOfEntriesPerTopic[int(i[0])] = numberOfEntriesPerTopic[int(i[0])] + 1
    return numberOfEntriesPerTopic

def RegressioneLineareTest():
    df1 = pd.read_csv('Dataset/archive/test.csv', skipinitialspace=True, usecols=['topic'])
    numberOfEntriesPerTopic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in df1.values:
        numberOfEntriesPerTopic[int(i[0])] = numberOfEntriesPerTopic[int(i[0])] + 1
    return numberOfEntriesPerTopic



# # Assuming 'topic' is the column you are interested in
# df = pd.read_csv('Dataset/archive/train.csv', skipinitialspace=True, usecols=['topic'])
# df1 = pd.read_csv('Dataset/archive/test.csv', skipinitialspace=True, usecols=['topic'])
#
# X_test = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshape to 2D array
# X_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshape to 2D array
#
# numberOfEntriesPerTopic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in df.values:
#     numberOfEntriesPerTopic[int(i[0])] = numberOfEntriesPerTopic[int(i[0])] + 1
#
# numberOfEntriesPerTopic1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in df1.values:
#     numberOfEntriesPerTopic1[int(i[0])] = numberOfEntriesPerTopic1[int(i[0])] + 1
#
# y_train = np.array(numberOfEntriesPerTopic)
# y_test = np.array(numberOfEntriesPerTopic1)
#
# linear_model = LinearRegression()
# linear_model.fit(X_train, y_train)
#
# y_pred_linear = linear_model.predict(X_test)
#
# # Visualizzazione della regressione lineare
# plt.scatter(X_train, y_train, color='blue', label='Actual')
# plt.plot(X_test, y_pred_linear, color='red', linewidth=3, label='Linear Regression')
# plt.title('Regressione Lineare')
# plt.xlabel('Topics')
# plt.ylabel('Number of Entries per Topic')
# plt.legend()
# plt.show()