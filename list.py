
## this are mutable means can be change after its creation 
## are well ordered and organized 
## use indexing 

## normal list

list1 = ["Pythics","Chemistry","Biology"]
list1.insert(0,"Civics")
list1.append("Mathematics")

for i in list1 :
    print("Book number "+format(list1.index(i)+1)+".............")
    print(i)



#### string with special instructors

list2 = list(("embe","chugwa","limao","mango"))
print(list1[1:3])

print(list2)