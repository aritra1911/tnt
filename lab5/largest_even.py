
# 3. Write a Python program to get the largest even number from a list.

def largest_even(nums):
    max_num = 0
    for num in nums:
        if not num & 1:
            if num > max_num:
                max_num = num
    return max_num

def main():
    list1 = [ 78, 23, 96, 128, 64, 39, 729 ];
    print("   List :", list1);
    print("Largest :", largest_even(list1));

if __name__ == '__main__':
    main()

