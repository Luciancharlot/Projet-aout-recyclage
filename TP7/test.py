from main import *

"""
f1 = Fraction(22, 2)
f2 = Fraction(9, 10)
#print(f1.as_mixed_number())
#f1.__add__(f2)
print(f1)
print(f1.as_mixed_number())
print(f2)
print(f2.as_mixed_number())
print(f1.__add__(f2))
#print(f1.__eq__(f2))



#print(f1)"""

if __name__ == '__main__':
    print("----------- \n\n")
    fraction1 = Fraction(2, 4)
    fraction2 = Fraction(1, -4)
    fraction3 = Fraction(0, 3)
    print(fraction2)
    print("----------- \n\n")
    print("-----(==)------")
    print(fraction1 == fraction2)
    print("----------- \n\n")
    
    print(fraction1)
    print(fraction2)
    print("----------- \n\n")
    print("as mixed number")
    print((fraction1 + fraction2).as_mixed_number())
    print("-----(+)------")
    print(fraction1 + fraction2)
    print("----------- \n\n")

    print(fraction1)
    print(fraction2)
    print("----------- \n\n")
    print("-----(-)------")
    print(fraction1 - fraction2)
    print("----------- \n\n")

    print(fraction1)
    print(fraction2)
    print("----------- \n\n")
    print("-----(*)------")
    f3 = fraction1 * fraction2
    print(f3)
    print("----------- \n\n")

    print(fraction1)
    print(fraction2)
    print("----------- \n\n")
    print("-----(/)------")
    print(fraction1 / fraction2)
    print("----------- \n\n")
    print("-----(==)------")
    print(fraction1 == fraction2)
    print("----------- \n\n")
    print("-----(float)------")
    print(fraction1.__float__())
    #print(fraction1 + "test")
    #print(fraction1 / fraction3)

