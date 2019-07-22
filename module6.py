#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #calculate housing price increase
    orig_price = 100
    rate = 0.1 #yearly increasing rate
    def housing_price(varOrig_price, varRate):
        varOrig_price *= (1+varRate)
        return varOrig_price
    orig_price= housing_price(orig_price, rate)
    print orig_price

if __name__ == '__main__':
    main()
