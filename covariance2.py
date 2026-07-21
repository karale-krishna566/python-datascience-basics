import numpy as np

X = np.array([10, 15, 20, 25, 30])
Y = np.array([120, 150, 180, 210, 240])

cov_matrix = np.cov(X, Y)

print("Covariance Matrix:")
print(cov_matrix)
print("\nSample Covariance:", cov_matrix[0, 1])
