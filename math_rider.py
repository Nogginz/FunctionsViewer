import math
class MathRider(object):
    def __init__(self, str):
        self.OPERATORS = {'+': (1, lambda x, y: x + y),
                    '-': (1, lambda x, y: x - y),
                    '*': (2, lambda x, y: x * y),
                    '/': (2, lambda x, y: x / y),
                    '^': (3, lambda x, y: x ** y),
                    'c': (4, lambda x: math.cos(x)),
                    's': (4, lambda x: math.sin(x)),
                    't': (4, lambda x: math.tan(x)),
                    'g': (4, lambda x: math.cos(x)/math.sin(x)),
                    'e': (4, lambda x: math.exp(x)),
                    'l': (5, lambda x, y: math.log(y, x)),
                    'n': (4, lambda x: math.log(x)),
                    'm': (6, lambda x: -x),
                    '$': (4, lambda x: x**0.5)}

        str = str.replace(' ', '')
        str = str.replace('cos', 'c')
        str = str.replace('sin', 's')
        str = str.replace('tan', 't')
        str = str.replace('cot', 'g')
        str = str.replace('exp', 'e')
        str = str.replace('log', 'l')
        str = str.replace('ln', 'n')
        str = str.replace('(-', '(m')
        str = str.replace('sqrt', '$')
        if str[0] == '-':
            str = 'm' + str[1:]

        self.str = str

    def parse(self, line):
        num = ''
        for i in line:
            if i in '1234567890.':
                num += i
            elif num:

                yield float(num)
                num = ''
            if i in self.OPERATORS or i in '()':

                yield i
        if num:

            yield float(num)

    def sort(self, parsed):
        tmp = []
        for i in parsed:
            if i in self.OPERATORS:
                while tmp and tmp[-1] != '(' and self.OPERATORS[i][0] <= self.OPERATORS[tmp[-1]][0]:

                    yield tmp.pop()
                tmp.append(i)
            elif i == ')':
                while tmp:
                    x = tmp.pop()
                    if x == '(':
                        break

                    yield x
            elif i == '(':
                tmp.append(i)
            else:

                yield i
        while tmp:

            yield tmp.pop()


    def calc(self, sort):
        tmp = []
        j=0
        for i in sort:
            if i in self.OPERATORS:
                if self.OPERATORS[i][0] == 4 or self.OPERATORS[i][0] == 6:
                    x = tmp.pop()
                    tmp.append(self.OPERATORS[i][1](x))
                    j+=1

                else:
                    y = tmp.pop()
                    x = tmp.pop()
                    tmp.append(self.OPERATORS[i][1](x, y))
                    j+=1

            else:
                tmp.append(i)
        return tmp[0]

    def interpretotor(self, x = 'None'):

        str2 = self.str.replace('x', str(x))
        str3 =''
        while str2!=str3:
            str3 = str2
            str2 = str2.replace('m-','')
            str2 = str2.replace('(-', '(m')
            str2 = str2.replace('--', '-m')
            str2 = str2.replace('mm', '')

            if str2[0] == '-':
                str2 = 'm' + str2[1:]
            str2 = str2.replace('+-', '+m')
            str2 = str2.replace('*-', '*m')
            str2 = str2.replace('/-', '/m')
            str2 = str2.replace('^-','^m')
            str2 = str2.replace('$-', '$m')
        return complex(self.calc(self.sort(self.parse(str2))))


if __name__ == '__main__':
    import numpy as np
    inp = ''
    while inp.upper() !='STOP':
        inp = input('EBASH: ')
        func = MathRider(inp)
        os_x = np.linspace(-5, 5, 10)
        vfunc = np.vectorize(func.interpretotor)
        print(vfunc(os_x))
        print(type(os_x[0]))