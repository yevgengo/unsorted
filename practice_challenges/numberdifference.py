#!/usr/local/bin/python
import math

def findthepairs(ourlist=[1,2], difference=1):
    numpairs=0
#    secondposition=1
#    if (len(ourlist)>1):
#        for first in ourlist[:-1]:

#            for second in ourlist[secondposition::]:
#                if (abs(second-first)==difference):
#                    numpairs=numpairs+1
#            secondposition=secondposition+1

#        print (numpairs)
#    return ( numpairs % 109)

    ourhashmap={}
    for element in ourlist:
        if (element + difference) in ourhashmap.keys():
            ourhashmap[element+difference] += 1
        else:
            ourhashmap[element+difference] = 1

        if (element - difference) in ourhashmap.keys():
            ourhashmap[element-difference] += 1
        else:
            ourhashmap[element-difference] = 1

    for key,value in ourhashmap.items():
            numpairs+=value-1
    # print (ourlist)
    # print (ourhashmap)
    return numpairs % 1000000007



print(findthepairs([1,6,8,2,4,9,12],3))
