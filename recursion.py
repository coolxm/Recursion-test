#avoid thinking abt the recursion
#start with the prolem that you can already solve
    #two integer arrays that have the same length
        #sensors : same, maybe small difference
        #calculate the total absolute difference
#make a funtion that gives the first function one element less
    #return that function to itself

sensorA = [15, -4, 56, 10, -3]
sensorB = [14, -9, 56, 14, -2]

#def iterative(sensorA, sensorB, len):
#    diff = 0 #
#    for i in range(0, len):#
#        diff += abs(sensorA[i#] - sensorB[i])
#    return diff

def dispatch(sensorA, sensorB, len):
    if len == 0:
        return 0
    else:
        lastdiff = abs(sensorA[len - 1] - sensorB[len - 1])
        diff = dispatch(sensorA, sensorB, len - 1) + lastdiff
    return diff

print (dispatch(sensorA, sensorB, len(sensorA)))