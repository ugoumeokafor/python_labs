#-------------------------------------------------------------------------------
# Name:        module7
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    orig_prices = [100,200,300]
    rate = 0.1
    def housing_price2(orig_prices,rate):
        new_hous_prices = []
        for items in orig_prices:
            items *= (1 + rate)
            new_hous_prices.append (items)
        print "The current values for original prices are: \n", new_hous_prices
    housing_price2 (orig_prices, rate)
    print "the updated prices are \n",  orig_prices











'''

            orig_prices *= (1+ (orig_prices), rate)
    orig_prices = housing_price2(orig_price, rate)

        #orig_prices = (*1+ str(orig_prices)+ rate)
        #orig_prices = housing_price2(orig_prices,rate)
    print orig_prices
    '''

if __name__ == '__main__':
    main()
