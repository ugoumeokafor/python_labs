#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      ufu1
#
# Created:     06/02/2017
# Copyright:   (c) ufu1 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #break statement in a loop
    for i in range(1,10):
        if i%7 == 0:
            print "okay, I will stop at "+str(i)+" no more iteration!"
            continue
    else:
        print "the current num is :"+str(i)



if __name__ == '__main__':
    main()
