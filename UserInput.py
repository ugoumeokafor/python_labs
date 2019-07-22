#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ufu1
#
# Created:     30/01/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Get user input
def main():
    myResponse = raw_input("Please enter a number")
    floatValue = float(myResponse)
    print str( floatValue ) + " is a good number, thanks!"

if __name__ == '__main__':
    main()
