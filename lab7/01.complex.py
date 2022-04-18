class Complex:
    def __repr__(self):
        imag = self.imag
        sign = '+'

        if self.imag < 0:
            imag = -self.imag
            sign = '-'

        return f"{self.real} {sign} {imag}j"

    def __init__(self, real=None, imag=None):
        self.real = 0 if real == None else real;
        self.imag = 0 if imag == None else imag;

    def __add__(self, z):
        return Complex(self.real + z.real, self.imag + z.imag)

def main():
    z1 = Complex(96, 30);
    z2 = Complex(6, -42);

    print('     z1 =', z1);
    print('     z2 =', z2);

    z_sum = z1 + z2;

    print('z1 + z2 =', z_sum);

if __name__ == '__main__':
    main()
