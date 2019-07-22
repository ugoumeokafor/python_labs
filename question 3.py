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
    #while-loop for repeatable jobs
    num = (0+1+2+3+4+5+6+7+8+9)
    while num<10:
        print 'the sum of the num is :'+str(num)
        num = num +1
    else:
        print 'the sum of the num is ' +str(num)

if __name__ == '__main__':
    main()
