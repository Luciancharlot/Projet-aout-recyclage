class Fraction:
    """Class representing a fraction and operations on it

    Author :L. Charlot
    Date : 11 August 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : -
        POST : Return a new Fraction object with numerator and denominator as specified in the parameters
        EXCEPT : ZeroDivisionError if den is zero.
                 ValueError if num/den isn't int.
        """
        if den == 0:
            raise ZeroDivisionError("Denominator can't be Zero ! ")

        elif type(num) != int or type(den) != int:
            raise ValueError("Num or Den must be integer !")

        else:
            self.__num = num
            self.__den = den

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    @staticmethod
    def pgcd(num, den):
        while den != 0:
            num, den = den, num % den
        return num

    @staticmethod
    def check_other(other):
        return isinstance(other, Fraction)

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        POST : Return textual representation of the reduced form of the fraction

        """
        return f"The fraction is {self.__num // self.pgcd(self.__den, self.__num)}/" \
               f"{self.__den // self.pgcd(self.__den, self.__num)}"

    def as_mixed_number(self):

        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        POST : return the reduced form of a fraction as a mixed number

        """

        a = self.__num // self.__den
        b = self.__num % self.__den

        if self.__den == 1 or self.__den == -1:
            return f"Mixed number : {a}"

        else:
            return f"Mixed number : {a} and {b}/{self.__den}"

        # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """
        Overloading of the + operator for fractions

         PRE  : /
         POST : return a new Fraction which is the addition of self and other
         Except : TypeError if Other isn't Fraction Object
         """
        if self.check_other(other):
            num = (self.__num * other.denominator) + (other.numerator * self.__den)
            den = self.__den * other.denominator
            pg = self.pgcd(num, den)
            return Fraction(int(num/pg), int(den/pg))
        else:
            raise TypeError("Other isn't a Fraction object")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : /
        POST : return a new Fraction which is the subtraction of self and other
        Except : TypeError if Other isn't Fraction Object
        """
        if self.check_other(other):
            num = (self.__num * other.denominator) - (other.numerator * self.__den)
            den = self.__den * other.denominator
            pg = self.pgcd(num, den)
            return Fraction(int(num/pg), int(den/pg))
        else:
            raise TypeError("Other isn't a Fraction object")

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : 0ther is an object created with the class Fraction
        POST : return a new Fraction which is the result of multiplying self and other
        Except : TypeError if Other isn't Fraction Object
        """
        if self.check_other(other):
            num = self.__num * other.numerator
            den = self.__den * other.denominator
            pg = self.pgcd(num, den)
            return Fraction(int(num/pg), int(den/pg))
        else:
            raise TypeError("Other isn't a Fraction object")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : 0ther is an object created with the class Fraction
        POST : return a new Fraction which is the result of dividing self and other
        Except : TypeError if Other isn't Fraction Object
                 ZeroDivisionError if den is zero.
        """

        if self.check_other(other):
            if self.denominator != 0 and other.denominator != 0:
                num = self.__num * other.denominator
                den = self.__den * other.numerator
                pg = self.pgcd(num, den)
                return Fraction(int(num/pg), int(den/pg))
            else:
                raise ZeroDivisionError("Denominator can't be Zero ! ")
        else:
            raise TypeError("Other isn't a Fraction object")

    def __pow__(self, other):
        """ Overloading of the ** operator for fractions

        PRE : 0ther is an object created with the class Fraction
        POST : return a new Fraction which is the result of power other and self
        Except : TypeError if Other isn't Fraction Object
        """
        if self.check_other(other):
            list_num = pow(self.__num, other.numerator / other.denominator).as_integer_ratio()
            list_den = pow(self.__den, other.numerator / other.denominator).as_integer_ratio()
            num = list_num[0] * list_num[1]
            den = list_den[0] * list_num[1]
            pg = self.pgcd(num, den)
            return Fraction(int(num/pg), int(den/pg))

        else:
            raise TypeError("Other isn't a Fraction object")

    def __eq__(self, other):
        """Overloading of the == operator for fractions
        PRE : 0ther is an object created with the class Fraction
        POST : return a boolean if self and other are equal or not
        Except : TypeError if Other isn't Fraction Object

        """
        if self.check_other(other):
            return self.__num == other.numerator and self.__den == other.denominator
        else:
            raise TypeError("Other isn't a Fraction object")

    def __float__(self):
        """Returns the decimal value of the fraction

        POST : return the decimal value of the fraction
        """
        return self.__num / self.__den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : return a boolean of the fraction's value == 0
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : return a boolean of fraction == int
        """
        if self.__num % self.__den == 0:
            return True
        else:
            return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : return a boolean of self.__num / self.__den < 1
        """
        return self.__num / self.__den < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : return a boolean of self.num == 1
        """
        pg = self.pgcd(self.__num, self.__den)
        return self.__num/pg == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        PRE : other has to be an object created with the class Fraction
        POST : return True if they are adjacent, False if not
        """
        divisor = self.pgcd(other.numerator * self.__den, self.__num * other.denominator)
        o_n = (other.numerator * self.__den) // divisor
        s_n = (self.__num * other.denominator) // divisor
        if abs(o_n - s_n) == 1:
            return True
        return False
