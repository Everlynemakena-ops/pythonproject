

age = 67 #Integer
height = 3.5 #Float
greeting = "Hey Hey" #String
ispythoninteresting = True #Boolean


#Data Strucures - A single variable storing multiple values

cars = ["Toyota","Ford","Mercedez","Mustang"] #List - Ordered and changeable
fruits = ( "Banana","Orange","Mango") #Tuple - ordered but unchangeable
countries = { "China","France","Germany","Italy"} #set -unordered and unchageable


#Dictionery- stores data in key value pairs
user_profile = {"username":"evelyne","role":"Developer","age":25,"is_active":True}

print(user_profile)
print(user_profile["username"])
print(user_profile.get("role"))




#updates the age if it exists
user_profile["age"] = 26

#pop key- removes a specific key and returns its value
user_profile.pop("is_active")




#Array-uses list which can hold multiple items of any data type.
# A list of scores (acting as an array)
scores = [85,90,78,92,88]

#Accessing items by index
print(scores[0])
print(scores[2])


#changing an item
scores[1] = 95
print(scores)



print(age)
print(height)
print(fruits)
print(cars)
print(countries)



#Typecasting- converts variable from one datatype to abother
age = int(25)
next_year = age + 1

print(f"Next year,i will be {next_year} years old.")