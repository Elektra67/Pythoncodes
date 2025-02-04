##################STRINGS################
Str1 = "hello"
str2 ='Reet'

Str3= "hello Reetika \nWelcome to the screen"
print(Str3)

Mainstr= Str1+ " " +str2  ####CONCATENATION
print(Mainstr)

length = len(Str1)  ####LENGTH
print(length)

###### str2[0]= R   
print(str2[3]) ####INDEXING HELPS IN ACCESSING THE CHARACTERS


####SLICING -- to get parts of the strings
slcing = Str3[2:11]
print(slcing)

print(str2.endswith("oi"))  #### returns true if ends with the substr

strn ="Reetika paul verma"
print(strn.count("a"));




a = int(input("hi can we have your marks please?"))
print("Your marks is ",a)
if(a >=90):
    print("your Grade is A")
elif(a<90 and a>=80):
    print("your Grade is B")
elif(a<80 and a>=70):
    print("your Grade is C")
else:
    print("Sorry");


