import numpy as np;

# 0 2 0 1
# 2 0 3 0
# 0 3 0 4
# 1 0 4 0

def main():
    mat = np.zeros((4, 4))
    mat[0, 3] = mat[3, 0] = 1
    mat[0, 1] = mat[1, 0] = 2
    mat[2, 1] = mat[1, 2] = 3
    mat[3, 2] = mat[2, 3] = 4
    print(mat)

if __name__ == '__main__':
    main()
