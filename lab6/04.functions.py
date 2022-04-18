def my_max(tup):
    max_so_far = 0;
    for item in tup:
        if item > max_so_far:
            max_so_far = item
    return max_so_far

def my_index(tup, target):
    for i in range(my_len(tup)):
        if tup[i] == target:
            return i
    raise ValueError

def my_reverse(tup):
    tmp_list = list();
    for i in range(my_len(tup)):
        tmp_list.append(tup[my_len(tup) - i - 1]);
    return tuple(tmp_list)

def my_count(tup, item):
    count = 0
    for i in tup:
        if i == item:
            count += 1
    return count

def my_len(tup):
    count = 0
    for _ in tup:
        count += 1
    return count

def main():
    my_tuple = (4, 4, 3, 2, 5, 7, 8, 8, 8, 7)
    print("my_len(my_tuple) :", my_len(my_tuple))
    print("my_count(my_tuple, 8) :", my_count(my_tuple, 8))
    print("my_reverse(my_tuple) :", my_reverse(my_tuple))
    print("my_index(my_tuple, 7) :", my_index(my_tuple, 7))
    print("my_max(my_tuple) :", my_max(my_tuple))

if __name__ == '__main__':
    main()
