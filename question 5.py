#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ufu1
#
# Created:     08/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    for num in range(1,101): #defining the range of numbers
        if num % 3 == 0 and num % 5 == 0: #numbers divisible by 3 and 5
            print "FizzBuzz"
        elif num % 3 == 0: #numbers divisible by 3 only
            print "Fizz"
        elif num % 5 == 0: #numbers divisible by 5 only
            print "Buzz"

        else: #numbers not divisible by either 3 or 5
            print num

if __name__ == '__main__':
    main()
