class Distance:
    def __repr__(self):
        return f"{self.km} km {self.m} m"

    def __init__(self, km=None, m=None):
        self.km = 0 if km == None else km;
        self.m = 0 if m == None else m;

    def __add__(self, d):
        km = self.km + d.km
        m = self.m + d.m
        km += m // 1000
        m %= 1000
        return Distance(km, m)

def main():
    d1 = Distance(0, 96);
    d2 = Distance(1, 0);

    print('     d1 =', d1);
    print('     d2 =', d2);

    total_distance = d1 + d2;

    print('Total Distance =', total_distance);

if __name__ == '__main__':
    main()
