import fractions
class Rational(object):    
    """represents rational numbers.
        attributes: x, y"""

    def __init__(self,n,d=1):
        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        g = fractions.gcd(n,d)
        self.numer = n/g
        self.denom = d/g
    
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        return self.__str__()

    def __add__(self,other):        
        if isinstance(other,int):
            return Rational(self.numer + other * self.denom, self.denom)
        elif isinstance(other,Rational):
            return Rational(self.numer * other.denom + other.numer * self.denom,
                        self.denom * other.denom)
        else:
            raise TypeError("Can't add Time and " + other.__class__.__name__)
        
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        return Rational(self.numer * other.denom - other.numer * self.denom,
                        self.denom * other.denom)
    
    def __mul__(self,other):
        return Rational(self.numer * other.numer,self.denom * other.denom)

    def __div__(self,other):
        return Rational(self.numer * other.denom,self.denom * other.numer)

    def __lt__(self,other):
        return self.numer * other.denom < self.denom * other.numer
    
    def __le__(self,other):
        return self.numer * other.denom <= self.denom * other.numer

    def __gt__(self,other):
        return self.numer * other.denom > self.denom * other.numer
    
    def __ge__(self,other):
        return self.numer * other.denom >= self.denom * other.numer
    
    
