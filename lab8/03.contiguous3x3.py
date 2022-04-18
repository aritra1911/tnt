import numpy as np;

def main():
    mat = np.random.randint(0, 10, (10, 10))
    print('matrix :')
    print(mat)
    print()
    print(np.lib.stride_tricks.as_strided(
        mat,
        shape=(8, 8, 3, 3),
        strides=2*mat.strides
    ))

if __name__ == '__main__':
    main()
