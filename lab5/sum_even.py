
# 1. Write a Python program to sum all the even numbers in a list

def sum_even(nums):
    sum = 0
    for num in nums:
        if not num & 1:
            sum += num
    return sum

def main():
    list1 = [2, 8, 7, 2, 69, 42, 65]
    print("        List :", list1)
    print("Sum of items :", sum_even(list1))

if __name__ == '__main__':
    main()
