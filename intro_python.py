#Script to demo python

print("Hello World!") #print stuff

var1 = "String"  #setting a String Variable
var2 = 64  #setting a Int Variable or float
var3 = True  #setting a Boolean Variable

print(type(var2), var2)

var4 = "32"
var5 = str(var2) #I am typecasting var2 --> string

print(type(var5), var5)

var2 = "Reassigned" #reassign va2

print(type(var2), var2) #print difference

var6 = float(input("Enter a number: "))

print("Your number is: ", type(var6), var6)
