
name = input("please enter your name ")

umri = input("Please enter your age ")

age = int(umri)
email = "@gmail.com"

if age < 18:
    print("ooooh Sorry your very a little guy")
    print("Your email will be ",f"{name.lower()}{email}")
elif age > 18 and age<35:
    print( "Dear",name,"Your a young person")
else:
    print("hahahhahah Your are matured eneough aisee")



