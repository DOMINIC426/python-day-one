

# extract the name from the email
email = "nazarethdominic@gmail.com"

# Get position of @ 
indexOfEmail = email.find("@")
name =email[:indexOfEmail]
print(name)
print(name.count("n"))  # counts how many times the n appears in name 

special = "hey this is haland from \"viking\" followed by mbape"

print(special)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 