#
# 5. Write a Python program to count the number of strings where the string
#    length is 3 or more and the first and second last character are same
#    from a given list of strings.
#
#        Sample List : ['abc', 'xyz', 'baba', '21221']
#        Expected Result : 2
#

def count(strings):
    c = 0
    for string in strings:
        if len(string) >= 3:
            first_ch = string[0]
            if string[-2] == first_ch:
                c += 1
    return c

def main():
    list5 = [ 'retro', 'robot', 'pypy', 'cc' ]
    print(" List :", list5)
    print("Count :", count(list5))

if __name__ == '__main__':
    main()
