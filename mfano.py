
# try   to use well the  dictionary

person ={
    "name":"Dominic",
    "age":2,
    "height":30,
    "scores":[30,70,40]
}


# print("The name of the person is ",person['name'], "and scores at index one is \n",*person["scores"])
# print(person)

people = [

  {
    "name":"Dominic",
    "age":40,
    "subjects":["Kiswahili","Hisabati","English"]
  },
  {
    "name":"Jamana",
    "age":43,
    "subjects":["Kiswahili","Hisabati","English"]
  }
]

print(*people[0]['subjects'])