## this are immutable 
## cannot be updated maybe we can covert them into list by doing casting

myTuple = ("sangara","kambare","dagaa","dun")

# add an item we have to cast and then update it 

updateTuple = list(myTuple)
updateTuple.append("samaki added")

# covert back to tuple
myTuple =tuple(updateTuple)

print(myTuple)