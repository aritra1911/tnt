import numpy as np;

def is_magic_square(mat):
    col_sums = list(map(sum, mat.transpose()))
    max_col_sum = max(col_sums)
    min_col_sum = min(col_sums)

    print("       col_sums :", col_sums)
    print("    max_col_sum :", max_col_sum)
    print("    min_col_sum :", min_col_sum)
    print()

    row_sums = list(map(sum, mat))
    max_row_sum = max(row_sums)
    min_row_sum = min(row_sums)

    print("       row_sums :", row_sums)
    print("    max_row_sum :", max_row_sum)
    print("    min_row_sum :", min_row_sum)
    print()

    sum_diag1 = sum(np.diag(mat))
    sum_diag2 = sum(np.diag(np.fliplr(mat)))

    print("      sum_diag1 :", sum_diag1)
    print("      sum_diag2 :", sum_diag2)
    print()

    return max_col_sum == min_col_sum == \
           max_row_sum == min_row_sum == \
           sum_diag1 == sum_diag2

def main():
    A = np.array([[17, 24,  1,  8, 15],
                  [23,  5,  7, 14, 16],
                  [ 4,  6, 13, 20, 22],
                  [10, 12, 19, 21,  3],
                  [11, 18, 25,  2,  9]])

    print()

    if is_magic_square(A):
        print("A is a magic square")
    else:
        print("A is NOT a magic square")

    print()

if __name__ == '__main__':
    main()
