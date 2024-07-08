# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(attributes):
    import math
    l = []
    z = 0
    m = 0
    for i in attributes:
        if int(i)>250:
            z=1
        else:
            x = math.ceil(int(i)/10)
            y = x*10 - int(i)
            l.append((x,y))
            m = m + int(i)
    if z == 1 or m>=500:
        return "No medicine given"
    else:
        return l