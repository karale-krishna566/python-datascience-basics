import numpy as np

# --- Part 1: Performance, Basics, and Array Creation ---

b = np.array(range(20000000))
print("Benchmarking array squaring operation:")
%timeit b**2

a = list(range(20))
print(type(a))

b = np.array(range(20000000))
print(type(b))
print(b.ndim)
print(len(b))
print(b.shape)

a_list = [1, 3, "Sandip"]
print(type(a_list))

b_arr = np.array(a_list)
print(type(b_arr))
print(b_arr)

c1 = np.arange(1, 10)
print(c1)

c3 = np.arange(1, 10, 0.5)
print(c3)

numpy_array = np.arange(1, 10)
b1 = numpy_array.astype('float')
print(b1)


# --- Part 2: 1D Indexing, Slicing, and Boolean Filtering ---

a_1d = np.arange(1, 10)
print(a_1d)
print(a_1d[-2])
print(a_1d[2:5])
print(a_1d[3:])

print(a_1d[[2, 5, 7]])

a_filter = np.array([6, 9, -3, 0, 5, 7, -2, 8, 1])
print(a_filter < 6)
print(a_filter[a_filter % 2 == 0])
print(a_filter[a_filter > 0])


# --- Part 3: Array Reshaping ---

a_reshape = np.array(range(16))
print(a_reshape.shape)
print(a_reshape.ndim)

b_manual = a_reshape.reshape(8, 2)
print(b_manual)

b_auto = a_reshape.reshape(4, -1)
print(b_auto)


# --- Part 4: 2D Array Indexing & Slicing ---

a_2d = np.arange(1, 10).reshape(3, 3)
print(a_2d)
print(a_2d[1][2])

print(a_2d[:2])
print(a_2d[:, :2])
print(a_2d[:, 1:3])
