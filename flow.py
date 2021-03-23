import numpy as np

new_img = np.array([[1,0,0,1,1],[1,1,0,0,0],[1,1,1,0,0],[1,1,1,1,0],[1,0,0,0,0]])
cluster = np.ones_like(new_img)

# Recursive function that finds potentially percolating clusters
# Join into clusters when open sites are adjacent to each other
# Diagonal open sites do not count

def flow(i, j):
    if new_img[i][j] == 0 and cluster[i][j] == 1:  # preventing counting open spots multiple times
        if all([i - 1 >= 0, j >= 0, i - 1 <= np.shape(new_img)[0] - 1, j <= np.shape(new_img)[0] - 1,
                i - 1 <= np.shape(new_img)[1] - 1,
                j <= np.shape(new_img)[1] - 1]):  # check if index exceeds the size of array
            if new_img[i - 1][j] == 0:
                flow(i - 1, j)
        if all([i + 1 >= 0, j >= 0, i + 1 <= np.shape(new_img)[0] - 1, j <= np.shape(new_img)[0] - 1,
                i + 1 <= np.shape(new_img)[1] - 1,
                j <= np.shape(new_img)[1] - 1]):  # check if index exceeds the size of array
            if new_img[i + 1][j] == 0:
                flow(i + 1, j)
        if all([i >= 0, j - 1 >= 0, i + 1 <= np.shape(new_img)[0] - 1, j - 1 <= np.shape(new_img)[0] - 1,
                i <= np.shape(new_img)[1] - 1,
                j - 1 <= np.shape(new_img)[1] - 1]):  # check if index exceeds the size of array
            if new_img[i][j - 1] == 0:
                flow(i, j - 1)
        if all([i >= 0, j + 1 >= 0, i <= np.shape(new_img)[0] - 1, j + 1 <= np.shape(new_img)[0] - 1,
                i <= np.shape(new_img)[1] - 1,
                j + 1 <= np.shape(new_img)[1] - 1]):  # check if index exceeds the size of array
            if new_img[i][j + 1] == 0:
                flow(i, j + 1)

flow(0,2)
print(new_img)
print(cluster)