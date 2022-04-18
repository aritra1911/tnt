import numpy as np;

def main():
    mat = np.ones((7, 7));
    mat[1:-1, 1:-1] = 0;
    print(mat)

if __name__ == '__main__':
    main()
