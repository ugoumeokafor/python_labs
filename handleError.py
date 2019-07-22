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

def main():
    try:
        myResponse = raw_input("Please enter a number")
        floatValue = float(myResponse)
        print 'floatValue' + " is a good number, thanks!"
    except Exception as err:
            print err.message




if __name__ == '__main__':
    main()
