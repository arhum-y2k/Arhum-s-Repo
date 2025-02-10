#!/usr/bin/python

### ----------------------------------------------------------------------------------------------------
# File name   : prime_number_gen.py
#
# Author      : Arhum Alam
#
# Description : The code should print out a list of all the prime numbers between 0 and 100.
#               The language used can be anything familiar (Python, Perl, C etc.) , or even just a
#               "pseudocode" language as long as it is clear and unambiguous and fully illustrates the
#               approach taken.
#               The exact syntax is much less important than the algorithm and clear expression of intent
#               (e.g. a missing semicolon is not important).
#               The purpose of the exercise is to show how a specification has been met by implementing
#               a particular algorithm in code.
### ----------------------------------------------------------------------------------------------------

def print_prime_nums():
    # Loop over the numbers between 0 and 100 (exclusive)
    for num in range(0, 100):
        # A control flag to indicate when a non-prime number is encounterd
        prime_flag = 1

        # By definition, a prime number should be greater than 1.
        # And have no divisor other than 1 and itself.
        if num > 1:
            for div in range(2, num):
                # Modulus operation to check if "div" is a divisor of "num".
                # If it is, toggle off the prime_flag and break from loop (there is no need
                # to continue with "num" if we have already found it's not a prime number)
                if (num % div) == 0:
                    prime_flag = 0
                    break

            # If "num" is not divisible by 2 =< div < num, then "prime_flag" should still be 1
            if prime_flag:
                print(num)

def main():
    print_prime_nums()

if __name__ == "__main__":
    main()