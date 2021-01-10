import math
import re

def is_multiple_of_9(n):
    """Return True if n is a multiple of 9; False otherwise."""
    return n % 9 == 0


def next_prime(m):
    """Return the first prime number p that is greater than m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    if m <= 1:
        return 2

    prime = m + 1
    while not is_prime(prime):
        prime = prime + 1

    return prime


def is_prime(m):
    """Returns True if m is prime."""
    if m <= 1:
        return False
    if m <= 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False

    for n in range (5, int(math.sqrt(m) + 1), 6):
        if m % n == 0 or m % (n + 2) == 0:
            return False

    return True

def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    m = b ** 2 - 4 * a * c
    if m < 0:
        return "complex"
    else:
        x_1 = (-1 * b + math.sqrt(m)) / (2 * a)
        x_2 = (-1 * b - math.sqrt(m)) / (2 * a)
        return (x_1, x_2)

def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    For example, [0, 1, 2, 3, 4, 5, 6, 7] => [0, 4, 1, 5, 2, 6, 3, 7]"""
    l = []
    mid = len(even_list) // 2
    for i in range(0, mid, 1):
        l.append(even_list[i])
        l.append(even_list[mid + i])
    return l

def triples_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3."""
    return [3 * i for i in input_list]

def double_consonants(text):
    """Return a new version of text, with all the consonants doubled.
    For example:  "The *BIG BAD* wolf!" => "TThhe *BBIGG BBADD* wwollff!"
    For this exercise assume the consonants are all letters OTHER
    THAN A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    s = ''
    l = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    for c in text:
        s = s + c
        if c in l:
            s = s + c
    return s

def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', '*', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ]  ).
    Convert all the letters to lower-case before the counting."""
    d = {}

    for w in re.findall("[A-Za-z0-9-+*/@#%']{1,}", text):
        if len(w) > 0:
            w = w.lower()
            d[w] = d.get(w, 0) + 1
    return d



def make_cubic_evaluator(a, b, c, d):
    """When called with 4 numbers, returns a function of one variable (x)
    that evaluates the cubic polynomial
    a x^3 + b x^2 + c x + d.
    For this exercise Your function definition for make_cubic_evaluator
    should contain a lambda expression."""
    return lambda x: a * x**3 + b * x**2 + c * x + d


class Polygon:
    """Polygon class."""

    def __init__(self, n_sides, lengths=None, angles=None):
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    def is_rectangle(self):
        """ returns True if the polygon is a rectangle,
        False if it is definitely not a rectangle, and None
        if the angle list is unknown (None)."""
        if self.n_sides != 4:
            return False

        if self.angles is None:
            for a in self.lengths:
                if self.lengths.count(a) != 2:
                    return False
            return None
        else:
            return self.angles.count(90) == 4

    def is_rhombus(self):
        if self.n_sides != 4:
            return False

        if self.lengths is None:
            if self.angles is not None:
                for a in self.angles:
                    if self.angles.count(a) < 2:
                        return False
            return None

        if self.lengths.count(self.lengths[0]) != 4:
            return False
        else:
            return True

    def is_square(self):
        if self.angles is None:
            return None
        return self.angles.count(90) == 4 and self.is_rhombus()

    def is_regular_hexagon(self):
        if self.n_sides != 6:
            return False

        if self.angles is None:
            if self.lengths is not None and self.lengths.count(self.lengths[0]) != 6:
                return False
            return None
        else:
            return self.angles.count(120) == 6

    def is_isosceles_triangle(self):
        if self.n_sides != 3:
            return False

        if self.lengths is not None:
            if self.lengths.count(self.lengths[0]) < 2 and self.lengths.count(self.lengths[1]) < 2:
                return False
            else:
                return True

        if self.angles is not None:
            if self.angles.count(self.angles[0]) < 2 and self.angles.count(self.angles[1]) < 2:
                return False
            else:
                return True
        return None

    def is_equilateral_triangle(self):
        if self.n_sides != 3:
            return False

        if self.lengths is not None:
            if self.lengths.count(self.lengths[0]) == 3:
                return True
            else:
                return False

        if self.angles is not None:
            if self.angles.count(60) == 3:
                return True
            else:
                return False
        return None

    def is_scalene_triangle(self):
        if self.n_sides != 3:
            return False

        if self.lengths is not None:
            return self.lengths.count(self.lengths[0]) == 1 and self.lengths.count(self.lengths[1]) == 1

        if self.angles is not None:
            return self.angles.count(self.angles[0]) == 1 and self.angles.count(self.angles[1]) == 1

        return None
