def length(s):
    s = s.lower()
    prev = None
    ret = 0
    for i in s:
        if i not in 'aeiou' and prev is not None and prev in 'aeiou':
            pass
        else:
            ret += 1
        prev = i
    return ret

def main():
    inp = input('Enter your string ')
    words = inp.split(' ')
    s = sum(list(map(lambda x: length(x), words)))
    while (s > 9):
        su = 0
        while (s > 0):
            su += s % 10
            s //= 10
        s = su
    print(s)

if __name__ == '__main__':
    main()
