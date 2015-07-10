class Fracrrion:
    a=0
    b=0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __init__(other, a, b):
        other.a = a
        other.b = b
    def __add__(self, other):
        if self.a == other.a:
            if self.b+other.b>self.a:
                n1 = self.b+other.b
                n2 = self.a
            else :
                n1 = self.a
                n2 = self.b+other.b
            while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
            print self.b, '/', self.a, '+', other.b, '/', other.a, '=', (self.b+other.b)/n3, '/', self.a/n3
        else:
            if self.b*other.a+self.a*other.b>self.a*other.a:
                n1 = self.b*other.a+self.a*other.b
                n2 = self.a*other.a
            else :
                n1 = self.a*other.a
                n2 = self.b*other.a+self.a*other.b
            while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
            print self.b, '/', self.a, '+', other.b, '/', other.a, '=', (self.b*other.a+self.a*other.b)/n3, '/', (self.a*other.a)/n3
    def __sub__(self, other):
        if self.a == other.a:
            if self.b-other.b>self.a:
                n1 = self.b-other.b
                n2 = self.a
            else :
                n1 = self.a
                n2 = self.b-other.b
            while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
            print self.b, '/', self.a, '-', other.b, '/', other.a, '=', (self.b-other.b)/n3, '/', self.a/n3
        else:
            if self.b*other.a-self.a*other.b>self.a*other.a:
                n1 = self.b*other.a-self.a*other.b
                n2 = self.a*other.a
            else :
                n1 = self.a*other.a
                n2 = self.b*other.a-self.a*other.b
            while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
            print self.b, '/', self.a, '-', other.b, '/', other.a, '=', (self.b*other.a-self.a*other.b)/n3, '/', (self.a*other.a)/n3
    def __mul__(self, other):
        if self.a>other.b:
            n1=self.a
            n2=other.b
        else:
            n1=other.b
            n2=self.a
        while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
        if self.a>other.b:
            n1=self.b
            n2=other.a
        else:
            n1=other.a
            n2=self.b
        while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n4 = n2
                    else:
                        n4 = n1
                    break
        print self.b, '/', self.a, '*', other.b, '/', other.a, '=', (self.b/n4)*(other.b/n3), '/', (self.a/n3)*(other.a/n4)
    def __div__(self, other):
        if self.a>other.a:
            n1=self.a
            n2=other.a
        else:
            n1=other.a
            n2=self.a
        while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n3 = n2
                    else:
                        n3 = n1
                    break
        if self.b>other.b:
            n1=self.b
            n2=other.b
        else:
            n1=other.b
            n2=self.b
        while True:
                if n1%n2!=0:
                    temp = n1%n2
                    n1 = n2
                    n2 = temp
                else:
                    if n2<n1:
                        n4 = n2
                    else:
                        n4 = n1
                    break
        print self.b, '/', self.a, '/', other.b, '/', other.a, '=', (self.b/n4)*(other.a/n3), '/', (self.a/n3)*(other.b/n4)

frac = Fracrrion(2,3)
frac2 = Fracrrion(6,5)
frac + frac2
frac - frac2
frac * frac2
frac / frac2