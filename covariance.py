import numpy as np

X = np.array([2, 4, 6, 8, 10])
Y = np.array([45, 50, 65, 80, 90])

cov_matrix = np.cov(X, Y)

print("Covariance Matrix:")
print(cov_matrix)
print("\nSample Covariance:", cov_matrix[0, 1])
