
# 3. Write a Python program to get the smallest odd number from a list.

def smallest_odd(nums):
    min_num = 9999
    for num in nums:
        if num & 1:
            if num < min_num:
                min_num = num
    return min_num

def main():
    list4 = [ 78, 24, 96, 128, 43, 39, 8 ];
    print("    List :", list4);
    print("Smallest :", smallest_odd(list4));

if __name__ == '__main__':
    main()

