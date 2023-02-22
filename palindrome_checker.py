#!/usr/bin/env python3

"""
palindrome_checker.py 


includes a class definition for PalindromeChecker that includes at least two methods:

a setter method setStrictMode() that takes a boolean value as input, which turns "strict mode" on and off

a boolean method isPalindrome(phrase) that takes a phrase as a parameter and returns true 
if the phrase is a palindrome, and false if it isn't. This method should use a Deque object to 
check the expression, and return True if the expression entered is a valid palindrome.
If "strict mode" is on, a palindrome will only be indicated if the phrase reads exactly the same, 
forwards and backwards, including spaces, punctuation, and case (upper and lower). 
If "strict mode" is off, then spaces, punctuation, and different cases are allowed, 
and the phrase will be identified as a palindrome because their letters all match.

You may wish to write an additional helper method sanitize(phrase) that will produce a new, 
"sanitized" version of a phrase that doesn't have any spaces, punctuation, or 
uppercase letters in it. This method can be useful when "strict mode" is off.

The main() function in the palindrome_checker.py can be used to perform a series of tests.
"""
from atds import *
import string

__author__ = "Kaylin Yagura"
__version__ = "2/15/23"


class PalindromeChecker:
    def __init__(self):
        self.strict = True
        self.san= ""

    def set_strict_mode(self, strict_change):
        self.strict = strict_change

    def sanitize(self, phrase):
        for x in string.punctuation:
            phrase = phrase.replace(x, "")
        phrase = phrase.replace(" ", "")
        phrase = phrase.lower()
        self.san = phrase
        return self.san

    def is_palindrome(self, phrase):
        d = Deque()
        m = Deque()
        
        
        if len(phrase) == 0:
            return False
        elif len(phrase) == 1:
            return True
        elif self.strict == True:
            y = 0
            while y < len(phrase):
                m.add_rear(phrase[y])
                y += 1
            print(m.print_deque())

            middle = int(len(phrase) / 2)
            x = middle - 1
            d.add_front(phrase[middle])
            while x >= 0:
                d.add_front(phrase[x])
                d.add_rear(phrase[x])
                x -= 1
            print(d.print_deque())
            print(d.compare(m))
            print("hello!")
        elif self.strict == False:
            self.sanitize(phrase)
            print(self.san)
            y = 0
            while y < len(self.san):
                m.add_rear(self.san[y])
                y += 1
            print(m.print_deque())

            middle = int(len(self.san) / 2)
            x = middle - 1
            d.add_front(self.san[middle])
            while x >= 0:
                d.add_front(self.san[x])
                d.add_rear(self.san[x])
                x -= 1
            print(d.print_deque())
            print(d.compare(m))


def main():
    print("Palindrome Checker!")
    p = PalindromeChecker()
    strict = input("Do you want strict mode on or off? ")
    phrase = input("Enter phrase here: ")
    
    if strict == "on":
        p.set_strict_mode(True)
    else:
        p.set_strict_mode(False)

    p.is_palindrome(phrase)


if __name__ == "__main__":
    main()
