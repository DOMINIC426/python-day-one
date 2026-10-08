# are immutable always 
# do not allow duplicate values 
# do not use index and are unordered so we are not sure of their position , so anytihing can appeear there
## if duplcates occours it will result into not printing it only , no more effect 

mySet ={ "Jamana","Jambo Books", "Msomi","This is set" }
setTwo = {"ugali","wali","chapati","maandazi","This is set"}

mySet.add("new item added")
mySet.pop()   ## removes any from the list 

print(mySet.union(setTwo))
print("the intersection of two sets is "+format(mySet.intersection(setTwo)))