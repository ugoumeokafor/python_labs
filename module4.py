#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    # find out whether a list has 1 item called ?Adele?
    name_list = ['Fred','Niaz','Adele','Monica']
    for item in name_list:
        if item =='Adele':
            print "I found Adele!"
        else:
            print "I did not find Adele in the list"

if __name__ == '__main__':
    main()
# a concise way
if "Adele" in name_list:
    print "I found Adele again!"
else:
    print "I didnt find it"

